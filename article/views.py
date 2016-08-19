from django.shortcuts import render,redirect

from article.models import Article
from block.models import Block

def article_list(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":articles_objs,"b":block})

def article_create(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=="GET":
        return render(request,"article_create.html",{"b":block})
    else:
        title=request.POST["title"]
        content=request.POST["content"]
        if not title or not content:
            error="标题和内容都不能为空"
            return render(request,"article_create.html",{"b":block,"error":error})
        if len(title)>100 or len(content)>10000:
            error="标题或内容过长"
            return render(request,"article_create.html",{"b":block,"error":error,"title":title,"content":content})
        article=Article(block=block,title=title,content=content,status=0)
        article.save()
        return redirect("/article/list/%s"%block_id)
