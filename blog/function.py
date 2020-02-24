#from django.http import  HttpResponse
from django.shortcuts import render #传递一个网页给用户

def home(request):
    return render(request,'home.html')

def count(request):
    user_text=request.GET['text']

    word_dict={}
    for word in user_text:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    
    sorted_dict=sorted(word_dict.items(),key=lambda w: w[1],reverse=True)
    

    total_count=len(user_text)
    return render(request,'count.html',{'count':total_count,'text':user_text,'wordict':word_dict,'sorted':sorted_dict})
    #在render中 可以通过字典的方式传递信息给html