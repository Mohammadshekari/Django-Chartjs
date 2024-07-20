"""
URL configuration for DjangoChartJs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from DjangoChartJs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('api/sample-bar-data', SampleBarDataView.as_view()),
    path('api/sample-line-data', SampleLineDataView.as_view()),
    path('api/sample-doughnut-data', SampleDoughnutDataView.as_view()),
    path('api/sample-pie-data', SamplePieDataView.as_view()),
    path('api/sample-radar-data', SampleRadarDataView.as_view()),
]
