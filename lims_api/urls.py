"""lims_api URL Configuration

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
from django.conf.urls.static import static
from rest_framework import routers
from instrument import views as instrument_views

from lims_api import settings

# rest router
router = routers.DefaultRouter()
router.register('users', instrument_views.UserViewSet)
router.register('departments', instrument_views.DepartmentViewSet)
router.register('manufacturers', instrument_views.ManufacturerViewSet)
router.register('reservation-types', instrument_views.ReservationTypeViewSet)
router.register('instruments', instrument_views.InstrumentViewSet)
router.register('reservations', instrument_views.ReservationViewSet)

# end rest
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^statistic/instrument/', instrument_views.InstrumentReservationStatistic.as_view()),
    url(r'^api/auth/', include('djoser.urls.authtoken')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
