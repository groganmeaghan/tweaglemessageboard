from django.urls import path
#from . import views
from .views import HomeView, PostDetailView, LikeView, DeletePostView

urlpatterns = [
    #path('', views.home, name = 'home')
    path('', HomeView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post-detail'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),
]
