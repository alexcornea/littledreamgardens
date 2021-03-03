from . import views
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search/', views.post_search, name='post_search'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.base_gallery, name='/base_gallery'),
    path('', views.contact, name='/contact'),
    path('', views.base, name='base'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),

]