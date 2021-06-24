from django.conf.urls import url
from article import views


urlpatterns = [
    url(r'^$', views.ArticlePageView.as_view(), name='article'),
    url(r'^first$', views.FirstArticlePageView.as_view(), name='first'),
    url(r'^second$', views.SecondArticlePageView.as_view(), name='second'),
    url(r'^third$', views.ThirdArticlePageView.as_view(), name='third'),
    url(r'^forth$', views.ForthArticlePageView.as_view(), name='forth'),
    url(r'^fifth$', views.FifthArticlePageView.as_view(), name='fifth'),
]