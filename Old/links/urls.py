from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.links_page, name='index'),

]