from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.content import views

router = DefaultRouter()

router.register(r'category', views.CategoryViewSet, base_name='category')
router.register(r'content', views.ContentViewSet, base_name='content')
router.register(r'comment', views.CommentViewSet, base_name='comment')
router.register(r'file', views.FileViewSet, base_name='file')

urlpatterns = [
    url(r'^', include(router.urls)),
]
