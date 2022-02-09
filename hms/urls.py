from django.contrib import admin
from django.urls import path
from hms import views
admin.site.site_header="TechnoKrat Hospital || Admin Page"
admin.site.site_title="TechnoKrat"
admin.site.index_title="view patient details"
urlpatterns = [
    path('',views.index,name='hms'),
    path('register',views.register,name='register'),
    path('index',views.index,name='hms'),
    path('save',views.sdetails,name='sdetails')
]
