
from django.conf.urls import url
from .views import like

urlpatterns = [
    url(r'^like/(?P<content_type>[\w-]+)/(?P<id>\d+)/(?P<vote>-?\d+)$', like, name='like'),
]
