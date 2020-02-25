#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   view.py    
@Auther  :  will_kkc 
@data    :  2020/2/25 14:55
@descr   :
'''

from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)
