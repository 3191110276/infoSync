import requests
import json

def create_fi(instance, user, pwd, mac, ip, mask, gateway, model, serial, moid):
    # Set the request parameters
    url = 'https://' + instance + '.service-now.com/api/now/table/cmdb_ci_ucs_equipment'

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
    requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))
    
    
def create_hxnode(instance, user, pwd, num_cpus, num_cores, num_threads, total_mem, num_adaptors, model, serial, moid, ip, mask, gateway):
    # Set the request parameters
    url = 'https://' + instance + '.service-now.com/api/now/table/cmdb_ci_ucs_rack_unit'

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
    requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))


def create_incident(instance, user, pwd, title, description, priority, urgency, severity, reference=""):
    # Set the request parameters
    url = 'https://' + instance + '.service-now.com/api/now/table/incident?sysparm_display_value=test'

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
    requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(data))