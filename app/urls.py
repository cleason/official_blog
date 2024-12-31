from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('contact/', views.contact, name='contact'),
    path('post/<int:post_id>/', views.detail, name='detail'),  # Détail d'un article
]