# path_to_fern_flower/urls.py
from django.conf.urls.static import static
from django.urls import path
import views
from path_to_fern_flower import settings
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('game/', views.game, name='game'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)