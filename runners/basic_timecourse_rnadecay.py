import roadrunner as rr

r = rr.RoadRunner('../model/rnadecay_sbml.xml')

r.setIntegrator('gillespie')

print(r.getReactionRates())

r.getIntegrator().setValue('nonnegative', True)
res = r.simulate(0,10,10, ['time', 'AMP__c', 'GMP__c', 'CMP__c', 'UMP__c'])

r.plot()
print(res)
