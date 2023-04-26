from rest_framework import routers
from api.views import PostViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet, basename='posts')
urlpatterns = router.urls