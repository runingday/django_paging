#coding:utf-8
from django.shortcuts import render, render_to_response
from app01 import models
from app01 import common
from app01 import html_helper



# Create your views here.


def index(request, page):

    page = common.try_int(page, 1)


    count = models.Host.objects.all().count()

    pageobj = html_helper.PageInfo(page, count)

    start = pageobj.start

    end = pageobj.end

    all_page_count = pageobj.all_page_count


    result = models.Host.objects.all()[start:end]
    page_string = html_helper.Pager(page, all_page_count)

    ret = {'data': result, 'count': count, 'page': page_string}
    return render_to_response('index.html', ret)
