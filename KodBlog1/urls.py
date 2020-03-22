from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "KodAdmin"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to KodAdmin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]