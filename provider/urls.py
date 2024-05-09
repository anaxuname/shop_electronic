from rest_framework.routers import DefaultRouter

from .views import ProviderViewSet

router = DefaultRouter()
app_name = "provider"

router.register(r"", ProviderViewSet, basename="provider")
urlpatterns = router.urls
