import json

from django.core import serializers
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def dm_Views(request,id=0):
    #分类
    an_class=['冒险','日常','后宫']
    if request.method =='GET':
        # cx = Anima.objects.all()
        # #排序
        # if 'sort' in request.GET:
        #     if request.GET['sort'] == '时间':
        #         cx = Anima.objects.order_by('-time')
        #     else:
        #         cx = Anima.objects.order_by('name')
        # if 'user' in request.session:
        #     user = request.session['user']
        #     u_user = m_user.objects.get(user=request.session['user'])
        #     number = len(u_user.anime.all())
            return render(request, 'dm.html', locals())
    #     else:
    #         return render(request, 'dm.html', locals())
    # else:
    #     pass

def dm_sort_Views(request):
    """排序"""
    if 'sort' in request.GET:
        print(request.GET['sort'])
        if request.GET['sort'] == '2':
            dm_sort =Anima.objects.order_by('-time')
            js_sort=serializers.serialize('json',dm_sort)
            dic = {
                'dm_sort':js_sort,
            }
            return HttpResponse(json.dumps(dic))
        else:
            dm_sort = Anima.objects.order_by('name')
            js_sort=serializers.serialize('json',dm_sort)
            dic = {
                'dm_sort':js_sort,
            }
            return HttpResponse(json.dumps(dic))

def dm_search_Views(request):
    pass

def register_Views(request):
        if request.method == 'GET':
            return render(request,'register.html')
        else:
            m_user.objects.create(user=request.POST['user_name'],
                                password=request.POST['pwd'],
                                email =request.POST['email'])
            return redirect('/login/')

def login_Views(request):
    if request.method =='GET':
        url = request.META.get('HTTP_REFERER','/dm')
        if url[-10:] == '/register/':
            url ='/dm'
        print(url)
        request.session['url'] = url
        return render(request,'login.html')
    else:
        # 有COOKIES并点击一键登录
        if 'COOKIES' in request.POST:
            #添加session
            request.session['user']=request.COOKIES['username']
            return redirect('/dm/')
        else:
            #没COOKIES
            #名字是否在数据库中
            if m_user.objects.filter(user=request.POST['username']):
                cx = m_user.objects.get(user=request.POST['username'])
                #密码是否和用户相对应
                if request.POST['pwd'] == cx.password:
                    url = request.session['url']
                    del request.session['url']
                    fh = redirect(url, locals())
                    request.session['user'] = request.POST['username']
                    #是否记住密码
                    if 'reb' in request.POST:
                        fh.set_cookie('username',request.POST['username'], 60 * 60 * 24)
                        return fh
                    return fh
                else:
                    status ='2'
                    return render(request,'login.html',{'status':status})
            else:
                status = '1'
                return render(request,'login.html',{'status':status})


# def addlove_Views(request,id=0):
#     users = request.session['user']
#     u_user = m_user.objects.get(user=request.session['user'])
#     user = m_user.objects.get(user=users)
#     anime = Anima.objects.get(id=id)
#     cx = Anima.objects.all()
#     number = len(user.anime.all())
#     try:
#         a = u_user.anime.get(id=anime.id)
#     except:
#         addanime = u_user.anime.add(anime)
#         script = '添加成功'
#         user = request.session['user']
#     else:
#         script = '已经添加过了'
#     return render(request, 'dm.html', locals())
def upload_Views(request):
    #添加
    if request.method =='POST':
        new_img = Anima(
            name=request.POST['name'],
            An_type=request.POST['An_type'],
            l_ing = request.FILES.get('img'),
            web=request.POST['web'],
            code=request.POST['code']
        )
        new_img.save()
        script = '添加成功'
        return render(request,'upload.html',locals())
    else:
        return render(request, 'upload.html')


def love_Views(request,id=0):
    users = request.session['user']
    u_user = m_user.objects.get(user=request.session['user'])
    user = m_user.objects.get(user=users)
    if request.method == 'GET':
        if 'user' in request.session:
            alen = len(user.anime.all())
            request.session['alen'] = alen
            dm = user.anime.all()
            return render(request, 'love.html', locals())
        return redirect('/login')
    # else:
    #     #删除收藏
    #     if 'del' in request.POST:
    #         deldm = Anima.objects.get(id=request.POST['del'])
    #         u_user.anime.remove(deldm)
    #         u_user.save()
    #         dm = u_user.anime.all()
    #         script = "<script type='text/javascript'>alert('删除成功！');history.back();</script>"
    #         return redirect('/love')
    #     else:
    #         anime = Anima.objects.get(id=id)
    #         cx = Anima.objects.all()
    #         number = len(user.anime.all())
    #         try:
    #             a = u_user.anime.get(id = anime.id)
    #         except:
    #             addanime = u_user.anime.add(anime)
    #             script = '添加成功'
    #             user = request.session['user']
    #         else:
    #             script = '已经添加过了'
    #         return render(request, 'dm.html', locals())

def class_daily_Views(request):
    if request.method == 'GET':
        #分类
        status =request.GET['a_class']
        class_daily = Anima.objects.filter(An_type = status)
        json_cdm = serializers.serialize('json',class_daily)
        return render(request,'class/daily.html',locals())
    else:
        status = '搜索结果'
        statu = 1
        search = request.POST['name']
        class_daily = []
        dm = Anima.objects.all()
        for a in dm:
            if search in str(a):
                class_dail = Anima.objects.filter(name=a)
                class_daily.append(class_dail)
        #查询
        return render(request, 'class/daily.html', locals())

def jsclass_Views(request):
    pass

def Check_users_Voews(request):
    user = request.GET['uphone']
    if m_user.objects.filter(user=user):
        msg = '用户名已存在'
        status = 0
    else:
        status = 1
        msg = '用户名可用'
    dic = {
        'status':status,
        'msg':msg,
    }
    return HttpResponse(json.dumps(dic))

def Check_dm_Views(request):
    if 'user' in request.session:
        status = 1
        user = request.session['user']
        u_user = m_user.objects.get(user=request.session['user'])
        number = len(u_user.anime.all())
    else:
        status = 0
        user = 0
        number=0
    dic={
        'status':status,
        'user':user,
        'number':number
    }
    return HttpResponse(json.dumps(dic))


def loginout_Views(request):
    if 'user' in request.session:
        url = request.META.get('HTTP_REFERER','/dm')
        del request.session['user']
        print(url)
        return redirect(url)

def Collection_Views(request):
    dm_list =[]
    u_user = m_user.objects.get(user = request.session['user'])
    dm = u_user.anime.all()
    adm = serializers.serialize('json',dm)
    dic = {
        'a_dm':adm
    }
    dm_list.append(dic)
    return HttpResponse(json.dumps(dm_list))


def del_Collection_Views(request):
    id = request.GET['a_id']
    u_user = m_user.objects.get(user=request.session['user'])
    deldm = Anima.objects.get(id=id)
    u_user.anime.remove(deldm)
    u_user.save()
    dm = u_user.anime.all()
    adm = serializers.serialize('json', dm)
    status = 1
    dic = {
        'a_dm': adm
    }
    return HttpResponse(json.dumps(dic))
def anime_Views(request):
    anime_list = []
    anime = Anima.objects.all()
    for ani in anime:
        ani_jdon=json.dumps(ani.to_dict())
        dic={
            "ani":ani_jdon,
        }
        anime_list.append(dic)
    return HttpResponse(json.dumps(anime_list))


def addlove_Views(request):
    id = request.GET['id']
    if 'user' in request.session:
        users = request.session['user']
        u_user = m_user.objects.get(user=request.session['user'])
        user = m_user.objects.get(user=users)
        id = request.GET['id']
        anime = Anima.objects.get(id=id)
        number = len(user.anime.all())
        try:
            a = u_user.anime.get(id=anime.id)
        except:
            addanime = u_user.anime.add(anime)
            script = '添加成功'
            user = request.session['user']
            status = 1
        else:
            script = '已经添加过了'
            status = 2
    else:
        status = 0
        number = 0

    dic={
        'status':status,
        'number':number+1
        }
    return HttpResponse(json.dumps(dic))


