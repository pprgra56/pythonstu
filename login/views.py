from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render

def my_render(request,template_path,context_dict={}):
    t = loader.get_template(template_path)
    context = RequestContext(request,context_dict)
    res_html = t.render()
    return HttpResponse(res_html)


def index(request):

    # return my_render(request,"booktest/index.html",{'id':'12'})
    return render(request,"booktest/index.h tml",{"context":"hello word"})
