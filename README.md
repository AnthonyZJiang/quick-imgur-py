# Quick Imgur Python Client

A simple Python client for uploading images and videos to Imgur.

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example` and fill in your Imgur API credentials:
- `IMGUR_CLIENT_ID`: Your Imgur application client ID
- `IMGUR_CLIENT_SECRET`: Your Imgur application client secret
- `IMGUR_REFRESH_TOKEN`: Your Imgur refresh token

## Usage

```python
from src.imgur import ImgurClient

# Initialize the client
client = ImgurClient()

# Upload an image from a file
response = client.upload_image(
    "path/to/your/image.jpg",
    title="My Image",
    description="A beautiful image"
)

# Upload an image from a URL
response = client.upload_image(
    "https://example.com/image.jpg",
    title="Image from URL",
    description="Downloaded from the web"
)

# Upload an image from a BytesIO object
from io import BytesIO
image_data = BytesIO()
# ... load your image data into BytesIO ...
response = client.upload_image(image_data)

# Upload a video from a file
response = client.upload_video(
    "path/to/your/video.mp4",
    title="My Video",
    description="A cool video"
)

# Upload a video from a URL
response = client.upload_video(
    "https://example.com/video.mp4",
    title="Video from URL",
    description="Downloaded from the web"
)

# The response will contain the Imgur URL and other metadata
print(response["data"]["link"])
```

## Error Handling

The client will raise exceptions for:
- Missing environment variables
- Authentication failures
- Upload failures
- Invalid URLs
- Failed downloads from URLs

Make sure to handle these exceptions appropriately in your code.

## Imgur upload limits
See: [What files can I upload? Is there a size limit?](https://help.imgur.com/hc/en-us/articles/26511665959579-What-files-can-I-upload-Is-there-a-size-limit)

## License

MIT 