from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
# Create your views here.
from booktest.models import BookInfo

def my_render(requst,template_path,context_dict={}):
    temp = loader.get_template(template_path)
    # context = RequestContext(requst,{})
    context = context_dict
    var_html = temp.render(context)
    return HttpResponse(var_html)

def books(requst):
    #处理M和T
    booklist = BookInfo.objects.all()
    temp = loader.get_template('booktest/index.html')
    # context = {'booklist': booklist}
    for i in booklist:
        print("图书标题",i.btitle)
    context={"books":booklist}
    return render(requst,'booktest/show_books.html',context)

def detail(requst,id):
    book =BookInfo.objects.get(id=id)
    heros = book.heroinfo_set.all()
    context={'book':book,"heros":heros}
    return render(requst, 'booktest/detail.html', context)