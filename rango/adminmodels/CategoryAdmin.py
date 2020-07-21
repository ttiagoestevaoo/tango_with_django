from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes','views','slug')
    prepopulated_fields = {'slug':('name',)}
