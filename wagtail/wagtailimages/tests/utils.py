import PIL.Image

from django.core.files.images import ImageFile
from django.utils.six import BytesIO

from wagtail.wagtailimages.models import get_image_model


Image = get_image_model()


def get_test_image_file(filename='test.png'):
    f = BytesIO()
    image = PIL.Image.new('RGB', (640, 480), 'white')
    image.save(f, 'PNG')
    return ImageFile(f, name=filename)
