"""
URL configuration for notspam project.

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
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

# from servers import views as server_views
from dashboard_app import views as dashboard_views

urlpatterns = [
    path('', dashboard_views.home, name='home'),
    path('', include('authentication.urls'), name='login'),
    path('servers/', include('servers.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)