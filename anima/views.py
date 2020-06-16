
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
def dm_Views(request):
    #分类
    an_class=['冒险','日常','后宫']
    if request.method =='GET':
        if request.session=='user':
            user = request.session['user']
            cx = Anima.objects.all()
            u_user = m_user.objects.get(user=request.session['user'])
            number = len(u_user.anime.all())

            return render(request, 'dm.html', locals())
        else:
            if 'user' in request.session:
                #计算数量
                u_user = m_user.objects.get(user=request.session['user'])
                number = len(u_user.anime.all())
                cx = Anima.objects.all()
                return render(request, 'dm.html', locals())
            cx = Anima.objects.all()
            return render(request, 'dm.html', locals())
    else:
        #退出登录
        if 'cancellation' in request.POST:
            del request.session['user']
            return redirect('/login/')
        else:
            #排序
            if 'sort' in request.POST:
                if request.POST['sort']=='时间':
                    u_user = m_user.objects.get(user=request.session['user'])
                    number = len(u_user.anime.all())
                    cx =Anima.objects.order_by('-time')
                    return render(request, 'dm.html', locals())
                else:
                    u_user = m_user.objects.get(user=request.session['user'])
                    number = len(u_user.anime.all())
                    cx = Anima.objects.order_by('name')
                    return render(request, 'dm.html', locals())

def register_Views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        #注册用户要大于2个字和小于20
        if len(request.POST['user_name'])>=2 and len(request.POST['user_name'])<=20:
            #查看该用户是否已存在数据库内
            if m_user.objects.filter(user=request.POST['user_name']):
                a = '用户名存在'
                return render(request,'register.html',{'a':a})
            else:
                # 密码要大于8个字和小于20
                if len(request.POST['pwd'])>=8 and len(request.POST['pwd'])<=20:
                    if request.POST['pwd']==request.POST['cpwd']:
                        m_user.objects.create(user=request.POST['user_name'],
                                          password=request.POST['pwd'],
                                          email=request.POST['email'])
                        return redirect('/login/')
                    else:
                        b = '两次输入密码不同'
                        return render(request,'register.html',{'b':b})
                else:
                    b ='密码不合法'
                    return render(request, 'register.html', {'b': b})
        else:
            a ='用户名不合法'
            return render(request, 'register.html', {'a': a})

def login_Views(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        # 有COOKIES并点击一键登录
        if 'COOKIES' in request.POST:
            #添加session
            request.session['user']=request.COOKIES['username']
            return redirect('/dm/',locals())
        else:
            #没COOKIES
            #名字是否在数据库中
            if m_user.objects.filter(user=request.POST['username']):
                cx = m_user.objects.get(user=request.POST['username'])
                fh = redirect('/dm/',locals())
                #密码是否和用户相对应
                if request.POST['pwd'] == cx.password:
                    request.session['user'] = request.POST['username']
                    script = '登录成功'
                    #是否记住密码
                    if 'reb' in request.POST:
                        fh.set_cookie('username',request.POST['username'], 60 * 60 * 24)
                        return fh
                    return fh
                else:
                    b ='密码错误'
                    return render(request,'login.html',{'b':b})
            else:
                a = '用户不存在'
                return render(request,'login.html',{'a':a})
            #else:
                # a = '用户不存在'
                # return render(request, 'login.html', {'a': a})


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
    if request.method == 'GET':
        return redirect('/login')
    else:
        #删除收藏
        if 'del' in request.POST:
            user = m_user.objects.get(user=request.session['user'])
            deldm = Anima.objects.get(id=request.POST['del'])
            user.anime.remove(deldm)
            user.save()
            dm = user.anime.all()
            script = "<script type='text/javascript'>alert('删除成功！');history.back();</script>"
            return render(request, 'love.html', locals())
        else:
            #id默认值为0
            if id ==0:
                #显示收藏
                user = m_user.objects.get(user=request.POST['id'])
                dm = user.anime.all()
                return render(request,'love.html',locals())
            else:
                #添加收藏
                user = m_user.objects.get(user=request.session['user'])
                anime = Anima.objects.get(id=id)
                try:
                    a = user.anime.get(id = anime.id)
                except:
                    addanime = user.anime.add(anime)
                    script = '添加成功'
                    user = request.session['user']
                    cx = Anima.objects.all()
                    u_user = m_user.objects.get(user=request.session['user'])
                    number = len(u_user.anime.all())
                    return render(request, 'dm.html', locals())
                else:
                    return HttpResponse('已经添加过了')

def class_daily_Views(request):
    if request.method == 'GET':
        #分类
        a =request.GET['a_class']
        class_daily = Anima.objects.filter(An_type = a)
        return render(request,'class/daily.html',locals())
    else:
        a = '搜索结果'
        print(request.POST['name'])
        #查询
        class_daily = Anima.objects.filter(name=request.POST['name'])
        return render(request, 'class/daily.html', locals())
