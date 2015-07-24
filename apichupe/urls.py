from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api

from app.resources import CategoryResource

v1_api = Api('v1')

v1_api.register(CategoryResource())


urlpatterns = [
    # Examples:
    # url(r'^$', 'apichupe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(v1_api.urls)),
]
