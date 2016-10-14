#!/usr/bin/env python
#coding:utf-8
from django.utils.safestring import mark_safe

class PageInfo:

    def __init__(self, current_page, all_count, per_item=5):
        self.Current_page = current_page
        self.All_count = all_count
        self.Per_item = per_item
    '''
    #第一页 0 - 5 page=1
    #第二页 5 - 10 page=2
    #第三页 10 - 15 page=3
    #(page-1) * 5   page * 5
    '''


    @property
    def start(self):

        return (self.Current_page - 1) * self.Per_item

    @property
    def end(self):

        return self.Current_page * self.Per_item

    @property
    def all_page_count(self):

        temp = divmod(self.All_count, self.Per_item)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1

        return all_page_count


def Pager(page, all_page_count):
    '''
    page 表示当前页
    all_page_count 表示页数量
    '''
    page_html = []

    first_html = "<a href='/index/%d'>首页</a>" % (1)

    page_html.append(first_html)

    if page <= 1:
        prev_html = "<a href='#'>上一页</a>"
    else:
        prev_html = "<a href='/index/%d'>上一页</a>" % (page - 1)
    page_html.append(prev_html)

    #11个页码
    if all_page_count < 11:
        begin = 0
        end = all_page_count
    #总页数大于11
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > all_page_count:
                begin = page - 5
                end = all_page_count
            else:
                begin = page -5
                end = page + 6


    for i in range(all_page_count):

        if page == i + 1:
            a_html = "<a class='selected' href='/index/%d'>%d</a>" % (i + 1, i + 1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" % (i + 1, i + 1)

        page_html.append(a_html)

    next_html = "<a href='/index/%d'>下一页</a>" % (page + 1)
    page_html.append(next_html)

    end_html = "<a href='/index/%d'>尾页</a>" % (all_page_count)

    page_html.append(end_html)

    page_string = mark_safe(''.join(page_html))

    return page_string