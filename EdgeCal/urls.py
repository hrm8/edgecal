from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'EdgeCal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^EdgeCalApp/', include('EdgeCalApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]