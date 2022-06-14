from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image
from django.urls import reverse

# from wagtail.log_actions import log


class CustomImage(AbstractImage):
    scanned = models.BooleanField(default=False)
    malicious = models.BooleanField(default=False)
    admin_form_fields = Image.admin_form_fields

    def get_delete_url(self):
        return reverse("wagtailimages:delete", args=(self.id,))


class Rendition(AbstractRendition):
    image = models.ForeignKey(
        "CustomImage", related_name="renditions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
