from django.conf.urls import url
from keil import views

urlpatterns = [
    url(r'^$', views.KeilPageView.as_view(), name='keil'),
    # url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    # url(r'^data/$', views.DataPageView.as_view(), name='data'),
]