from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about$', views.about_page, name='about'),
    url(r'^blog$', views.blog_page, name='blog'),
    url(r'^thanks$', views.thanks_page, name='thanks'),
    url(r'^questions$', views.QuestionView.as_view(), name='questions'),
    url(r'^contacts$', views.contacts_page, name='contacts'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]