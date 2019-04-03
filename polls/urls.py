from django.urls import path
from django.urls import re_path

from . import views


app_name = "request_demo"
urlpatterns = [
    # ex: /polls/
    re_path(r'^index/$', views.index, name='index'),

    # ex: /polls/
    re_path(r'^index/request_demo/$', views.request_demo, name='request_demo'),

    re_path(r'^intro/$', views.index, name='intro'),















    # ex: /polls/5/
    # first element is path, second is view's content, the last one is name
    # 在浏览器中，如果你转到 "/polls/34/" ，Django 将会运行 detail() 方法并且展示你在 URL 里提供的问题 ID。
    # 再试试 "/polls/34/vote/" 和 "/polls/34/vote/" ——你将会看到暂时用于占位的结果和投票页。
    # 当某人请求你网站的某一页面时——比如说， "/polls/34/" ，Django 将会载入 pythonWebsite.urls 模块，
    # 因为这在配置项 ROOT_URLCONF 中设置了。# ROOT_URLCONF = 'pythonWebsite.urls' #
    # 然后 Django 寻找名为 urlpatterns 变量 (pythonWebsite的url配置中的路径)
    # 并且按序匹配正则表达式。在找到匹配项 'polls/'，它切掉了匹配的文本（"polls/"），(匹配到的了就切掉了)
    # 将剩余文本——"34/"，发送至 'polls.urls' URLconf 做进一步处理。在这里剩余文本匹配了 '<int:question_id>/'，
    # 使得我们 Django 以如下形式调用 detail():
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]