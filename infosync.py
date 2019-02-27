import yaml



class controller:
    def __init__(self, config='./credentials.yaml'):
        self.config = config
        config_file = open(self.config,"r")
        config_file = yaml.load(config_file.read())
        print config_file
        
    