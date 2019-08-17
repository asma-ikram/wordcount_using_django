from django.http import HttpResponse #allows to return HttpResponse
from django.shortcuts import render
import operator

def homepage(request): #the request object checks which URL the user is looking for, cookies etc
    return render(request,'home.html')

def count(request):
    text=request.GET['fulltext']
    wordlist=text.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            #increase the countthewords
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'sentence': text, 'count': len(wordlist),'sortedwords':sortedwords })
