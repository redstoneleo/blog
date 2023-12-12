from django.db import models
from django import forms
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator
from django.utils import timezone
from markdown_it import MarkdownIt

from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.texmath import  texmath_plugin
from mdit_py_plugins.dollarmath import  dollarmath_plugin


class Post(models.Model):
	# class Category(models.TextChoices):
	# 	math = "高等数学",_("高等数学")#The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
	# 	mySoftware = "我的软件",_("我的软件")
	# 	paidService = "付费服务",_("付费服务")
	# 	# __empty__ = ""#未分类；Because an enumeration with a concrete data type requires all values to match the type, overriding the blank label cannot be achieved by creating a member with a value of None. Instead, set the __empty__ attribute on the class:
	Category = models.TextChoices("Category", "高等数学 我的软件 付费服务")

	title = models.CharField(max_length=90)
	body = models.TextField(verbose_name="仅支持HTML格式的内容",)
	category = models.CharField(max_length=4,choices=Category.choices, blank=True)#,default=Category.__empty__
	# isMarkdown=models.BooleanField(default=False, blank=True)
	slug=models.SlugField(default='', blank=True)
	firstReleaseDate = models.DateTimeField(auto_now_add=True)#default=timezone.now  因为cnblog用的是datetime，所以只能用DateTimeField，否则我想用DateField
	latestRevisionDate = models.DateTimeField(auto_now=True)#default=timezone.now  


	def __str__(self):
	    return self.title

	class Meta:
	    ordering = ['-latestRevisionDate']