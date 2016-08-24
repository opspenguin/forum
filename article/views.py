from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from article.models import Article
from block.models import Block
from article.forms import ArticleForm

def article_list(request,block_id):
    ARTICLE_CNT_1PAGE=10
    page_no=int(request.GET.get("page_no","1"))
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    all_articles=Article.objects.filter(block=block,status=0).order_by("-id")
    p=Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page=p.page(page_no)
    #articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    articles_objs=page.object_list
    return render(request,"article_list.html",{"articles":articles_objs,"b":block})

def article_create(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=="GET":
        return render(request,"article_create.html",{"b":block})
    else:
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.block=block
            article.status=0
            article.save()
            return redirect("/article/list/%s"%block_id)
        else:
            return render(request,"article_create.html",{"b":block,"form":form})

def article_detail(request,article_id):
    article_id=int(article_id)
    article=Article.objects.get(id=article_id)
    return render(request,"article_detail.html",{"article":article})
