from django.urls import path
from .views import home
# from .views import product

urlpatterns = [
   path('', home.as_view(), name='home'),
]