from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.maps_page, name='index'),
    # url(r'^$', views.IndexView.as_view(), name='index')
]