from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.hadu, name='hadu'),
    path('<int:song_id>/', views.detail, name='detail'),
]

