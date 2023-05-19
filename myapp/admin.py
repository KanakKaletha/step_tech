from django.contrib import admin

# Register your models here.
from myapp.models import User

class ServiceAdmin(admin.ModelAdmin):
    {'first_name','last_name', 'email'}
admin.site.register(User,ServiceAdmin)