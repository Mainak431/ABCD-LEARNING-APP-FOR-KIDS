from django.conf.urls import url

from . import views
from .views import *
import django.contrib.auth.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('^$', views.home, name='home'),
                  url(r'^letter/(?P<pk>\d+)/$', views.letter, name="letter"),
                  url(r'check/(?P<pk>\d+)/(?P<pkl>\d+)/(?P<ind>\d+)$',views.check,name="check"),
                  url(r'redirect/(?P<pk>\d+)/$', views.redirect, name="redirect"),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
