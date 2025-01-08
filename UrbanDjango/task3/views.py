from django.shortcuts import render
from django.views.generic import TemplateView


class PageMain(TemplateView):
    template_name = 'third_task/main.html'


class PageShop(TemplateView):

    template_name = 'third_task/shop.html'


class PageBasket(TemplateView):
    template_name = 'third_task/basket.html'
