from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

import simplejson
import csv

# Create your views here.
    
def tracts(request, extension, state="", county="", tract=""):
    
    test = { 'a':1, 'b':2 }
    
    if extension == 'json':
        return HttpResponse(simplejson.dumps(test), mimetype='application/json')
    
    elif extension == 'csv':
        response = HttpResponse(mimetype='text/csv')
        filename = "%s%s%s.csv" % (state,county,tract)
        response['Content-Disposition'] = 'attachment; filename=' + filename
        writer = csv.writer(response)
        writer.writerow(test.values())
        return response
    
    else: #html
        return render_to_response('tracts.html',
            {
                'state': state,
                'county': county,
                'tract': tract,
                'extension': extension,
            },
            context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))