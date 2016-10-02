from django.shortcuts import render
from helpers import util

# Create your views here.


def list_EC2_instances(request):
	instances = util.listInstances(region='eu-west-1',nameregex='^dev1-dev.*')
	return render(request, 'startstop/list_EC2_instances.html', {'instances': instances})

