from infosync import controller

c = controller()

#1 Register all used adapters
c.register_adapter('servicenow')
print c.get_adapters()
c.register_adapter('intersight')
print c.get_adapters()

#2 Set up transformation rules
#....
print c.get_rules()

#3 Start loop
c.start()