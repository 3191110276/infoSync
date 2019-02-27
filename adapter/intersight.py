import intersight
from intersight.intersight_api_client import IntersightApiClient

class connector:
    def __init__(self, apikey, keyfile):
        api_instance = IntersightApiClient(
            private_key=keyfile,
            api_key_id=api_key
        )
        
        self.NetworkElementApi = intersight.NetworkElementApi(api_instance)
        self.ComputeRackUnitApi = intersight.ComputeRackUnitApi(api_instance)
        self.HyperflexClusterApi = intersight.HyperflexClusterApi(api_instance)
        self.CondAlarmApi = intersight.CondAlarmApi(api_instance)
        self.HyperflexAlarmApi = intersight.HyperflexAlarmApi(api_instance)
    
    
    
    
    
    
    
    #networkelemApi = intersight.NetworkElementApi(api_instance)
#intersight_networkelems = networkelemApi.network_elements_get()
#
#rackApi = intersight.ComputeRackUnitApi(api_instance)
#intersight_racks = rackApi.compute_rack_units_get()
#
#hxclustersApi = intersight.HyperflexClusterApi(api_instance)
#intersight_clusters = hxclustersApi.hyperflex_clusters_get()
#
#alarmApi = intersight.CondAlarmApi(api_instance)
#intersight_alarms = alarmApi.cond_alarms_get()
#
#alarmApi = intersight.HyperflexAlarmApi(api_instance)
#hx_alarms = alarmApi.hyperflex_alarms_get()
#
#for net in intersight_networkelems.results:
#    #print(net.device_mo_id)
#    #print(net.ucsm_running_firmware)
#    create_fi(net.out_of_band_mac, net.out_of_band_ip_address, net.out_of_band_ip_mask, net.out_of_band_ip_gateway, net.model, net.serial, net.moid)
#    
#for rack in intersight_racks.results:
#    #print(rack.account_moid)
#    #print(rack.available_memory)
#    #print(rack.num_eth_host_interfaces)
#    #print(rack.adapters[0])
#    #if len(rack.tags) > 0:
#        #print(rack.tags[0].value)
#    #print(rack.top_system.moid)
#    create_hxnode(rack.num_cpus, rack.num_cpu_cores, rack.num_threads, rack.total_memory, rack.num_adaptors, rack.model, rack.serial, rack.moid, rack.kvm_ip_addresses[0].address, rack.kvm_ip_addresses[0].subnet, rack.kvm_ip_addresses[0].default_gateway)
#
#
#for alarm in intersight_alarms.results:
#    #print(alarm.orig_severity)
#    #print(alarm.severity)
#    #print(alarm.owners)
#    #print(alarm.affected_mo_type)
#    #print(alarm.registered_device)
#    #print(alarm.affected_object)
#    #print(alarm.affected_mo_id)
#    #print(alarm.ancestor_mo_id)
#    
#    create_incident(alarm.description,alarm.description, 3, 2, 1, "Affected system ID: " + alarm.affected_mo_id + " with alarm code " + alarm.code)
#    #print("-----------------------")
#    
##print("####################################")
#    
#for alarm in hx_alarms.results:
#    #print(alarm.account_moid)
#    #print(alarm.ancestors)
#    #print(alarm.cluster)
#    #print(alarm.entity)
#    #print(alarm.key)
#    #print(alarm.moid)
#    #print(alarm.mor)
#    #print(alarm.parent)
#    create_incident(alarm.description,alarm.description, 3, 2, 1, "Cluster: " + alarm.entity_name)
#    #print("-----------------------")