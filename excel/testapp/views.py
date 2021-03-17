from django.core.paginator import Paginator
from django.shortcuts import render
from testapp.models import *
# Create your views here.
def display_bank(request):
    return render(request,'testapp/index.html')

def abhyudayabank(request):
    item = abhyudaya.objects.all()
    paginator = Paginator(item,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    d = {'item':item,'page_obj':page_obj}
    return render(request,'testapp/abhyudaya.html',context=d)

def ahmedabadbank(request):
    item = ahmedabad.objects.all()
    paginator = Paginator(item,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dic = {'item':item,'page_obj':page_obj}
    return render(request,'testapp/ahmedabad.html',context=dic)
