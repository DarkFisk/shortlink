from django.conf.urls import patterns, url

from apps.tracking.views import LinkCreateView, LinkDetailView, LinkListView


urlpatterns = patterns(
    '',
    url(r'create/$', LinkCreateView.as_view(), name='create'),
    url(r'list/$', LinkListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w]+)/$', LinkDetailView.as_view(), name='detail'),
)
