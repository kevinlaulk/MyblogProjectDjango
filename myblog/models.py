from django.db import models

# Create your models here.
# 这里就是定义数据库、数据表
# 网站信息
class SiteInfo(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    
    # 展示数据
    def __int__(self):
        # 定义查询该表单时返回的是什么
        return self.id #每加入一条数据就会有一条id
    
    def __str__(self):
        return self.title

    # 写完之后检查数据库差异并更新，终端输入：
    # 同步执行-数据迁移
    # python manage.py makemigrations 监测数据库是否改变
    # python manage.py migrate 合并改变

# 课程分类
class Classes(models.Model):
    text = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.text

# 用户
class UserInfo(models.Model):
    NickName = models.CharField(max_length=50, null=True, blank=True)
    HeadImg = models.ImageField(upload_to='UserInfo/', null=True, blank=True)
    belong = models.ForeignKey(Classes, on_delete=models.SET_NULL, related_name="userinfo_classes", null=True, blank=True)
    def __str__(self):
        return self.NickName

    