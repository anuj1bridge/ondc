from django.urls import path
from . import views

app_name = "scanner"

urlpatterns = [
    path("", views.scan_qr_code, name="scan-qr-code"),
    path("send-to-shopify", views.send_to_shopify, name="send_to_shopify"),
]
