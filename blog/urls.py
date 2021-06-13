#what takes us to our where we need to go when we pass the command in our browser
from django.urls import path
from . import views
#for more details on our posts from views.py
from .views import (
    PostListView,
    #PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    like_post,
    share_post,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('likes/post/<int:pk>', like_post, name='like'),
    path('shares/post/<int:pk>', share_post, name='shares'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/detail',views.getpostdetail, name='post-detail'),
]
