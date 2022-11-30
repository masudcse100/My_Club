from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('blog/', include('Blog.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "My Club Administrator"
admin.site.site_title = "My Club"
# admin.site.index_title = "Welcome To Admin Area"
admin.site.index_title = ""