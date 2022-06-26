from django.db import models
from django.urls import reverse
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from wagtail.documents.models import Document, AbstractDocument


class CustomImage(AbstractImage):
    """Custom image model"""

    scanned = models.BooleanField(default=False)  # new field
    malicious = models.BooleanField(default=False)  # new field
    admin_form_fields = Image.admin_form_fields

    def get_delete_url(self):
        return reverse("wagtailimages:delete", args=(self.id,))


class Rendition(AbstractRendition):
    """Custom rendition model, straight out of the Wagtail docs"""

    image = models.ForeignKey(
        "CustomImage", related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class CustomDocument(AbstractDocument):
    # Custom field example:
    scanned = models.BooleanField(default=False)  # new field
    malicious = models.BooleanField(default=False)  # new field

    admin_form_fields = Document.admin_form_fields
