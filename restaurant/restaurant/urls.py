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
    url(r'^kitchen/items/$', 'core.views.kitchen_items', name="kitchen_items"),
    url(r'^waiter/statistics/$', 'core.views.waiter_statistics', name="waiter_statistics"),
    url(r'^waiter/order_list/$', 'core.views.waiter_order_list', name="waiter_order_list"),
    url(r'^kitchen/ingredients/$', 'core.views.kitchen_ingredients', name="kitchen_ingredients"),
    url(r'^kitchen/login/$', 'core.views.kitchen_login', name="kitchen_login"),
    url(r'^kitchen/claim/$', 'core.views.kitchen_claim', name="kitchen_claim"),
    url(r'^kitchen/ready/$', 'core.views.kitchen_ready', name="kitchen_ready"),

    url(r'^kitchen/items/out/$', 'core.views.menu_item_out', name="menu_item_out"),
    url(r'^kitchen/items/in/$', 'core.views.menu_item_in', name="menu_item_in"),
    url(r'^kitchen/ingredients/out/$', 'core.views.ingredient_out', name="ingredient_out"),
    url(r'^kitchen/ingredients/in/$', 'core.views.ingredient_in', name="ingredient_in"),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^standby/$', 'core.views.standby', name='standby'),
    #url(r'^standby/refill$', 'core.views.refill_request', name="refill_request"),
    #url(r'^standby/help$', 'core.views.help_request', name="help_request"),

    url(r'view_order/(\d+?)/', 'core.views.view_order', name="view_order"),
    url(r'menuitem_details/', 'core.views.menuitem_details', name="menuitem_details"),

    url(r'place_order/$', 'core.views.place_order', name="place_order"),
)
