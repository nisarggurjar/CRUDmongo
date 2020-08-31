from django.urls import path
from .views import getArticles, getArticleDetail

urlpatterns = [
    path('', getArticles),
    path('getArticleDetail/<str:AId>/', getArticleDetail),
    
]