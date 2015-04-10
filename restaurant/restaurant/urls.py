from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'core.views.index', name='index'),
    url(r"^logout/$", "core.views.logout", name="logout"),
    url(r"^logout/(.+?)$", "core.views.logout_redirect", name="logout_redirect"),

    url(r'^waiter/$', 'core.views.waiter_index', name="waiter_index"),
    url(r'^waiter/login/$', 'core.views.waiter_login', name="waiter_login"),
    url(r'^waiter/set_status/$', 'core.views.waiter_set_status', name="waiter_set_status"),

    url(r'^kitchen/$', 'core.views.kitchen_index', name="kitchen_index"),
    url(r'^kitchen/login/$', 'core.views.kitchen_login', name="kitchen_login"),
    url(r'^admin/', include(admin.site.urls)),
)
