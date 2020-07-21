
# Register your models here.
from django.contrib import admin
from rango.models import Category, Page
from .AdminModels.CategoryAdmin import CategoryAdmin
from .AdminModels.PageAdmin import PageAdmin

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)

