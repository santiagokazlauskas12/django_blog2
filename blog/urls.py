from django.urls import path
from blog import views

app_name='blog'

urlpatterns = [
    path("",views.IndexView.as_view(), name="index"),
    path("posts",views.PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>",views.PostDetailView.as_view(), name="post_detail"),
    path("posts/create",views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update",views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete",views.PostDeleteView.as_view(), name="post_delete"),
    path("posts/drafts",views.PostDraftsView.as_view(), name="post_drafts"),
    path("posts/<int:pk>/publish",views.post_publish, name="post_publish"),
    path("posts/<int:pk>/leave_comment",views.post_publish, name="post_comment"),
    path("posts/<int:pk>/create_comment",views.add_comment_to_post, name="create_comment"),
    path("posts/<int:pk>/publish_comment",views.aprove_comment, name="aprove_comment"),
    path("posts/<int:pk>/delete_comment",views.delete_comment, name="delete_comment"),
    
]
