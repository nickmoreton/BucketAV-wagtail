from wagtail.core.models import Page
from wagtail.images import get_image_model
from wagtail.documents import get_document_model
from app.bav.views import image_scan_hook_simulation, document_scan_hook_simulation


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
