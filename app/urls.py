from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    # Customer Urls
    path("",home,name='home'),
    path("course/<int:pk>",course,name='course'),
    path("course/register/<int:pk>",register,name='register'),
    path('success/',success,name='success'),
    path('payment/<int:pk>',pay,name='payment'),
    #Student Urls
    path('login',stu_login,name='stu_login'),
    path('logout_stu',logout_stu,name='logout_stu'),
    path('student_register',stu_register,name='stu_register'),
    path('student_portal',stu_portal,name='stu_portal'),
    #Admin Panel Urls
    path('ad',admin_home,name='admin_home'),
    path('login_admin',login_admin,name='admin_login'),
    path('logout_admin',logout_admin,name='admin_logout'),
    path('ad/course_manage',course_manage,name='course_manage'),
    path('ad/course_manage/edit/<int:pk>',edit_course,name='course_edit'),
    path('ad/students',student_manage,name='student_manage'),
    path('ad/content',content_manage,name='content_manage'),
    path('index',index)
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
