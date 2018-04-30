from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^random_number/$', views.random_generator, {'max_rand':100}, name='number generator default'),
    url(r'^random_number/(?P<max_rand>\d+)/$', views.random_generator, name='number generator max given'),
]