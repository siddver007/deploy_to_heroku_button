from django.shortcuts import render_to_response, render
from django.http import HttpResponseBadRequest, HttpResponse
from django.template import RequestContext
from collections import Counter
from forms import UploadFileForm
import time

def getServerHitTime(request):
	return HttpResponse(time.ctime())

def csvProcessView(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			start_time = time.time()
			filehandle = request.FILES['file']
			csv_list = []

			filename = filehandle.name
			if not filename.endswith('.csv'):
				return HttpResponse('Not a CSV file')

			for line in filehandle:
				csv_list.append(tuple(line.strip().split(',')))
			filehandle.close()	

			duplicates = [k for k,v in Counter(csv_list).items() if v>1]
			duplicate_number = len(duplicates)

			duplicate_rows_string = ''			
			for row in duplicates:
				duplicate_rows_string += str(row).replace('u\'','').replace('\'','') + '<br><br>'

			if duplicate_rows_string != '':	
				return HttpResponse('Number of duplicate rows = ' + '<b>' + str(duplicate_number) + '</b><br>'+ '(Approx. time taken : ' +
					str('{0:.1f}'.format(time.time() - start_time)) + ' sec)' + '<br><br>' + '<br><br><b>Duplicate Rows(Tuples)</b>:-' +
					'<br><br>' + duplicate_rows_string)
			else:
				return HttpResponse('Number of duplicate rows = ' + '<b>' + str(duplicate_number) + '</b><br>'+ '(Approx. time taken : ' + 
					str('{0:.1f}'.format(time.time() - start_time)) + ' sec)' + '<br><br>' + '<br><br><b>Duplicate Rows(Tuples)</b>:-'
					'<br><br>No duplicate rows')	
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render_to_response('upload_form.html',
						{'form': form},
						context_instance=RequestContext(request))
