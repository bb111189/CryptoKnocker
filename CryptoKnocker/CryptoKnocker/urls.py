from django.conf.urls import patterns, include, url

from django.contrib import admin
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
)
