
from django.conf.urls import *
from sogi.views import *

urlpatterns = patterns('',
    (r'^$', main_page),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    (r'^portal/', include('portal.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)

