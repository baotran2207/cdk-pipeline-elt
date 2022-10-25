# After we successfully deploy/run this repo . we can get the list of resources created by cdk by simply run : python get_created_resources.py

import aws_cdk.cx_api as cx_api
from pprint import pprint
import json
cloud_assembly = cx_api.CloudAssembly("cdk.out")
resources = [stack.template["Resources"] for stack in cloud_assembly.stacks]

f = open('/tmp/resources.json', 'w+')
json.dump(resources, f)

# the resources created will be save at /tmp/resources.json