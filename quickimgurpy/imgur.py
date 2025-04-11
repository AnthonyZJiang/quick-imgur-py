import os
import base64
import requests
from io import BytesIO
from urllib.parse import urlparse
from dotenv import load_dotenv

class ImgurClient:
    BASE_URL = "https://api.imgur.com/3"
    
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("IMGUR_CLIENT_ID")
        self.client_secret = os.getenv("IMGUR_CLIENT_SECRET")
        self.refresh_token = os.getenv("IMGUR_REFRESH_TOKEN")
        self.access_token = None
        
        if not all([self.client_id, self.client_secret, self.refresh_token]):
            raise ValueError("Missing required environment variables. Please check your .env file.")
        
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Imgur API using refresh token"""
        auth_url = "https://api.imgur.com/oauth2/token"
        data = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token"
        }
        
        response = requests.post(auth_url, data=data)
        response.raise_for_status()
        self.access_token = response.json()["access_token"]
    
    def _get_headers(self):
        """Get headers with authentication"""
        return {
            "Authorization": f"Bearer {self.access_token}"
        }
    
    def _is_url(self, data):
        """Check if the input is a valid URL"""
        try:
            result = urlparse(data)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def _download_from_url(self, url):
        """Download content from URL"""
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    
    def _prepare_file(self, image_data, force_base64=False):
        """Prepare image data for upload"""
        if self._is_url(image_data):
            if force_base64:
                file_bytes = self._download_from_url(image_data)
            else:
                return "url", image_data
        elif isinstance(image_data, str):
            # If it's a file path
            with open(image_data, "rb") as f:
                file_bytes = f.read()
        elif isinstance(image_data, BytesIO):
            file_bytes = image_data.getvalue()
        else:
            # If it's already bytes
            file_bytes = image_data
            
        return "base64", base64.b64encode(file_bytes).decode('utf-8')
    
    def upload_image(self, image_data, title=None, description=None, force_base64=False):
        """
        Upload an image to Imgur
        
        Args:
            image_data: Can be a file path, URL, BytesIO object, or bytes
            title (optional): Title for the image
            description (optional): Description for the image
            
        Returns:
            dict: Response from Imgur API
        """
        url = f"{self.BASE_URL}/image"
        
        upload_type, data = self._prepare_file(image_data, force_base64)
        data = {
            "image": data,
            "type": upload_type
        }

        response = requests.post(url, headers=self._get_headers(), data=data)
        response.raise_for_status()
        return response.json()
    
    def upload_video(self, video_data, title=None, description=None, disable_audio=False, force_base64=False):
        """
        Upload a video to Imgur
        
        Args:
            video_data: Can be a file path, URL, BytesIO object, or bytes
            title (optional): Title for the video
            description (optional): Description for the video
            disable_audio (optional): Disable audio in the video
            
        Returns:
            dict: Response from Imgur API
        """
        url = f"{self.BASE_URL}/image"
        
        upload_type, data = self._prepare_file(video_data, force_base64)
        data = {
            "video": data,
            "type": upload_type
        }
        
        if title:
            data["title"] = title
        if description:
            data["description"] = description
        data["disable_audio"] = disable_audio
            
        response = requests.post(url, headers=self._get_headers(), data=data)
        response.raise_for_status()
        return response.json()
