from django.contrib import admin
from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smoke/', views.smoke, name='smoke'),
]