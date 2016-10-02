import boto3
import botocore
import re

#https://github.com/russellballestrini/botoform/blob/master/botoform/util.py
def make_tag_dict(ec2_object):
    """
    Return a dictionary of existing tags.
    :param ec2_object: A tagable Boto3 object with a tags attribute.
    :returns: A dictionary where tag names are keys and tag values are values.
    """
    tag_dict = {}
    if ec2_object.tags is None: return tag_dict
    for tag in ec2_object.tags:
        tag_dict[tag['Key']] = tag['Value']
    return tag_dict

class ParsedEC2Instance(object):
    def __repr__(self):
        return self.name

def listInstances(region, nameregex='^.*$'):
    ec2 = boto3.resource('ec2',region)
    instances = list(ec2.instances.all())
    parsedinstances = []
    for instance in instances:
        tags = make_tag_dict(instance)
        if re.match (nameregex, tags['Name']):
            parsedinstance = ParsedEC2Instance()
            parsedinstance.name = tags['Name']
            parsedinstance.allocatedto = tags['allocatedto']
            parsedinstance.id = instance.id
            parsedinstance.instance_type = instance.instance_type
            parsedinstance.powerState = instance.state['Name']
            parsedinstances.append(parsedinstance)
    return parsedinstances

def get_instance_id_by_name(instancename, region):
    ec2 = boto3.resource('ec2',region)
    namefilter = [ { 'Name' : 'tag:Name', 'Values' : [instancename] } ]
    instance = list(ec2.instances.filter(Filters=namefilter))[0]
    return instance.id

def start_instance_by_id(instanceid, region):
    ec2 = boto3.resource('ec2',region)
    try:
        ec2.instances.filter(InstanceIds=[instanceid]).start()
        return True
    except botocore.exceptions.ClientError as e:
        return e.response['Error'] #['Message']

def check_necessary_permissions(region):
    try:
        ec2 = boto3.resource('ec2',region)
        ec2.instances.limit(1).start(DryRun=True)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'UnauthorizedOperation':
            return "Insufficient IAM permissions"
        if e.response['Error']['Code'] == 'DryRunOperation':
            return True
    