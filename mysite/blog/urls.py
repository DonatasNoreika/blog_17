from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
]
