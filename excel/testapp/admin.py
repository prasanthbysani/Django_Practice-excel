from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class ViewAdmin(admin.ModelAdmin):
    pass

admin.site.register(abhyudaya,ImportExportModelAdmin)
admin.site.register(ahmedabad,ImportExportModelAdmin)
