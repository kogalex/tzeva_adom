from django.conf.urls import patterns, url, include
from rest_framework import routers
from tzevaadom import views

router = routers.DefaultRouter()
router.register(r'alarms', views.AlarmViewSet)
router.register(r'areas', views.AreaViewSet)
router.register(r'cities', views.CityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)