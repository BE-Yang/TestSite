from django.conf.urls import url
from . import views

app_name = 'BG'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'submit/', views.SubmitView.as_view(), name = 'submit'),
    url(r'^(?P<Model>\w+)/$', views.DrinkView, name = 'ListOfDrinks'),
    url(r'^(?P<Model>[\w\s]+)/(?P<Drink>[\w\s]+)$', views.DetailView.as_view(), name = 'Detail'),
    url(r'^about$', views.AboutView, name = 'About'),
]