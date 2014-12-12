from django.conf.urls import patterns, include, url
from django.contrib import admin
from Orders import views

urlpatterns = patterns('',
    url(r'^', include('Orders.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
