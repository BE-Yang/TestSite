from django.conf.urls import url
from . import views

app_name='BG'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'submit/', views.SubmitView.as_view(), name='submit'),
]