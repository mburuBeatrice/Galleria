from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.start,name='start'),
    url(r'^search/', views.search_results, name='search_results')
]