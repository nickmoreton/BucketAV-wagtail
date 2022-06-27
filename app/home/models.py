from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page
from wagtail.documents import get_document_model
from wagtail.fields import RichTextField
from wagtail.images import get_image_model, get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel

from app.bav.views import (document_scan_hook_simulation,
                           image_scan_hook_simulation)


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        """Set an image status and return the image status of all images"""
        filename = request.GET.get("filename")
        result = request.GET.get("result")
        type = request.GET.get("type")

        images = get_image_model().objects.all()
        documents = get_document_model().objects.all()

        if filename and result and type == "image":
            image_scan_hook_simulation(filename, result)

        if filename and result and type == "document":
            document_scan_hook_simulation(filename, result)

        context = super().get_context(request, *args, **kwargs)
        context["images"] = images
        context["documents"] = documents

        return context


class StandardPage(Page):
    body = RichTextField(blank=True)

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        ImageChooserPanel("image"),
    ]
