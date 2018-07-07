from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.latest_news, name = 'latest_news'),
    url(r'^sports/$', views.sports_news, name = 'sports_news'),
    url(r'^business/$', views.business_news, name = 'business_news'),
    url(r'^entertainment/$', views.entertainment_news, name = 'entertainment_news'),
    url(r'^health/$', views.health_news, name = 'health_news'),
    url(r'^technology/$', views.technology_news, name = 'technology_news'),
    url(r'^general/$', views.general_news, name = 'general_news'),
    url(r'^science/$', views.science_news, name = 'science_news'),
    url(r'^search/$', views.search_news, name = 'search_news'),
]
