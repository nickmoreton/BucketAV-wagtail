from wagtail.core.models import Page
from wagtail.images import get_image_model
from app.bav.views import scan_hook_simulation


class HomePage(Page):
    def get_context(self, request, *args, **kwargs):
        """Set an image status and return the image status of all images"""
        filename = request.GET.get("filename")
        result = request.GET.get("result")
        images = get_image_model().objects.all()
        if filename and result:
            scan_hook_simulation(filename, result)

        context = super().get_context(request, *args, **kwargs)
        context["images"] = images

        return context
