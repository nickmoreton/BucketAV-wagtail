from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import AdminOnlyMenuItem
from wagtail.admin.navigation import get_site_for_user
from wagtail.images import get_image_model
from wagtail.images.permissions import permission_policy
from wagtail.images.wagtail_hooks import ImagesSummaryItem as SummaryItem

from app.bav.views import ImagesReportView


@hooks.register("register_reports_menu_item")
def register_images_report_view_meny_item():
    return AdminOnlyMenuItem(
        "Bucket Scans",
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


class ImagesSummaryItemMalicious(SummaryItem):
    order = 400
    template_name = "wagtailimages/homepage/site_summary_malicious_images.html"

    def get_context_data(self, parent_context):
        site_name = get_site_for_user(self.request.user)["site_name"]

        return {
            "total_malicious_images": get_image_model()
            .objects.filter(malicious=True)
            .count(),
            "site_name": site_name,
        }

    def is_shown(self):
        return permission_policy.user_has_any_permission(
            self.request.user, ["add", "change", "delete"]
        )


@hooks.register("construct_homepage_summary_items")
def malicious_images_summary_item(request, items, order=900):
    items.append(ImagesSummaryItemMalicious(request))


class ImagesSummaryItemScanned(SummaryItem):
    order = 400
    template_name = "wagtailimages/homepage/site_summary_scanned_images.html"

    def get_context_data(self, parent_context):
        site_name = get_site_for_user(self.request.user)["site_name"]

        return {
            "total_scanned_images": get_image_model()
            .objects.filter(scanned=True)
            .count(),
            "site_name": site_name,
        }

    def is_shown(self):
        return permission_policy.user_has_any_permission(
            self.request.user, ["add", "change", "delete"]
        )


@hooks.register("construct_homepage_summary_items")
def scanned_images_summary_item(request, items, order=900):
    items.append(ImagesSummaryItemScanned(request))
