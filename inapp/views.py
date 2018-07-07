from django.shortcuts import render
from django.utils import timezone
from .models import Post
from newsapi import NewsApiClient

NEWS_API_TOKEN = 'ad8ad995f5ae4d30aaeaf323902f265c'
##mytoken

# Create your views here.
def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'inapp/post_list.html', {'posts': posts})

def latest_news(request):
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
       
        all_articles = newsapi.get_everything(sources='bbc-news,the-verge,cnn',language='en',
        from_parameter=str(timezone.now()-timezone.timedelta(days=1)),to=str(timezone.now()))
        
        news_status = all_articles['status']
        news_count = all_articles['totalResults']
        news_list = all_articles['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        return render(request, 'inapp/latest_news.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})

def sports_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        sources = newsapi.get_sources()
        top_headlines = newsapi.get_top_headlines(category='sports',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/sports.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})

def business_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='business',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/business.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def entertainment_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='entertainment',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/entertainment.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def general_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='general',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/general.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def health_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='health',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/health.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def science_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='science',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/science.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def technology_news(request):
        #logger.log("Entered sports news")
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(category='technology',language='en',country='in',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        #logger.log("Rendering sports news")
        return render(request, 'inapp/technology.html', {'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
def search_news(request):        
    if request.method == 'POST':      
        query_str =  request.POST['search']
        newsapi = NewsApiClient(api_key=NEWS_API_TOKEN)
        top_headlines = newsapi.get_top_headlines(q = query_str,language='en',)
        news_status = top_headlines['status']
        news_count = top_headlines['totalResults']
        news_list = top_headlines['articles']
        for i in range(len(news_list)):
                news_list[i]['publishedAt'] = news_list[i]['publishedAt'][:10]+' at '+news_list[i]['publishedAt'][12:-1]
        return render(request, 'inapp/search.html', {'query_str':query_str, 'news_list':news_list, 'news_count':news_count, 'news_status':news_status})
    else:
        return render(request,"inapp/search.html",{})
