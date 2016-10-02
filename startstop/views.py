from django.shortcuts import render
from helpers import util
from django.contrib.auth.decorators import login_required

# Create your views here.

def list_EC2_instances(request):
	if util.check_necessary_permissions('eu-west-1') == True:	
		instances = util.listInstances(region='eu-west-1',nameregex='^dev1-dev.*')
		return render(request, 'startstop/list_EC2_instances.html', {'instances': instances})
	else:
		return render(request, 'startstop/error.html', {'error': 'Insufficient IAM permissions to start instances. Please check with the administrator.'})

@login_required
def start_instance(request):
	if request.method == 'POST':
		try:
			util.start_instance_by_id(request.POST['instanceid'], 'eu-west-1')
			return render(request, 'startstop/error.html', {'error': 'Success! Instance should be ready to use in about 5 minutes.'})
		except BaseException as e:
			return render(request, 'startstop/error.html', {'error': (e)})			
	else:
		return render(request, 'startstop/error.html', {'error': 'You shouldn\'t GET this page (expected an HTTP POST).'})