import base64
from io import BytesIO
from PIL import Image
from app.config.settings import settings

def get_b64thumbnail_from_b64image(image_b64: str) -> str:
    image = base64.b64decode(image_b64)
    pil_image = Image.open(BytesIO(image))
    pil_image.thumbnail((settings.THUMBNAIL_SIZE, settings.THUMBNAIL_SIZE), Image.NEAREST)
    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")
    thumbnail_b64 = base64.b64encode(buffered.getvalue()).decode('ascii')
    return thumbnail_b64


