from django.shortcuts import render
from usercenter.models import ActivateCode
from django.utils import timezone

def activate(request,code):
    query=ActivateCode.objects.filter(code=code,expire_time__gte=timezone.now())
    if query.count()>0:
        record=query[0]
        record.owner.is_active=True
        record.owner.save()
        msg="激活成功，请登录"
        return render(request,"register_success.html",{"msg":msg})
    else:
        msg="激活失败"
        return render(request,"register_success.html",{"msg":msg})
