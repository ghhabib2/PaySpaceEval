"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.template.loader import render_to_string
from .routes import user_routes, address_routes, transaction_routes


user_endpoints = DefaultRouter()

for route in user_routes:
    user_endpoints.register(route['regex'], route['viewset'], basename=route['basename'])

address_endpoints = DefaultRouter()

for route in address_routes:
    address_endpoints.register(route['regex'], route['viewset'], basename=route['basename'])

transactions_endpoints = DefaultRouter()

for route in transaction_routes:
    transactions_endpoints.register(route['regex'], route['viewset'], basename=route['basename'])

schema_view = get_schema_view(
    openapi.Info(
        title="Pay Space Endpoints",
        default_version='v1',
        description=render_to_string('swagger/introduction.md'),
        terms_of_service="https://ghhabib.me/",
        contact=openapi.Contact(email="ghhabib2@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.AppPages.login, name='login'),
    path('sign-up', views.AppPages.sign_up, name='sign-up'),
    path('home', views.AppPages.home, name='home'),
    path('addresses', views.AppPages.addresses, name='addresses'),
    path('inner_outer_transaction', views.AppPages.inner_outer_transaction, name='Transaction'),
    path('inner_inner_transaction', views.AppPages.inner_inner_transaction, name='Inner Transaction'),
    path('addressdetails', views.AppPages.address_details, name='addressDetails'),
    path('address_search_details', views.AppPages.address_search_details, name='addressDetails'),
    path('api/v1/users/', include(user_endpoints.urls)),
    path('api/v1/adr/', include(address_endpoints.urls)),
    path('api/v1/txs/', include(transactions_endpoints.urls)),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)