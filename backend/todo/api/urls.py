from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router=DefaultRouter()
router.register("todo",TodoViewSet,basename='all-todos')

urlpatterns = []
urlpatterns+=router.urls