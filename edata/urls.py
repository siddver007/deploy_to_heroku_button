from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^', include('edapp.urls',namespace='edapp')),
    url(r'^admin/', include(admin.site.urls)),
]
