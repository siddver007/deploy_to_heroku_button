from django.shortcuts import render_to_response, render
from django.http import HttpResponseBadRequest, HttpResponse
from django.template import RequestContext
import django_excel as excel
from collections import Counter
from forms import UploadFileForm
import time

def getServerHitTime(request):
	return HttpResponse(time.ctime())

def csvProcessView(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			filehandle = request.FILES['file']
			csv_dict = filehandle.get_dict()
			duplicates = [k for k,v in Counter(csv_dict['Well_ID']).items() if v>1]
			return HttpResponse('The number of duplicates = ' + str(len(duplicates)))
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render_to_response('upload_form.html',
						{'form': form},
						context_instance=RequestContext(request))
