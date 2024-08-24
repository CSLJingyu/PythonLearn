from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator


# Create your views here.

# 实现HTML页面表达的内容


def hello_world(request):
    return HttpResponse("hello worlddededede")


def hello_world1(request):
    return HttpResponse("helloxxx")


def article_content(request):
    a = Article.objects.all()[0]
    title = a.title
    brief_content = a.brief_content
    content = a.content
    a_id = a.article_id
    a_publishdate = a.publish_date
    res_str = 'title: %s, brief_content: %s, ' \
              'content: %s, a_id: %s, a_publishdate: %s' % (title, brief_content, content,
                                                            a_id, a_publishdate)

    return HttpResponse(res_str)


# 传入到index.html中的article_list
# 设置分页URL设置 分页参数为page
def get_index_page(request):
    # 得到page参数 此时为字符串
    page = request.GET.get('page')
    # 将字符串转为整型
    if page:
        page = int(page)
    else:
        # 如果没有得到合法的page,就默认为1
        page = 1
    print('page: ', page)

    # 通过分页组件
    # 得到全部文章对象
    all_article = Article.objects.all()

    # 得到最近的3篇文章 倒序排序
    top3_article_list = Article.objects.order_by('-publish_date', )[:3]

    # 每页三条数据
    paginator = Paginator(all_article, 2)
    # 分页数量
    page_num = paginator.num_pages
    print('total:', paginator.num_pages)
    # 得到某一页文章的列表
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_age = page - 1
    else:
        previous_age = page

    # 实现了分页功能 返回的当前页面下的文章页面
    return render(request, 'blog/index.html',
                  {
                      'article_list': page_article_list,
                      'page_num': range(1, page_num + 1),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous_age': previous_age,
                      'top3_article_list': top3_article_list
                  }
                  )


# 通过article_id得到指定页面信息
def get_detail_page(request, article_id):
    print('id:', article_id)
    # 先得到全部文章对象
    all_article = Article.objects.all()

    # 创建目标文章对象
    curr_article = None
    # 定义上,下文章的id
    previous_article = None
    next_article = None
    previous_index = 0
    next_index = 0
    # 遍历得到目标文章id
    for index, articles in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if articles.article_id == article_id:
            curr_article = articles
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break

    # 每个文章的章节内容
    section_list = curr_article.content.split('\n')
    return render(request, 'blog/detail.html',
                  {'curr_article': curr_article,
                   'section_list': section_list,
                   'previous_article': previous_article,
                   'next_article': next_article
                   }
                  )

# 分页的URL设置
