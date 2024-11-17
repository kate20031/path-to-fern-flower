<<<<<<< HEAD
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
=======
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
>>>>>>> 1dd51f0b6274b73d1e89e4fd1eaf8c5ff42a6ebf
