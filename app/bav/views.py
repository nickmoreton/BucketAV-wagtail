from wagtail.admin.filters import WagtailFilterSet
from wagtail.admin.views.reports import ReportView
from wagtail.images import get_image_model
from wagtail.documents import get_document_model


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


def image_scan_hook_simulation(filename, result):
    """Simulate an endpoint to be called by the scan hook.
    Gets an image (custom image model) by it's original filename and update it's status."""
    image_obj = get_image_model().objects.filter(file=filename)

    if result == "1":
        image_obj.update(scanned=True, malicious=True)
    elif result == "0":
        image_obj.update(scanned=True, malicious=False)
    elif result == "2":
        image_obj.update(scanned=False, malicious=False)


class DocumentsReportFilterSet(WagtailFilterSet):
    class Meta:
        model = get_document_model()
        fields = ["scanned", "malicious"]


class DocumentsReportView(ReportView):
    template_name = "bav/reports/document_report.html"
    title = "Document Report"
    header_icon = "doc-full"
    list_export = ["id", "title", "malicious", "scanned"]
    filterset_class = DocumentsReportFilterSet

    def get_queryset(self):
        return get_document_model().objects.all().order_by("-malicious")


def document_scan_hook_simulation(filename, result):
    """Simulate an endpoint to be called by the scan hook.
    Gets a document (custom document model) by it's original filename and update it's status."""
    document_obj = get_document_model().objects.filter(file=filename)

    if result == "1":
        document_obj.update(scanned=True, malicious=True)
    elif result == "0":
        document_obj.update(scanned=True, malicious=False)
    elif result == "2":
        document_obj.update(scanned=False, malicious=False)
