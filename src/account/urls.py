from django.contrib import admin
from django.urls import path

from account.views import smoke, UserInfoView, SignUpView, EditUserView


app_name = 'account'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smoke/', smoke, name='smoke'),  # test view
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('edit/<int:pk>/', EditUserView.as_view(), name='edit'),

]
