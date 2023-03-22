from django.urls import path
from . import views
from .views import HomeView, PostDetail, AboutView, AddPostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetail.as_view(), name="post-detail"),
    path('about', AboutView.as_view(), name="about"),
    path('add_post/', AddPostView.as_view(), name="add_post")
]
