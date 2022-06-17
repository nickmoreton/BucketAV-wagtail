from django.http import HttpResponse, HttpResponseNotFound
from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.views.reports import ReportView
from wagtail.images import get_image_model

# from wagtail.log_actions import log
from wagtail.models import ModelLogEntry
from wagtail.images import get_image_model


class ImagesReportFilterSet(WagtailFilterSet):
    class Meta:
        model = get_image_model()
        fields = ["scanned", "malicious"]


class ImagesReportView(ReportView):
    template_name = "bav/reports/image_report.html"
    title = "Image Report"
    header_icon = "image"
    list_export = ["id", "title", "malicious", "scanned"]
    filterset_class = ImagesReportFilterSet

    def get_queryset(self):
        return get_image_model().objects.all().order_by("-malicious")


def scan_hook(request):
    #  http://localhost:8000/bav/scan-hook/?filename=alesia-kazantceva-VWcPlbHglYc-unsplash.jpg&result=1

    filename = request.GET.get("filename")
    result = request.GET.get("result")
    # print(filename, result)

    """
    This gets an image by it's filename.
    Wagtail never has duplicate file names, file system would error too. 
    They are appended with a hash if they are accepted duplicates.
    Wagtail takes care of this ???
    """
    image_obj = (
        get_image_model().objects.filter(file="original_images/" + filename).all()
    )

    # I suppose it's not a bad idea to check though
    if len(image_obj) == 1 and result == "1":
        image_obj.update(scanned=True, malicious=True)
        # log(image_obj, "wagtail_package.echo", data={"scanned": True, "malicious": True})
        return HttpResponse("Bad")
    elif len(image_obj) == 1 and result == "0":
        image_obj.update(scanned=True, malicious=False)
        # log(image_obj, "wagtail_package.echo", data={"scanned": True, "malicious": False})
        return HttpResponse("Good")
    else:
        # show we return a 404 or 200?
        return HttpResponseNotFound("Image not found")
