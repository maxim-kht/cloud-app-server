"""cloud_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from custom_messages import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'messages/$', views.MessageListView.as_view(),
            name='messages'),
        url(r'gallery/$', views.GalleryView.as_view(),
            name='gallery'),
        url(r'json-placeholder/$', views.JsonPlaceholderView.as_view(),
            name='json_placeholder'),
    ]))
]
