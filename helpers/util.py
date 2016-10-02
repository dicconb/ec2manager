import boto3

#https://github.com/russellballestrini/botoform/blob/master/botoform/util.py
def tag_filter(tag_key, tag_values):
    """
    Return a tag filter document expected by boto3.
    :param tag_key: A tag key or name.
    :param tag_values: The tag value or a list of values to filter on.
    :returns: A filter document (list/dict) in the form that Boto3 expects.
    """
    return make_filter('tag:{}'.format(tag_key), tag_values)
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
	pass

def listInstances(region):
    ec2 = boto3.resource('ec2',region)
    instances = list(ec2.instances.all())
    parsedinstances = []
    for instance in instances:
        tags = make_tag_dict(instance)
        parsedinstance = ParsedEC2Instance()
        parsedinstance.name = tags['Name']
        parsedinstance.id = instance.id
        parsedinstance.instance_type = instance.instance_type
        parsedinstance.powerState = instance.state['Name']
        parsedinstances.append(parsedinstance)
    return parsedinstances