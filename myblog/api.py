from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog.models import Classes, UserInfo
# 自己写的json序列化工具
from myblog.toJson import Classes_data, UserInfo_data
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
    return Response('ok')