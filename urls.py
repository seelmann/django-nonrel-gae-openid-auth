from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^accounts/', include('django_openid_auth.urls')),
    (r'^accounts/logout', 'django.contrib.auth.views.logout', {'template_name': 'home.html', 'next_page': '/'}),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
