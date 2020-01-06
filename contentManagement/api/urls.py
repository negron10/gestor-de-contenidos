from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include(('api.user.urls', 'api_user'), namespace='api_user')),
    url(r'^content/', include(('api.content.urls', 'api_content'), namespace='api_content')),
]
