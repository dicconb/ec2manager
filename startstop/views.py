from django.shortcuts import render
import boto3

# Create your views here.


def list_EC2_instances(request):
	return render(request, 'startstop/list_EC2_instances.html', {})