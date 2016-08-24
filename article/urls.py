from django.conf.urls import url

from article.views import *

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
    url(r'^create/(?P<block_id>\d+)', article_create),
    url(r'^detail/(?P<article_id>\d+)', article_detail),
]
