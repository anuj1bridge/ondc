from django.http import HttpResponse
from django.shortcuts import render


def scan_qr_code(request):
    return render(request, "index.html")


def send_to_shopify(request):
    return HttpResponse("qr code result - " + request.GET["text"])
