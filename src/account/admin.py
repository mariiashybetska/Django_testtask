from django.contrib import admin
from account.models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'date_of_birth',
              'bio', 'email', 'phone', 'username']


admin.site.register(User, UserAdmin)

