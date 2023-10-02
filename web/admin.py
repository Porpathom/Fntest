from django.contrib import admin
from web.models import Employ, Department
# Register your models here.
# admin.site.register(Employ)
# admin.site.register(Department)

@admin.register(Employ)
class EmployAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'sex', 'age', 'education', 'dep']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', ]

