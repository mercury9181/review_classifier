from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render_to_response

from textblob import TextBlob
import nltk

def allblogs(request):
    blogs =Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def rc(request):
    good_count=0
    bad_count=0
    location_count=0
    blogs =Blog.objects.all()
    good=dict()
    bad=dict()
    total_location=dict()
    for blog in blogs:
        if blog.location not in total_location.values():

                 total_location[location_count]=blog.location
                 location_count=location_count+1
        decision = TextBlob(blog.body)
        c = format(decision.sentiment.polarity)
        if float(c) < 0.1:
            bad_count=bad_count+1
            bad[bad_count]=blog

        else:
            good[good_count]=blog
            good_count=good_count+1

        # print(c)
        # print (blog.title)
    # print(good)
    return render(request, 'blog/rc.html',{'blogs':blogs,'good':good,'bad':bad,'total_location':total_location,'search_place':'All place'})


def search(request):
   if request.method=='POST':
                search_indication=1
                search_place=request.POST['search']
                good_count=0
                bad_count=0
                location_count=0
                blogs =Blog.objects.all()
                good=dict()
                bad=dict()
                total_location=dict()
                for blog in blogs:
                   if blog.location not in total_location.values():
                          total_location[location_count]=blog.location
                          location_count=location_count+1

                   if blog.location==search_place:
                           print(blog.location)
                           decision = TextBlob(blog.body)
                           c = format(decision.sentiment.polarity)
                           if float(c) < 0.1:
                               bad_count=bad_count+1
                               bad[bad_count]=blog

                           else:
                               good[good_count]=blog
                               good_count=good_count+1

                    # print(c)
                    # print (blog.title)
                # print(good)
                return render(request, 'blog/rc.html',{'blogs':blogs,'good':good,'bad':bad,'search_indication':search_indication,'total_location':total_location,'search_place':search_place})




def detail(request,blog_id):
   detail_blog = get_object_or_404(Blog, pk= blog_id)
   return render(request, 'blog/detail.html',{'blog':detail_blog})

@login_required
def givereview(request):
           # print("form is working")
        if request.method == 'POST':
            if request.POST['title'] and request.POST['rating'] and request.POST['location'] and request.POST['body'] and request.FILES['image']:
                  blog = Blog()
                  blog.title=request.POST['title']
                  blog.rating=request.POST['rating']
                  blog.location=request.POST['location']
                  blog.pub_date=timezone.datetime.now()
                  blog.body=request.POST['body']
                  blog.image=request.FILES['image']
                  blog.save()
                  return redirect('givereview')
            else:
                  return render(request, 'blog/givereview.html',{'error':'all field must be fulfilled!!'})
        else:
           return render(request, 'blog/givereview.html')
