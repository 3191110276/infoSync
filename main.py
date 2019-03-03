from infosync import controller
import json
import requests
import yaml

c = controller()


snow = yaml.load(open('./credentials.yaml',"r").read())['servicenow']

def create_fi(mac, ip, mask, gateway, model, serial, moid):
    #Need to install requests package for python
    #easy_install requests
    import requests

    # Set the request parameters
    url = 'https://' + snow['instance'] + '.service-now.com/api/now/table/cmdb_ci_ucs_equipment'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = snow['user']
    pwd = snow['pwd']

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    data = {
        "skip_sync": "false",
        "operational_status": "1",
        "dn": "",
        "discovery_source": "Intersight Connector",
        "asset_tag": "",
        "hardware_substatus": "",
        "fqdn": "",
        "sys_domain_path": "/",
        #"version": "10",
        "hardware_status": "installed",
        "install_status": "1",
        "name": moid,
        "default_gateway": gateway,
        "short_description": model,
        "sys_class_name": "cmdb_ci_ucs_equipment",
        "manufacturer": "Cisco",
        "sys_class_path": "/!!/!2/!5",
        "mac_address": mac,
        "vendor": "Cisco",
        "model_number": model,
        "total_fabric_interconnect": "2",
        "comments": "",
        "serial_number": serial,
        "ip_address": ip,
        "model_id": model,
        "unverified": "false",
        "location": "Vienna",
        "category": "Fabric Interconnect"
    }
    
    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))

    # Check for HTTP codes other than 200
    #if response.status_code != 200: 
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        #exit()

    # Decode the JSON response into a dictionary and use the data
    #data = response.json()
    #print(data)

    
def create_hxnode(num_cpus, num_cores, num_threads, total_mem, num_adaptors, model, serial, moid, ip, mask, gateway):
    #Need to install requests package for python
    #easy_install requests
    import requests

    # Set the request parameters
    url = 'https://' + snow['instance'] + '.service-now.com/api/now/table/cmdb_ci_ucs_rack_unit'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = snow['user']
    pwd = snow['pwd']

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    data = {
        "os_address_width": "",
        "operational_status": "1",
        "os_service_pack": "",
        "cpu_core_thread": "",
        "cpu_manufacturer": "Intel",
        "discovery_source": "Intersight Connector",
        "state": "",
        "ram": total_mem,
        "warranty_expiration": "",
        "cpu_name": "",
        "cpu_speed": "",
        "disk_space": "",
        "sys_domain_path": "/",
        "short_description": model,
        "num_of_cores": num_threads,
        "availability": "",
        "cpu_count": num_cpus,
        "manufacturer": "Cisco",
        "total_memory": total_mem,
        "vendor": "Cisco",
        "model_number": model,
        "number_of_adapters": num_adaptors,
        "serial_number": serial,
        "unverified": "false",
        "asset": "",
        "cpu_core_count": num_cores,
        "form_factor": "rack",
        "uuid": "",
        "hardware_substatus": "",
        "fqdn": "",
        "num_of_cpus": num_cpus,
        "server_id": "",
        "hardware_status": "installed",
        "install_status": "1",
        "name": moid,
        "subcategory": "",
        "default_gateway": gateway,
        "virtual": "false",
        "comments": "",
        "monitor": "false",
        "ip_address": ip,
        "model_id": "Cisco " + model,
        "sys_tags": "",
        "rack_serial": "",
        "location": "Vienna",
        "category": ""
        }
    
    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))

    # Check for HTTP codes other than 200
    #if response.status_code != 200: 
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        #exit()

    # Decode the JSON response into a dictionary and use the data
    #data = response.json()
    #print(data)


def create_incident(title, description, priority, urgency, severity, reference=""):
    # Set the request parameters
    url = 'https://' + snow['instance'] + '.service-now.com/api/now/table/incident?sysparm_display_value=test'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = snow['user']
    pwd = snow['pwd']

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    data = {
    "short_description": title,
    "description": description,
    "priority": priority,
    "urgency": urgency,
    "severity": severity,
    "caller_id": "Intersight Connection",
    "category": "inquiry",
    "approval": "not requested",
    "location": "Vienna",
    "sys_tags": "intersight-import",
    "active": "true",
    "comments": reference
    }

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))

    # Check for HTTP codes other than 200
    #if response.status_code != 200: 
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        #exit()

    # Decode the JSON response into a dictionary and use the data
    #data = response.json()
    #print(data)

    
#2 Set up transformation rules
def transform_network_elements(data):
    create_fi(data.out_of_band_mac, data.out_of_band_ip_address, data.out_of_band_ip_mask, data.out_of_band_ip_gateway, data.model, data.serial, data.moid)
    
def transform_compute_rack_units(data):
    create_hxnode(data.num_cpus, data.num_cpu_cores, data.num_threads, data.total_memory, data.num_adaptors, data.model, data.serial, data.moid, data.kvm_ip_addresses[0].address, data.kvm_ip_addresses[0].subnet, data.kvm_ip_addresses[0].default_gateway)
    
def transform_hyperflex_clusters(data):
    pass
    
def transform_cond_alarms(data):
    create_incident(data.description,data.description, 3, 2, 1, "Affected system ID: " + data.affected_mo_id + " with alarm code " + data.code)
    
def transform_hyperflex_alarms(data):
    create_incident(data.description,data.description, 3, 2, 1, "Cluster: " + data.entity_name)

c.add_rule('Intersight', 'network_elements', 'ADD', transform_network_elements)
c.add_rule('Intersight', 'compute_rack_units', 'ADD', transform_compute_rack_units)
c.add_rule('Intersight', 'hyperflex_clusters', 'ADD', transform_hyperflex_clusters)
c.add_rule('Intersight', 'cond_alarms', 'ADD', transform_cond_alarms)
c.add_rule('Intersight', 'hyperflex_alarms', 'ADD', transform_hyperflex_alarms)

#3 Start loop
c.start()