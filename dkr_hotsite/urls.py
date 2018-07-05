from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns (
    path('i18n/', include('django.conf.urls.i18n')),
    path('',include('website.urls')),
)
