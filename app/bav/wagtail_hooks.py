# from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
# from app.bav.models import BavItem
from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import AdminOnlyMenuItem

from app.bav.views import ImagesReportView

# class BavItemAdmin(ModelAdmin):
#     model = BavItem
#     list_display = ("file_name", "title", "scanned", "malicious", "waiting_for_scan", "updated_at", "created_at")
#     ordering = ("-malicious", "-updated_at",)
#     # list_filter = ("malicious", "scanned", "waiting_for_scan")


# modeladmin_register(BavItemAdmin)


@hooks.register('register_reports_menu_item')
def register_images_report_view_meny_item():
    return AdminOnlyMenuItem("Bucket Scans", reverse('image_report_view'), classnames='icon icon-' + ImagesReportView.header_icon, order=700)


@hooks.register('register_admin_urls')
def images_report_urls():
    return [
        path('admin/reports/images_log/', ImagesReportView.as_view(), name='image_report_view'),
    ]

# @hooks.register('register_log_actions')
# def images_report_action(actions):
#     actions.register_action('wagtail_package.echo', 'Echo', 'Sent an echo')
