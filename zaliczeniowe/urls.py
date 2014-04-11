from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zaliczeniowe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'rooms.views.main', name='main'),
    url(r'^login$', 'rooms.views.login_', name='login'),
    url(r'^logout$', 'rooms.views.logout_', name='logout'),
    url(r'^room_list', 'rooms.views.room_list', name='room_list'),
    url(r'^room_list', 'rooms.views.room_list', name='search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^booking', 'rooms.views.booking', name='booking'),
    url(r'^final_decision', 'rooms.views.final_decision', name='final_decision'),
    url(r'^actual_booking', 'rooms.views.actual_booking', name='actual_booking'),
    
)
