from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from documentManagement.views import DocumentApi
from propertyManagement.views import PersonApi, PropertyApi
from warhouse.views import ProductApi, AllProductstApi, AutoIncrementApi
from property.views import *

router = routers.DefaultRouter()
router.register(r'documents', DocumentApi, 'documents')
router.register(r'persons', PersonApi, 'persons')
router.register(r'properties', PropertyApi, 'properties')
router.register(r'product', ProductApi, 'product')
router.register(r'allproducts', AllProductstApi, 'allproducts')
router.register(r'autoIncrement', AutoIncrementApi, 'autoIncrement')
router.register(r'autoincrement101', AutoIncrement101Api, 'autoincrement101')
router.register(r'autoincrement102', AutoIncrement102Api, 'autoincrement102')
router.register(r'autoincrement103', AutoIncrement103Api, 'autoincrement103')
router.register(r'autoincrement104', AutoIncrement104Api, 'autoincrement104')
router.register(r'autoincrement105', AutoIncrement105Api, 'autoincrement105')
router.register(r'autoincrement106', AutoIncrement106Api, 'autoincrement106')
router.register(r'autoincrement107', AutoIncrement107Api, 'autoincrement107')


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
