from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CryptoKnocker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include("mainpage.urls")),
    url(r"^login/$", "mainpage.views.login_form"),
    url(r'^management/$', "management.views.index"),
    url(r'^management/login$', "management.views.user_login"),
    url(r'^logout/$', "management.views.user_logout"),
    url(r'^management/registration/$', "management.views.registration"),
    url(r'^management/keys/$', "management.views.manageKeys"),
    url(r'^management/keys/changeKey$', "management.views.changeKey"),
    url(r'^management/getPorts/$', "management.views.getPorts"),
    url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

)
