from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^random_number/(?P<max_rand>\d+)?/$', views.random_generator, name='number generator'),
]