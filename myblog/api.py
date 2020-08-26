from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import SiteInfo, Classes, UserInfo
# 自己写的json序列化工具
from myblog.toJson import  Classes_data, UserInfo_data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.authtoken.models import Token
import json

@api_view(['GET','POST'])
def api_test(request):
    # if request.method == 'POST':
    #     return Response('post')
    classes = Classes.objects.all() #原始数据
    # classes_data = Classes_data(classes, many = True) #使用toJson的类进行转化
    
    # userlist = UserInfo.objects.all()
    # userlist_data = UserInfo_data(userlist, many = True)
    
    # data = {
    #     'classes': classes_data.data,
    #     'userlist': userlist_data.data
    # }

    data = {
        'classes': []
    }
    for c in classes:
        data_item = {
            'id': c.id,
            'text': c.text,
            'userlist': []
        }
        userlist = c.userinfo_classes.all() #通过model中的related_name进行反向查询
        for user in userlist:
            user_data = {
                'id': user.id,
                'nickname': user.NickName,
                'headimg': str(user.HeadImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    # data = json.dumps(data)
    return Response(data)

@api_view(['GET'])
def getMenuList(request):
    allClasses = Classes.objects.all()
    siteinfo = SiteInfo.objects.get(id = 1)
    siteinfo_data = {
        'sitename': siteinfo.title,
        'logo':'http://127.0.0.1:9000/upload/'+str(siteinfo.logo)
    }
    # 整理数据为json
    menu_data = []
    for c in allClasses:
        # 设计单条数据的结构
        data_item = {
            'id': c.id,
            'text': c.text,
        }
        menu_data.append(data_item)
    data = {
        'menu_data':menu_data,
        'siteinfo':siteinfo_data
    }
    return Response(data)

@api_view(['GET'])
def getUserList(request):
    # 获得前端发送的id开始查找数据库
    menuId = request.GET['id'] # 对应vue/UserList.vue中的params:{id}
    print(menuId)
    menu = Classes.objects.get(id=menuId)
    print(menu)
    UserList = UserInfo.objects.filter(belong=menu)
    print(UserList)
    
    #开始整理数据列表准备发送给前端
    data = []
    for user in UserList:
        data_item = {
            'id':user.id,
            'headImg':str(user.HeadImg),
            'nickName':user.NickName,
        }
        data.append(data_item)
    return Response(data)

@api_view(['POST'])
def toLogin(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    # print(username, password)
    # 查询数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        # 未通过是none
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            token = Token.objects.update_or_create(user = user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            data = {
                'token': token.key
            }
            return Response(data)
        else:
            return Response('pwderr')
    else:
        return Response('none') # 对应为axios/res/data数据

@api_view(['POST'])
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username, password, password2)

    # 判断用户是否存在
    user = User.objects.filter(username = username)
    if len(user)>0:
        return Response('false_same')
    else:
        newPassword = make_password(password, username)
        newUser = User(username=username, password=newPassword)
        newUser.save()
    return Response('ok')

@api_view(['POST','PUT'])
def uploadLogo(request):
    if request.method == 'PUT':
        sitename = request.POST['sitename']
        old_info = SiteInfo.objects.get(id=1)
        old_info.title = sitename
        new_info = SiteInfo.objects.get(id=2)
        old_info.logo = new_info.logo
        old_info.save()
        return Response('ok')
    img = request.FILES['logo']
    # print(img)
    test_siteLogo = SiteInfo.objects.get(id=2)
    test_siteLogo.logo = img
    test_siteLogo.save()
    data = {
        'img': str(test_siteLogo.logo)
    }
    return Response(data)