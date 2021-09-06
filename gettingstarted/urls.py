from django.urls import path, include
from rest_framework import routers
from gettingstarted.start import views

from django.contrib import admin

admin.autodiscover()

import hello.views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
