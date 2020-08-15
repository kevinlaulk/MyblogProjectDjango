from rest_framework import serializers
# 序列化工具
from myblog.models import Classes, UserInfo

# 与models类似
class Classes_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Classes
        fields = '__all__'

# 与models类似
class UserInfo_data(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = UserInfo
        fields = '__all__'
 