from django.shortcuts import render, get_object_or_404

# Create your views here.
from news.models import News


def list_news(request):
    news = News.objects.all()
    return render(request, 'news/list_news.html',{'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request,'news/news_details.html',{'news': news})