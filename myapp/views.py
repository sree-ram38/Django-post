from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import  posts, Contact
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World")
# def detail(request, post_id):
#     return HttpResponse(f"You are viewing post detail page and the post id is {post_id}")

# static data for testing
# post = [
#     {'id': 1, 'title':'post 1', 'content':'content of post 1'},
#     {'id': 2, 'title':'post 2', 'content':'content of post 2'},
#     {'id': 3, 'title':'post 3', 'content':'content of post 3'},
#     {'id': 4, 'title':'post 4', 'content':'content of post 4'},
#     {'id': 5, 'title':'post 5', 'content':'content of post 5'},
#     {'id': 6, 'title':'post 6', 'content':'content of post 6'},
#     {'id': 7, 'title':'post 7', 'content':'content of post 7'},
#     {'id': 8, 'title':'post 8', 'content':'content of post 8'},
#     {'id': 9, 'title':'post 9', 'content':'content of post 9'},
# ]

def index(request):
    myapp_title = "--LIST OF POST--"
    # getting data from post model
    all_post = posts.objects.all()

    # paginator
    paginator = Paginator(all_post, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request,'index.html', {'myapp_title':myapp_title, 'page_object':page_object})

def detail(request, slug):  #the parameter should be same as from the path(url)
    detail_title = 'Detail'
    # static data for testing
    # post_item = next((item for item in posts if item['id'] == int(post_id)), None)
    try:
        post_item = posts.objects.get(slug=slug)
        related_posts = posts.objects.filter(category=post_item.category).exclude(pk=post_item.id)
    except posts.DoesNotExist:
        raise Http404("post does not exist")
    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable is {post_item}')
    return render(request,'detail.html', {'posts':post_item, 'related_posts':related_posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        success = True
    return render(request, 'contact.html', {'success': success})

def old_url_redirect(request):
    return redirect(reverse('myapp:new_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

def new(request):
    return render(request,'new.html')