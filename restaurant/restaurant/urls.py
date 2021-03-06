from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'core.views.index', name='index'),

    url(r'^waiter/$', 'core.views.waiter_index', name="waiter_index"),
    url(r'^waiter/login/$', 'core.views.waiter_login', name="waiter_login"),
    url(r'^admin/', include(admin.site.urls)),
)
