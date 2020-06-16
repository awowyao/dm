from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import *
from .models import *
# Create your views here.
def tesr_Views(request):
    return render(request,'index.html',locals())

def add_Views(request):
    if request.method =='GET':
        return render(request,'index.html',locals())
    else:
        if len(request.POST['username'])>0:
            if len(request.POST['address'])>0 and len(request.POST['address'])<20:
                if len(request.POST['hobby'])>0 and len(request.POST['hobby'])<30:
                    if len(request.POST['massage'])>0 and len(request.POST['massage'])<50:
                        Information.objects.create(username=request.POST['username'],
                                                 enail=request.POST['email'],
                                                 sex=request.POST['sex'],
                                                 address=request.POST['address'],
                                                 hobby=request.POST['hobby'],
                                                 massage=request.POST['massage'],
                                                 )
                        return render(request,'index.html',locals())
                    else:
                        return HttpResponse('留言不能为空，或超50字')
                else:
                    return HttpResponse('兴趣不能为空或超30字')
            else:
                return HttpResponse('地址不能为空或超20字')
        else:
            return HttpResponse('名字不能为空')



def see_Views(request):
    sj = Information.objects.all()
    return render(request, 'massage.html', locals())

def user_Views(request,id):
    cx=Information.objects.get(id=id)
    return render(request, 'user.html', locals())

def detail_Views(request,id):
    cx = Information.objects.get(id=id)
    return render(request, 'detail.html', locals())

def del_Views(request,id):
    ip =0
    pa = 0
    page = 1
    q = int(id)
    #print(q)
    #获取所有id
    ipList = Information.objects.values_list("id")
    #取出id所在的下标并把计算出下标0到id的数据数
    for a,b in enumerate(ipList):
        if b==(q,):
            page+=a
            #print(a)
        #print(b)
    ip = int(page)
    print(ip)
    #计算出删除前的页数
    for x in range(0,ip):
        print(x)
        if x % 5==0:
            pa = pa+ 1
            #print(pa)
            c = str(pa)
            print(c)
            cx = Information.objects.get(id=id)
            html = redirect('/massage/?page='+c)
    if request.method=='GET':
        return HttpResponse('ok')
    else:
        cx = Information.objects.get(id=id)
                #判断是否有COOKIES
                #passwd在COOKIES里
        if 'passwd' in request.COOKIES:
            cx.delete()
            return html
        else:
                    #不在COOKIES
            passwd = request.POST['passwd']
            if passwd =='123456':
                        #加入COOKIES
                        #html.set_cookie('passwd',passwd,60*60*24)
                cx.delete()
                return html
            else:
                return HttpResponse('密码错误')

# def paging_Views(request):
#     user_list = Information.objects.all()
#     paginator = Paginator(user_list, 5)
#     try:
#         page_number = request.GET.get('page','1')
#         # page = Paginator.page(page_number,)
#
#     except (PageNotAnInteger, EmptyPage, InvalidPage):
#         page = paginator.page(1)
#     return render(request, 'massage.html',locals())

def paging_Views(request):
    blogs = Information.objects.all()
    paginator = Paginator(blogs,5)
    page = request.GET.get('page')
    try:
        a = paginator.page(page)
    except PageNotAnInteger:
        a =paginator.page(1)
    except EmptyPage:
        a =paginator.page(paginator.num_pages)
    L=[]
    for x in range(1,paginator.num_pages+1):
        L.append(x)
    #print(L)
    return render(request, 'massage.html', locals())


def adds_Views(request):
        Information.objects.create(username='chen',
                                 enail='123456@qq.con',
                                 sex='男',
                                 address='广州',
                                 hobby=' 打球',
                                 massage='就这',
                                 )
        return HttpResponse('ok')


def tc_Views(request):
    messages.success(request,'hhhhhh')
    return render(request,'tc.html',locals())