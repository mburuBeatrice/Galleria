from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.start,name='start'),
    url(r'^search/', views.search_results, name='search_results'),
     url(r'^searchloc/', views.search_location, name='search_location'),
    url(r'^image/(\d+)', views.image_details,name = 'image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)