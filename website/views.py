#  hello/views.py

from django.shortcuts import render


def home_page_view(request):
    return render(request, 'website/layout.html')


def layout_filho1_page_view(request):
    return render(request, 'website/layoutFilho1.html')


def layout_filho2_page_view(request):
    return render(request, 'website/layoutFilho2.html')


def layout_filho3_page_view(request):
    return render(request, 'website/layoutFilho3.html')
