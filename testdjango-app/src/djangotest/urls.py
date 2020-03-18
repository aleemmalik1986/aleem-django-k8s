from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from quickstart.views import UserViewSet, GroupViewSet, frontend

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

	path('', frontend, name='frontend'),
    path('products/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
