from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
