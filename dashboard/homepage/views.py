from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class home(TemplateView):
    template_name = 'home/Homepage.html'
    
class product(TemplateView):
    template_name = 'home/product.html'
    
class contact_us(TemplateView):
    template_name = 'home/contact_us.html'
