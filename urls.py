from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Assuming views.home exists
    # path('game/', views.game, name='game'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]

from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Assuming views.home exists
    # path('game/', views.game, name='game'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]