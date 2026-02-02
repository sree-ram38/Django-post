from django.urls import path
from .import views

app_name = 'myapp'

urlpatterns = [
    path('',views.index, name="Index"),
    path('detail/<str:slug>', views.detail, name="Detail"),
    # path('detail/', views.detail, name="Detail"),
    path('new_something_url',views.new_url_view, name='new_url'),
    path('old_url',views.old_url_redirect, name='old_url'),
    path('newhtml/', views.new, name="New"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
]