from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
def hello(request):
    return HttpResponse ("<h1>Я тебя люблю</h1>")
# Create your views here.
def world(request):
    response = {"name": "Kirill", "d":34, "arr": [1, 2, 3, 4]}
    response["content"] = Video.objects.all()
    return render(request, "index.html", response)

def accept_comment(request, id):
    Comment.objects.create(text=request.POST["com"], comment_video_id=id)
    return HttpResponse(Video.comment)

def one_video(request, id):
    response = {"video":Video.objects.get(id=id)}
    return render(request, "one_video.html", response)

def add_like(request, id):
    video = Video.objects.get(id=id)
    video.likes+=1
    video.save()
    return redirect("main_page")

def ajax_like(request):
    id = request.GET["id"]
    video = Video.objects.get(id=id)
    video.likes += 1
    video.save()
    return HttpResponse(video.likes)

# def ajax_comment_add(request):
#     Comment.objects.create(text=request.POST["com"], comment_video_id=id)
#     return HttpResponse(video.comment.all)
