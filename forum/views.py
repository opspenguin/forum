#from django.http import HttpResponse
from django.shortcuts import render,redirect
from block.models import Block
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
import datetime
from usercenter.models import ActivateCode
from django.core.mail import send_mail

def index(request):
    #return HttpResponse("hello world")
    #block_infos=Block.objects.all().order_by("-id")
    block_infos=Block.objects.filter(status=0).order_by("-id")
    return render(request,"index.html",{"blocks":block_infos})

def register(request):
    error=""
    if request.method=="GET":
        return render(request,"register.html")
    else:
        username=request.POST["username"].strip()
        email=request.POST["email"].strip()
        password=request.POST["password"].strip()
        re_password=request.POST["re_password"].strip()
        if not username or not email or not password or not re_password:
            error="任何字段都不能为空"
        if password != re_password:
            error="两次密码不一致"
        if User.objects.filter(username=username).count()>0:
            error="用户已存在"
        if User.objects.filter(email=email).count()>0:
            error="邮箱已存在"
        if not error:
            user=User.objects.create_user(username=username,email=email,password=password,is_active=False)
            user.save()

            code=str(uuid.uuid4()).replace("-", "") 
            expire_time=timezone.now() + datetime.timedelta(days=2)
            code_record=ActivateCode(owner=user, code=code, expire_time=expire_time)
            code_record.save()

            activate_link = "http://%s/activate/%s" % (request.get_host(), code)
            activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link
            send_mail(subject='[TEST]激活邮件',
                      message='点击链接激活: %s' % activate_link,
                      html_message=activate_email,
                      from_email='1004020240@qq.com',
                      recipient_list=[email],
                      fail_silently=False)
        else:
            return render(request,"register.html",{"error":error})
        return redirect("/")
