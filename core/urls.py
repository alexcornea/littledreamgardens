from . import views
from django.urls import path


app_name = 'core'
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.base_gallery, name='/base_gallery'),
    path('', views.contact, name='/contact'),
    path('', views.base, name='base'),
]