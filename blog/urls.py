from django.urls import path 
from . import views

urlpatterns = [
    path('creer/', views.create_article, name="create_article"),
    path('', views.page_acceuil, name="page_acceuil"),
    path('articles/<int:id>/', views.afficher_article, name="afficher_article")
]
