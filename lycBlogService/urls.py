"""lycBlogService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
# from rest_framework.authtoken import views

urlpatterns = [
    # Django 后台管理
    path('admin/', admin.site.urls),

    # Django REST Framework
    # path('api/login/', views.obtain_auth_token),
    path('api/auth/', include('account.urls')),
    path('api/docs/', include_docs_urls(title='DRF文档')),
    path('api/user/', include('user.urls')),
    path('api/article/', include('article.urls')),
    path('api/comment/', include('commentary.urls')),
]
