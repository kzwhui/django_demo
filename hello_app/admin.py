from django.contrib import admin
from models import TStudentInfo

# Register your models here.
class TStudentInfoAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_score', 'c_modify_time', 'c_create_time')

admin.site.register(TStudentInfo, TStudentInfoAdmin)