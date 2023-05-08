from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from documentManagement.views import DocumentApi
from propertyManagement.views import PersonApi, PropertyApi

router = routers.DefaultRouter()
router.register(r'documents', DocumentApi, 'documents')
router.register(r'persons', PersonApi, 'persons')
router.register(r'properties', PropertyApi, 'properties')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include('authentification.urls')),
    path('api/', include(router.urls)),
]
