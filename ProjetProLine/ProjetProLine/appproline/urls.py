from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path ('ApplicationWeb',views.Appli_web1),
    path ('ApplicationWeb',views.Appli_web2),
    path ('ApplicationWeb',views.Appli_web_Admin),   
]
