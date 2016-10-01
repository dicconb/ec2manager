from django.shortcuts import render
import boto3

# Create your views here.


def list_EC2_instances(request):
	ec2 = boto3.resource('ec2','eu-west-1')
	instances = ec2.instances.all()
	return render(request, 'startstop/list_EC2_instances.html', {'instances': instances})