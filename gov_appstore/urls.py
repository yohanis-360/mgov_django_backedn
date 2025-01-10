"""
URL configuration for gov_appstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('users/', include('users.urls')),  # User management URLs
    path('captcha/', include('captcha.urls')),  # Include the captcha URLs
    path('', home, name='home'),  # Set the home view for the empty path
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('apps/', include('apps.urls')),  # App submission and management URLs
    path('admin_panel/', include('admin_panel.urls')),  # Admin-specific URLs
#     path('notifications/', include('notifications.urls')),  # Notification system URLs
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
