from django.conf.urls import patterns, url

from Orders import views

urlpatterns = patterns('',
    # url(r'^$', views.Home.as_view(), name='home'),
    url(r'^$', views.first, name='home'),
    url(r'^uploads/', views.upload, name='upload'),
    url(r'^auth/', views.auth, name='upload'),
    url(r'^add_songs/', views.add_songs, name='upload'),
    url(r'^admin/', views.admin_line, name='upload'),
    url(r'^artists/', views.artists, name='upload'),
    url(r'^logout/', views.log_out, name='upload'),
    url(r'^next_song/', views.next_song, name='upload'),
    url(r'^order(?P<id>\d+)/$', views.add_order),
    url(r'^page(?P<page>\d+)/$', views.home),
    url(r'^artist(?P<id>\d+)/$', views.artist_list),
    url(r'^admin_del(?P<id>\d+)/$', views.admin_del),
    url(r'^pull_list/', views.pull_list, name='upload'),
    url(r'^pull_list_dark/', views.pull_list_dark, name='upload'),
)

