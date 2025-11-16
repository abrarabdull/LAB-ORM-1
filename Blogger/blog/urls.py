from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/", views.add_post, name="add_post"),
    path("manage/", views.manage_posts, name="manage_posts"),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path("post/<int:post_id>/", views.post_detail_view, name="post_detail"),
]