from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('example.urls')),
    url(r'^keil/', include('keil.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^article/', include('article.urls')),
]
