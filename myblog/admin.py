from django.contrib import admin
from myblog.models import SiteInfo, Classes, UserInfo
# Register your models here.
# 将数据表注册后可以在后台看到
admin.site.register(SiteInfo)
admin.site.register(Classes)
admin.site.register(UserInfo)