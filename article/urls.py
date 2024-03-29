from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path("addarticle/", views.addArticle, name='addarticle'),
    path("article/<int:id>", views.detail, name='detail')
]
