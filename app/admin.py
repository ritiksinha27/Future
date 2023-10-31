from django.contrib import admin
from .models import *
# Register your models here.
class ClientAdm(admin.ModelAdmin):
    list_display=['name','phone','email','client_id']
admin.site.register(Client,ClientAdm)

class ContentAdm(admin.ModelAdmin):
    list_display=['category','video_name','video']
admin.site.register(Course_content,ContentAdm)

class CourseAdm(admin.ModelAdmin):
    list_display=['category','description','highlight','price','photo']
admin.site.register(Course,CourseAdm)

class StudentAdm(admin.ModelAdmin):
    list_display=['name','course','amount_paid','remaining','user_id','password']
admin.site.register(Student,StudentAdm)

class LeadsAdm(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Leads,LeadsAdm)