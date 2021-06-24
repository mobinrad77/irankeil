from django.conf.urls import url
from aboutus import views

urlpatterns = [
    url(r'^$', views.AboutusPageView.as_view(), name='aboutus'),
]