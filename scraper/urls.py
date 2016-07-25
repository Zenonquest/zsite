from django.conf.urls import url, include, patterns
from . import views

app_name = 'scraper'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^voteUp$', views.voteUp, name='voteUp'),
	url(r'^voteDown$', views.voteDown, name='voteDown'),
	url(r'^updateSite$', views.updateSite, name='updateSite'),
	url(r'^api/dailybruin/$', views.dailybruin, name='dailybruin'),
	url(r'^api/csmonitor/$', views.csmonitor, name='csmonitor'),
	url(r'^api/engadget/$', views.engadget, name='engadget'),

]