from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from rango.models import Category, Page, PageAdmin

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
