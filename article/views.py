from django.shortcuts import render
from django.views.generic import TemplateView

class ArticlePageView(TemplateView):
    template_name = "article.html"

class FirstArticlePageView(TemplateView):
    template_name = "first.html"

class SecondArticlePageView(TemplateView):
    template_name = "second.html"

class ThirdArticlePageView(TemplateView):
    template_name = "third.html"

class ForthArticlePageView(TemplateView):
    template_name = "forth.html"

class FifthArticlePageView(TemplateView):
    template_name = "fifth.html"