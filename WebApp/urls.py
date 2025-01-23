# from WebApp.views import contact,about,properties,property,userdata
from django.urls import path
from WebApp.views import *

urlpatterns = [
    path('contact/',contact,name='contact'),
    path('about-us/',about,name='about'),
    path('properties',properties,name='properties'),
    path('property',property,name='property'),
    path('user/<name>',userdata,name='user'),
    path('user/',userdata,name='userdefault'),
    # path('insert/',insert,name='insert'),
    path('insert_data/',insert_form_data,name='insert_data'),
    path('read_model/',read_model_data,name='read_model'),
    path('read_model/<page_no>',read_model_data,name='read_model_pages'),
    path('update/<id>',update_data,name='update'),
    path('delete/<id>',delete_data,name='delete'),
    path('products/',products,name='products'),
    path('upload_products/',upload_products,name='upload_products'),
    path('download/<id>',download,name='download'),
    path('setcookies/',setcookies),
    path('getcookies/',getcookies),
    path('setsession/',setsession),
    path('getsession/',getsession),
]   