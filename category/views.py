from django.shortcuts import render
from django.views.generic import TemplateView


class CategoryView(TemplateView):
    template_name = 'index.html'