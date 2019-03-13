from infosync import controller
from example_functions import create_fi, create_hxnode, create_incident
import json
import requests
import yaml

c = controller()


snow = yaml.load(open('./credentials.yaml',"r").read())['servicenow']

    
#2 Set up transformation rules
def add_network_elements(data):
    create_fi(snow['instance'], snow['user'], snow['pwd'], data.out_of_band_mac, data.out_of_band_ip_address, data.out_of_band_ip_mask, data.out_of_band_ip_gateway, data.model, data.serial, data.moid)
    
def delete_network_elements(data):
    pass
    
def add_compute_rack_units(data):
    create_hxnode(snow['instance'], snow['user'], snow['pwd'], data.num_cpus, data.num_cpu_cores, data.num_threads, data.total_memory, data.num_adaptors, data.model, data.serial, data.moid, data.kvm_ip_addresses[0].address, data.kvm_ip_addresses[0].subnet, data.kvm_ip_addresses[0].default_gateway)
    
def delete_compute_rack_units(data):
    pass
    
def add_hyperflex_clusters(data):
    pass

def delete_hyperflex_clusters(data):
    pass
    
def add_cond_alarms(data):
    create_incident(snow['instance'], snow['user'], snow['pwd'], data.description,data.description, 3, 2, 1, "Affected system ID: " + data.affected_mo_id + " with alarm code " + data.code)
    
def delete_cond_alarms(data):
    pass
    
def add_hyperflex_alarms(data):
    create_incident(snow['instance'], snow['user'], snow['pwd'], data.description,data.description, 3, 2, 1, "Cluster: " + data.entity_name)
    
def delete_hyperflex_alarms(data):
    pass

c.add_rule('Intersight', 'network_elements', 'ADD', add_network_elements)
c.add_rule('Intersight', 'compute_rack_units', 'ADD', add_compute_rack_units)
c.add_rule('Intersight', 'hyperflex_clusters', 'ADD', add_hyperflex_clusters)
c.add_rule('Intersight', 'cond_alarms', 'ADD', add_cond_alarms)
c.add_rule('Intersight', 'hyperflex_alarms', 'ADD', add_hyperflex_alarms)

c.add_rule('Intersight', 'network_elements', 'DELETE', delete_network_elements)
c.add_rule('Intersight', 'compute_rack_units', 'DELETE', delete_compute_rack_units)
c.add_rule('Intersight', 'hyperflex_clusters', 'DELETE', delete_hyperflex_clusters)
c.add_rule('Intersight', 'cond_alarms', 'DELETE', delete_cond_alarms)
c.add_rule('Intersight', 'hyperflex_alarms', 'DELETE', delete_hyperflex_alarms)

#3 Start loop
c.start()