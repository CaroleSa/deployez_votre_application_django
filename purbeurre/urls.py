#! /usr/bin/env python3
# coding: UTF-8

"""purbeurre URL Configuration

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


# imports
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls import url
from food import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mentions_legal/$', views.mentions_legal, name='mentions_legal'),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^food/', include('food.urls', namespace='food')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
