from django.conf.urls import patterns, url

from apps.homepage.views import MainPage


urlpatterns = patterns(
    '',
    url(r'^$', MainPage.as_view(), name='main'),
)
