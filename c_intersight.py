import intersight
from intersight.intersight_api_client import IntersightApiClient

class connector:
    def __init__(self, api_key, keyfile):
        self.type = 'Intersight'
        
        api_instance = IntersightApiClient(
            private_key=keyfile,
            api_key_id=api_key
        )
       
        self.NetworkElementApi = intersight.NetworkElementApi(api_instance)
        self.ComputeRackUnitApi = intersight.ComputeRackUnitApi(api_instance)
        self.HyperflexClusterApi = intersight.HyperflexClusterApi(api_instance)
        self.CondAlarmApi = intersight.CondAlarmApi(api_instance)
        self.HyperflexAlarmApi = intersight.HyperflexAlarmApi(api_instance)
        
        self.current_state = {
            'network_elements': [],
            'compute_rack_units': [],
            'hyperflex_clusters': [],
            'cond_alarms': [],
            'hyperflex_alarms': []
        }
        self.previous_state = {
            'network_elements': [],
            'compute_rack_units': [],
            'hyperflex_clusters': [],
            'cond_alarms': [],
            'hyperflex_alarms': []
        }
    
    def pull_all(self):
        self.previous_state = self.current_state
        self.current_state = {
            'network_elements': self.NetworkElementApi.network_elements_get().results,
            'compute_rack_units': self.ComputeRackUnitApi.compute_rack_units_get().results,
            'hyperflex_clusters': self.HyperflexClusterApi.hyperflex_clusters_get().results,
            'cond_alarms': self.CondAlarmApi.cond_alarms_get().results,
            'hyperflex_alarms': self.HyperflexAlarmApi.hyperflex_alarms_get().results
        }