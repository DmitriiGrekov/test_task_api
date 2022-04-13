from django.urls import path
from .views import api_post, api_post_detail, api_comment_add


urlpatterns = [
        path("api/posts/", api_post),
        path('api/post/<int:pk>/', api_post_detail),
        path('api/comments/add/<int:post_pk>/', api_comment_add),
        ]
