from django.conf.urls import url, include

urlpatterns = [
    url(r'^person/', include(('api.person.urls', 'api_person'), namespace='api_person')),
    url(r'^content/', include(('api.content.urls', 'api_content'), namespace='api_content')),
]
