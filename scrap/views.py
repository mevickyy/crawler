from .crawler import Crawler
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
import json


def crawler_view(request):
	url = request.GET['url'].encode("ascii","replace")
	level = int(request.GET['level'].encode("ascii","replace"))
	# import ipdb;ipdb.set_trace()
	res = Crawler(url, level=level)
	# import ipdb;ipdb.set_trace()
	response = res.scrape()
	res = JsonResponse({"result": response})
	res['Access-Control-Allow-Origin'] = '*'
	return res