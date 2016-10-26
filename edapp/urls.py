from django.conf.urls import include, url
from edapp.views import *

urlpatterns = [
    
    url(r'^time/$', getServerHitTime , name = 'serverHitTime'),
    url(r'^upload/$', csvProcessView , name = 'csvProcess'),
]