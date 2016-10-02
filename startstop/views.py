from django.shortcuts import render
from helpers import util

# Create your views here.


def list_EC2_instances(request):
	instances = util.listInstances('eu-west-1')
	return render(request, 'startstop/list_EC2_instances.html', {'instances': instances})
