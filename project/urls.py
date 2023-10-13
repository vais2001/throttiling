from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls.conf import  path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from throttilingapp.views import StudentViewSet

router = DefaultRouter()
router.register("studentapi",StudentViewSet, basename="student")


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='restframework'))
                     
]