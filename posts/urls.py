from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('<int:post_id>/', views.index, name='index'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('tweetLikeAdd/<int:post_id>/',
         views.tweetLikeAdd, name='tweetLikeAdd'),
    path('tweetLikeSubtract/<int:post_id>/',
         views.tweetLikeSubtract, name='tweetLikeSubtract'),
]
