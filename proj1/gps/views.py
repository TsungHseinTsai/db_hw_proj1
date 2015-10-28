from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from gps.models import Post

# Create your views here.

def locat(request):
	return render(request,
                  'locat.html')

				  
def received(request):
	if request.method == 'POST':
		Title = request.POST.get('Title')
		X = request.POST.get('Xpos')
		Y = request.POST.get('Ypos')
		Post.objects.create(title=Title,Xpos=X,Ypos=Y)
		return render_to_response('received.html',
                                  {'status': HttpResponse(status=200) , 'Title' : Title , 'Xpos' : X , 'Ypos' : Y})
	return render_to_response('received.html',
                              {'status': HttpResponse(status=404)})