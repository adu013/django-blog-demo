from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from articles.views import articleListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articleListView, name='home'),
    path('articles/',  include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
