from django.shortcuts import render
# 重定向
from django.shortcuts import redirect
# 一般用来返回错误提示
from django.http import HttpResponse
# 导入模型
from myblog.models import SiteInfo, Classes,UserInfo
# 发送json
from django.http import JsonResponse

# Create your views here.
# 新建新的页面在此处定义函数，函数名与mysite中urls.py添加的函数相同
def index(request):
    # 此处写入业务逻辑
    # 此处写入数据库
    
    # 站点基础信息
    siteinfo = SiteInfo.objects.all()[0] #获取siteinfo模型中的所有数据
    # 菜单分类
    classes = Classes.objects.all()

    # 全部用户
    userlist = UserInfo.objects.all()
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, 'index.html', data)

def classes(request):
     # 站点基础信息
    siteinfo = SiteInfo.objects.all()[0] #获取siteinfo模型中的所有数据
    # 菜单分类
    classes = Classes.objects.all()
    # 对应用户列表
    try:
        choosed_id = request.GET['id'] #直接访问classes会报错
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id) #即使是空也返回数组
        print(choosed)
    except :
        return redirect('/')
    # 解决错误
    if choosed:
        userlist = UserInfo.objects.filter(belong=choosed[0])
    else:
        data = {
            "value": "无结果"
        }
        # return HttpResponse('<h1>无结果</h1>')
        # return JsonResponse(data)
        return redirect('/')
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, 'classes.html', data)