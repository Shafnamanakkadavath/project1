from django.contrib import admin

# Register your models here.
from todoself.models import task

admin.site.register(task)