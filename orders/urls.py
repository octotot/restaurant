from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menu/$', views.menu_list),
    url(r'^post/$', views.order_post),
]
