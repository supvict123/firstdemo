from datetime import datetime
from django.shortcuts import render
from .models import Post
import numpy as np
from trips import classifier as clf
# Create your views here.


def hello(request):
    return render(request, 'hello.html',{'current_time': str(datetime.now()),})

def prediction(request):
    name = request.GET['name']
    data = request.GET['message']
    c = clf.classifier()
    pred, prob = c.prediction([str(data)])    
    return render(request, 'prediction.html',{'current_time': str(datetime.now()),'prediction': str(pred),'probablity':str(int(prob)),'review':data,'name':str(name),})

def index(request):
	return render(request, 'index.html', {'current_time': str(datetime.now())})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


