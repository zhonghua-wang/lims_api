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
from core import views as core_views

from lims_api import settings

# rest router
router = routers.DefaultRouter()
router.register('user', core_views.UserViewSet)
router.register('department', instrument_views.DepartmentViewSet)
router.register('manufacturer', instrument_views.ManufacturerViewSet)
router.register('reservation-type', instrument_views.ReservationTypeViewSet)
router.register('instrument', instrument_views.InstrumentViewSet)
router.register('reservation', instrument_views.ReservationViewSet)

# end rest
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
