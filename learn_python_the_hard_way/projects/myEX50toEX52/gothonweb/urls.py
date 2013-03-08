from django.conf.urls import patterns, url
from gothonweb import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^hello/', views.hello, name='hello'),
    url(r'^game/', views.game, name='gameengine'),                   
)
