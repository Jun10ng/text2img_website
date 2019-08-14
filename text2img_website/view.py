from django.shortcuts import render
from tool.translate import translate

def text(request):
    if request.method == 'GET':
        return render(request,'text.html')
    elif request.method=='POST':
        text = request.POST['text']
        text_en = translate(text)
        # 单用户操作
        with open('text/text_en.txt','w') as f:
            f.write(text_en)
        return render(request,"showimg.html",{"text":text})

def img(request):
    context = {"text":' '}
    return render(request, 'showimg.html',context)