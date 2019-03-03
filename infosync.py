import yaml
from jsondiff import diff
import time
import copy


class controller:
    def __init__(self, config='./credentials.yaml'):
        config_file = open(config,"r")
        self.config = yaml.load(config_file.read())
        self.adapters = []
        self.rules = []
        
        #1 Register all used adapters
        for x in self.config:
            self.register_adapter(x)
        
    def get_adapters(self):
        return self.adapters
     
    def register_adapter(self, type):
        if type == 'intersight':
            import c_intersight
            self.adapters.append(c_intersight.connector(api_key=self.config['intersight']['apikey'],keyfile=self.config['intersight']['keyfile']))
        
        if type == 'servicenow':
            import c_servicenow
            self.adapters.append(c_servicenow.connector(instance=self.config['servicenow']['instance'],user=self.config['servicenow']['user'],pwd=self.config['servicenow']['pwd']))
            
            
    def add_rule(self, connector, group, change_type, function):
        self.rules.append({
            'connector': connector,
            'group': group,
            'change_type': change_type,
            'function': function
        })
        
    def get_rules(self):
        return self.rules
    
    def start(self):
        while True:
            changes = []
            
            #4 Loop pulls data from all platforms
            current_adapter = 0
            for a in self.adapters:
                state = 'Pulling data for adapters: ' + str(current_adapter) + '/' + str(len(self.adapters)) + ' done'
                print (state, end="\r")
                
                a.pull_all()

                #5 Loop does comparisons of new vs old data and determines the differences
                current = copy.deepcopy(a.current_state) 
                previous = a.previous_state
                for elem in a.current_state:
                    for x in a.current_state[elem]:
                        if x not in a.previous_state[elem]:
                            changes.append({
                                'change_type': 'ADD',
                                'connector': a.type,
                                'group': elem,
                                'data': x
                            })
                            
                    for x in a.previous_state[elem]:
                        if x not in a.current_state[elem]:
                            changes.append({
                                'change_type': 'DELETE',
                                'connector': a.type,
                                'group': elem,
                                'data': x
                            })
                            
                current_adapter += 1


            current_change = 0
            #6 Differences are sent through transformation rules
            for change in changes:
                state = 'Processing Changes: ' + str(current_change) + '/' + str(len(changes)) + ' done          '
                print (state, end="\r")
                for rule in self.rules:
                    if change['change_type'] == rule['change_type'] and change['connector'] == rule['connector'] and change['group'] == rule['group']:
                        rule['function'](change['data'])
                    
                current_change += 1
        
            state = 'Processing Changes: ' + str(current_change) + '/' + str(len(changes)) + ' done'
            print (state, end="\r")
            time.sleep(2)
            print ('All changes processed, sleeping for 60 seconds', end="\r")
            time.sleep(58)