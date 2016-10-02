from django.shortcuts import render
from helpers import util

# Create your views here.


def list_EC2_instances(request):
	if util.check_necessary_permissions('eu-west-1') == True:	
		instances = util.listInstances(region='eu-west-1',nameregex='^dev1-dev.*')
		return render(request, 'startstop/list_EC2_instances.html', {'instances': instances})
	else:
		return render(request, 'startstop/error.html', {'error': 'Insufficient IAM permissions to start instances. Please check with the administrator.'})

