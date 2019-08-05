from django.shortcuts import render

def text(request):
    if request.method == 'GET':
        return render(request,'text.html')
    elif request.method=='POST':
        text = request.POST['text']
        return render(request,"showimg.html",{"text":text})

def img(request):
    context = {"text":' '}
    return render(request, 'showimg.html',context)