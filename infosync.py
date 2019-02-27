import yaml


class controller:
    def __init__(self, config='./credentials.yaml'):
        config_file = open(config,"r")
        self.config = yaml.load(config_file.read())
        self.adapters = []
        self.rules = []
        
    def get_adapters(self):
        return self.adapters
     
    def register_adapter(self, type):
        if type == 'intersight':
            import c_intersight
            x = c_intersight.connector(apikey=self.config['intersight']['apikey'],keyfile=self.config['intersight']['keyfile'])
            self.adapters.append(x)
        
        if type == 'servicenow':
            import c_servicenow
            x = c_servicenow.connector(instance=self.config['servicenow']['instance'],user=self.config['servicenow']['user'],pwd=self.config['servicenow']['pwd'])
            self.adapters.append(x)
            
            
    def add_rule(self, x):
        print x
        
    def get_rules(self):
        return self.rules
    
    def start(self):
        print 'Continuously fetching data'
        
        #4 Loop pulls data from all platforms
        for a in self.adapters:
            print a
            #5 Loop does comparisons of new vs old data and determines the differences
        
        
        #6 Differences are sent through transformation rules
        
        
        #7 Transformed differences are pushed to connector based on configured target
        