from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.user import views

router = DefaultRouter()

router.register(r'user', views.UserViewSet, base_name='user')
router.register(r'role', views.RoleViewSet, base_name='role')

urlpatterns = [
    url(r'^', include(router.urls)),
]
