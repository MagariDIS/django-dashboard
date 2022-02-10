# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


'''
def projects_detail_view(request, p_pk):
    project = Projects.objects.get(pk=p_pk)
    # 完了済のタスクを取得し、開始日の昇順でタスク一覧を取得
    tasks = project.project_task.filter(status=2).order_by('createdDate')
    df = []
    for task in tasks:
        df.append(
            dict(Task=task.taskName,
                 # create_ganttのStartとFinishで使うため、フォーマットを整形
                 Start="{0:%Y-%m-%d %H:%M:%S}".format(task.createdDate),
                 Finish="{0:%Y-%m-%d %H:%M:%S}".format(task.finishedDate),))
    fig = ff.create_gantt(df, title='これまでの軌跡', bar_width=0.5, showgrid_x=True, showgrid_y=False,)
    plot_html = plot(fig, output_type='div', include_plotlyjs=False)

    context = {
        'home/plot_html': plot_html,
    }
    return render(request, 'home/detail.html', context)
'''
