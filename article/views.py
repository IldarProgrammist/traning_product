from django.shortcuts import render, get_object_or_404
from .models import Article

def list_article(request):
    article = Article.objects.all()
    return render(request, '../templates/article/list_article.html', {'article': article})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, '../templates/article/article_details.html', {'article': article})