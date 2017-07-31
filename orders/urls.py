from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^menu/$', views.categories_list),
    url(r'^dishes/$', views.dishes_list),
]
