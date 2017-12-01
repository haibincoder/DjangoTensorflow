from django.shortcuts import render
#from .models import Article, Category, BlogComment, Tag, Suggest
#from .forms import BlogCommentForm, SuggestForm
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import markdown
import re
import logging
from .tasks import celery_send_email

# Create your views here.

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        """
        过滤数据，并转为html格式
        Returns:

        """

        return


def blog_search(request,):

    print("function search:")
    print(request.GET["name"])
    return redirect('app:index')


def suggest_view(request):
    # form = SuggestForm()
    # if request.method == 'POST':
    #     form = SuggestForm(request.POST)
    #     if form.is_valid():
    #         suggest_data = form.cleaned_data['suggest']
    #         # new_record = Suggest(suggest=suggest_data)
    #         # new_record.save()
    #         # try:
    #         #     # 使用celery并发处理邮件发送的任务
    #         #     celery_send_email.delay('访客意见', suggest_data, 'haibincoder@outlook.com', ['tomming233@163.com'])
    #         # except Exception as e:
    #         #     logger.error("邮件发送失败: {}".format(e))
    #         return redirect('app:thanks')
    return render(request, 'blog/about.html')

