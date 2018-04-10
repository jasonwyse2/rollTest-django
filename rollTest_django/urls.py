"""rollTest_django URL Configuration

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
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url

from . import view
from models import intraday_minute

urlpatterns = [
    url(r'^intraday$', view.intraday_area),
    url(r'^dynamic$', view.dynamic_update),
    url(r'^intraday_minute$', view.intraday_minute),
    url(r'^intraday_area/$', view.intraday_area, name='intraday_area'),
    url(r'^minute$', view.minute),
    url(r'^IntradayMinutePrediction/$', view.IntradayMinutePrediction, name='IntradayMinutePrediction'),
    url(r'^InterdayTrendPrediction/$', view.InterdayTrendPrediction, name='InterdayTrendPrediction'),
    url(r'^IntradayModelName/$', view.IntradayModelName, name='IntradayModelName'),
    url(r'^InterdayModelName/$', view.InterdayModelName, name='InterdayModelName'),

    url(r'^interday_trend/$', view.interday_trend, name='interday_trend'),
]

urlpatterns += staticfiles_urlpatterns()