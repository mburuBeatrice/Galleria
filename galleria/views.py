from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def start(request):
    pictures = Image.objects.all()

    return render(request,'start.html',{"pictures":pictures})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term) 

        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images":searched_images}) 
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 

def search_location(request):
    if 'image' in request.GET and request.GET["image"]:
        search = request.GET.get("image")
        searched_images = Image.search_by_location(search) 

        message = f"{search}"

        return render(request, 'search.html', {"message":message,"images":searched_images}) 
    else:
        message = "You haven't searched for any term"
        return render(request, 'location.html',{"message":message}) 
def image_details(request,image_id):

    try:
        imagey = Image.objects.get(id = image_id)

    except DoesNotExist:
        raise Http404()
    
    return render(request, "image_deets.html", {"imagey":imagey})
