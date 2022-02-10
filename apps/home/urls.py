# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
import timeline.views as tl


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('/timeline', tl.index, name='timeline'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
