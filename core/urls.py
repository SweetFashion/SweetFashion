from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', include('admin_honeypot.urls')),
    path('sweetfashionadmin', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('product.urls', namespace='product')),
    
]
if settings.DEBUG:  # Dev only
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
