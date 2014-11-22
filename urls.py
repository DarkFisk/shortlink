from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.tracking.views import RedirectLinkView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'settings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        r'^tracking/',
        include(
            'tracking.urls',
            namespace="tracking",
            app_name="tracking"
        )
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^',
        include(
            'homepage.urls',
            namespace="homepage",
            app_name="homepage"
        )
    ),
    url(r'^(?P<b62_key>[a-zA-Z0-9]+)$', RedirectLinkView.as_view(), name="redirect_link"),
)
