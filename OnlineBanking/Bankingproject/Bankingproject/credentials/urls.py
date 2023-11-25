from . import views
from django.urls import path
app_name='credentials'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('new/',views.new,name='new'),
    path('form1/',views.form1,name='form1'),
    path('nn/',views.nn,name='nn'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('apply/',views.apply,name='apply'),

]