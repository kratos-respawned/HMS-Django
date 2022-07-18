from django.contrib import admin
from django.urls import path
from hms import views
admin.site.site_header = "21BCS_407GPA_T3 Hospital || Admin Page"
admin.site.site_title = "SPLIT"
admin.site.index_title = "view patient details"
urlpatterns = [
    path('', views.index, name='hms'),
    path('home', views.index, name='hms'),
    path('register', views.register, name='register'),
    path('index', views.index, name='hms'),
    path('save', views.sdetails, name='sdetails'),
    path('view', views.view, name='showdetails'),
    path('delete_view', views.delete_view, name='delete_view'),
    path('deleteBtn', views.deleteBtn, name='deleteBtn'),
]
