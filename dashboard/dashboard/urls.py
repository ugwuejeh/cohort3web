from django.contrib import admin
from django.urls import path, include
from homepage.views import home,product,contact_us

urlpatterns = [
    path('admin/', admin.site.urls),

   path('', home.as_view(), name='home'),
   
   path('product', product.as_view(), name='home'),
   
   path('contact_us', contact_us.as_view(), name='home'),

   path('index/', include('homepage.urls'))
]