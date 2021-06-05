from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pinwin.urls')),
    url(r'^files/', include('db_file_storage.urls')),
]