from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import AdminOnlyMenuItem
from wagtail.images.wagtail_hooks import ImagesSummaryItem as SummaryItem

from app.bav.views import ImagesReportView
from wagtail.admin.navigation import get_site_for_user
from wagtail.images import get_image_model

@hooks.register('register_reports_menu_item')
def register_images_report_view_meny_item():
    return AdminOnlyMenuItem("Bucket Scans", reverse('image_report_view'), classnames='icon icon-' + ImagesReportView.header_icon, order=700)


@hooks.register('register_admin_urls')
def images_report_urls():
    return [
        path('admin/reports/images_log/', ImagesReportView.as_view(), name='image_report_view'),
    ]

# class ImagesSummaryItem(SummaryItem):
#     # order = 200
#     # template_name = "wagtailimages/homepage/site_summary_images.html"

#     def get_context_data(self, parent_context):
#         site_name = get_site_for_user(self.request.user)["site_name"]

#         return {
#             "total_images": get_image_model().objects.count(),
#             "site_name": site_name,
#         }

#     # def is_shown(self):
#     #     return permission_policy.user_has_any_permission(
#     #         self.request.user, ["add", "change", "delete"]
#     #     )


# # @hooks.unregister('construct_homepage_summary_items')
# # def construct_homepage_summary_items(request, items):
# #     pass

# @hooks.register("construct_homepage_summary_items")
# def add_images_summary_item(request, items, order=900):
#     items.append(ImagesSummaryItem(request))
