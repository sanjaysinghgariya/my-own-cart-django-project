from django.shortcuts import render
from django.http import HttpResponse
from .models import makeblog
# Create your views here.
def index(request):
    blog_posting = makeblog.objects.all()
    params = {"blog_posting":blog_posting}
    return render(request, 'blog2/showblog.html',{"blog_posting":blog_posting})
def postblog(request):
    if  request.method == 'POST':
        name = request.POST.get('name', '')
        title = request.POST.get('title', '')
        heading0 = request.POST.get('main_heading', '')
        cheading0 = request.POST.get('cmain_heading', '')
        heading1 = request.POST.get('heading2', '')
        cheading1 = request.POST.get('c_heading2', '')
        sub_heading = request.POST.get('sub_heading', '')
        csub_heading = request.POST.get('c_sub_heading', '')
        image = request.POST.get('avatar', '')
        print(image)
        print(name, title, heading0, cheading0, heading1, cheading1, sub_heading, csub_heading)
        blog1 = makeblog(name=name,title=title, heading0=heading0, cheading0=cheading0, heading1=heading1, cheading1=cheading1, sub_heading=sub_heading, csub_heading=csub_heading, image=image)
        blog1.save()
        thank = True
        id = blog1.post_id
        return render(request, 'blog2/blogpost.html' ,{'thank':thank, 'id':id})
    return render(request, 'blog2/blogpost.html')

def showblog(request):
    blog_posting = makeblog.objects.all()
    params = {"blog_posting":blog_posting}
    print(type(params))
    return render(request, 'blog2/showblog.html', {'blog_posting':blog_posting})

def showingblog(request, my_id):
    blog_posting1 = makeblog.objects.filter(post_id=my_id)
    blog_posting0 = []
    blog_posting = makeblog.objects.all()
    length = 3
    for k in blog_posting:
        length +=1
    print(length)
    print({'blog_posting1': [blog_posting1[0], length]})

    return render(request, 'blog2/blogshowing.html', {'blog_posting1':[blog_posting1[0], length]})


def error_handling(request):
    blog_posting = makeblog.objects.all()
    length = 0
    for k in blog_posting:
        length += 1
    print(length)
    return render(request, 'blog2/errorhandling.html')