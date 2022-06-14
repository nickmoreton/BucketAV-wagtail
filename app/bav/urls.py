from django.urls import path
from .views import scan_hook

urlpatterns = [
    path("scan-hook/", scan_hook, name="scan_hook"),
]
