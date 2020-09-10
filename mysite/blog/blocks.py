from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class GalleryBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    images = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)),
            ("alt_text", blocks.CharBlock(required=False, max_length=100)),
        ])
    )