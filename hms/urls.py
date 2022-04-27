from django.contrib import admin
from django.urls import path
from hms import views
admin.site.site_header = "21BCS_407GPA_T3 Hospital || Admin Page"
admin.site.site_title = "Team7"
admin.site.index_title = "view patient details"
urlpatterns = [
    path('', views.index, name='hms'),
    path('register', views.register, name='register'),
    path('index', views.index, name='hms'),
    path('save', views.sdetails, name='sdetails'),
    path('view', views.view, name='showdetails'),
    path('comingSoon', views.sed, name='sed')
]
