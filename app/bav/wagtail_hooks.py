from django.urls import path, reverse
from django.template.loader import get_template
from django.template import Context
from wagtail import hooks
from wagtail.admin.menu import AdminOnlyMenuItem
from wagtail.images import get_image_model
from wagtail.documents import get_document_model


from wagtail.admin.ui.components import Component
from wagtail import hooks

from app.bav.views import ImagesReportView, DocumentsReportView


class BucketAVPanel(Component):
    order = 1000

    def render_html(self, parent_context=None):
        if parent_context is None:
            parent_context = Context()
        context_data = self.get_context_data(parent_context)
        if context_data is None:
            raise TypeError("Expected a dict from get_context_data, got None")
        context_data["total_scanned_images"] = (
            get_image_model().objects.filter(scanned=True).count()
        )
        context_data["total_malicious_images"] = (
            get_image_model().objects.filter(malicious=True).count()
        )
        context_data["total_scanned_documents"] = (
            get_document_model().objects.filter(scanned=True).count()
        )
        context_data["total_malicious_documents"] = (
            get_document_model().objects.filter(malicious=True).count()
        )

        template = get_template("scanned.html")
        return template.render(context_data)


@hooks.register("construct_homepage_panels")
def bucket_av_panel(request, panels):
    panels.append(BucketAVPanel())


@hooks.register("register_reports_menu_item")
def register_images_report_view_menu_item():
    return AdminOnlyMenuItem(
        "Image Scan Report",
        reverse("image_report_view"),
        classnames="icon icon-" + ImagesReportView.header_icon,
        order=700,
    )


@hooks.register("register_admin_urls")
def images_report_urls():
    return [
        path(
            "reports/images_log/",
            ImagesReportView.as_view(),
            name="image_report_view",
        ),
    ]


@hooks.register("register_reports_menu_item")
def register_documents_report_view_menu_item():
    return AdminOnlyMenuItem(
        "Docs Scan Report",
        reverse("documents_report_view"),
        classnames="icon icon-" + DocumentsReportView.header_icon,
        order=700,
    )


@hooks.register("register_admin_urls")
def documents_report_urls():
    return [
        path(
            "reports/documents_log/",
            DocumentsReportView.as_view(),
            name="documents_report_view",
        ),
    ]


# class ImagesSummaryItemMalicious(SummaryItem):
#     order = 400
#     template_name = "wagtailimages/homepage/site_summary_malicious_images.html"

#     def get_context_data(self, parent_context):
#         site_name = get_site_for_user(self.request.user)["site_name"]

#         return {
#             "total_malicious_images": get_image_model()
#             .objects.filter(malicious=True)
#             .count(),
#             "site_name": site_name,
#         }

#     def is_shown(self):
#         return permission_policy.user_has_any_permission(
#             self.request.user, ["add", "change", "delete"]
#         )


# @hooks.register("construct_homepage_summary_items")
# def malicious_images_summary_item(request, items, order=900):
#     items.append(ImagesSummaryItemMalicious(request))


# class ImagesSummaryItemScanned(SummaryItem):
#     order = 400
#     template_name = "wagtailimages/homepage/site_summary_scanned_images.html"

#     def get_context_data(self, parent_context):
#         site_name = get_site_for_user(self.request.user)["site_name"]

#         return {
#             "total_scanned_images": get_image_model()
#             .objects.filter(scanned=True)
#             .count(),
#             "site_name": site_name,
#         }

#     def is_shown(self):
#         return permission_policy.user_has_any_permission(
#             self.request.user, ["add", "change", "delete"]
#         )


# @hooks.register("construct_homepage_summary_items")
# def scanned_images_summary_item(request, items, order=900):
#     items.append(ImagesSummaryItemScanned(request))

# class DocumentsSummaryItemMalicious(SummaryItem):
#     order = 400
#     template_name = "wagtaildocs/homepage/site_summary_malicious_documents.html"

#     def get_context_data(self, parent_context):
#         site_name = get_site_for_user(self.request.user)["site_name"]

#         return {
#             "total_malicious_documents": get_document_model()
#             .objects.filter(malicious=True)
#             .count(),
#             "site_name": site_name,
#         }

#     def is_shown(self):
#         return permission_policy.user_has_any_permission(
#             self.request.user, ["add", "change", "delete"]
#         )


# @hooks.register("construct_homepage_summary_items")
# def malicious_documents_summary_item(request, items, order=900):
#     items.append(DocumentsSummaryItemMalicious(request))


# class DocumentsSummaryItemScanned(SummaryItem):
#     order = 400
#     template_name = "wagtaildocs/homepage/site_summary_scanned_documents.html"

#     def get_context_data(self, parent_context):
#         site_name = get_site_for_user(self.request.user)["site_name"]

#         return {
#             "total_scanned_documents": get_document_model()
#             .objects.filter(scanned=True)
#             .count(),
#             "site_name": site_name,
#         }

#     def is_shown(self):
#         return permission_policy.user_has_any_permission(
#             self.request.user, ["add", "change", "delete"]
#         )


# @hooks.register("construct_homepage_summary_items")
# def scanned_documents_summary_item(request, items, order=900):
#     items.append(DocumentsSummaryItemScanned(request))
