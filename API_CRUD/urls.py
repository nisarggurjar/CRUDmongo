from django.urls import path
from .views import *

urlpatterns = [
    path('', getArticles, name='getArticles'),
    path('getArticleDetail/<str:articleId>/', getArticleDetail),
    
]