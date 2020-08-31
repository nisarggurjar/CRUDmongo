from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from bson import ObjectId 
 
@csrf_exempt
def getArticles(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def getArticleDetail(request, articleId):
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(_id=ObjectId(articleId))
        print('working')
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        print('get')
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
 
    elif request.method == 'PUT':
        print('put')
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP)
 
    elif request.method == 'DELETE':
        article.delete()
        print('delete')
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)