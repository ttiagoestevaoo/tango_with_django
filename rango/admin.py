
# Register your models here.
from django.contrib import admin
from rango.models.Category import Category
from rango.models.Page import Page

from .adminmodels.CategoryAdmin import CategoryAdmin
from .adminmodels.PageAdmin import PageAdmin

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)

