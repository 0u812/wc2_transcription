import roadrunner as rr

r = rr.RoadRunner('../model/transcription_sbml.xml')

r.setIntegrator('gillespie')

print(r.getReactionRates())

r.getIntegrator().setValue('nonnegative', True)
res = r.simulate(0,10,10, ['time', 'ATP__c', 'GTP__c', 'CTP__c', 'UTP__c'])

r.plot()
print(res)
