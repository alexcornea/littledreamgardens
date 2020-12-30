from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import core.views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', core.views.home, name='home'),
    path('', core.views.base, name='base'),
    path('post_detail', core.views.post_detail, name='post_detail'),
    path('base_gallery', core.views.base_gallery, name='base_gallery'),
    path('contact', core.views.contact, name='contact'),
    path('category/<category>/', core.views.CatListView.as_view(), name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
