from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
def blogpost(request):
    return render(request, 'blog/blogpost.html')
def makeblog(request):
    if  request.method == 'POST':
        name = request.POST.get('name', '')
        title = request.POST.get('title', '')
        heading0 = request.POST.get('main_heading', '')
        cheading0 = request.POST.get('cmain_heading', '')
        heading1 = request.POST.get('heading2', '')
        cheading1 = request.POST.get('c_heading2', '')
        sub_heading = request.POST.get('sub_heading', '')
        csub_heading = request.POST.get('c_sub_heading', '')
        print(name, title, heading0, cheading0, heading1, cheading1, sub_heading, csub_heading)
        blog1 = blogpost(name=name, title=title, heading0=heading0, cheading0=cheading0, heading1=heading1, cheading1=cheading1, sub_heading=sub_heading, csub_heading=csub_heading)
        blog1.save()
    return render(request, 'blog/makeblog.html')
def showblog(request):
    post_blog = blogpost.objects.all()
    print(post_blog)
    return render(request, 'blog2/showblog.html')