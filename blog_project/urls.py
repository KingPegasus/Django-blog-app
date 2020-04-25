"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from accounts.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    
	
	#Accounts Views
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/signup/', SignUpView.as_view(), name='signup'),

    #The order of our urls matters here because Django reads this file top-to-bottom.
	#Therefore when we request them /accounts/signup url, Django will first look in auth,
	#not find it, and then proceed to the accounts app.

    #Blog Views
    path('',BlogListView.as_view(), name= 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',  BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/',  BlogDeleteView.as_view(), name='post_delete'),

]
