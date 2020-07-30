from django.contrib import admin
from django.urls import include, path
from home import views

# Django Customization
admin.site.site_header = "Encode Programming"
admin.site.site_title = "Encode Programming"
admin.site.index_title = "Welcome to Dashboard"


urlpatterns = [
    path("", views.home, name='Home'),
    path("about", views.about, name='About'),
    path("contact", views.contact, name='Contact'),
    path("search", views.search, name='Search'),
    path("signup", views.signup, name='SignUp'),
    path("login", views.login, name='Login'),
    path("logout", views.logout, name='Logout'),


]
