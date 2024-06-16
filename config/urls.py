from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.api.v1.views import EmployeeViewSet, SubscriptionViewSet, UserViewSet

from .yasg import urlpatterns as doc_urls

router = DefaultRouter()
router.register(r"api/v1/users", UserViewSet, basename="users")
router.register(r"api/v1/employees", EmployeeViewSet, basename="employees")
router.register(r"api/v1/subscriptions", SubscriptionViewSet, basename="subscriptions")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
