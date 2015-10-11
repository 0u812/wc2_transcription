import roadrunner as rr

r = rr.RoadRunner('../model/transcription_sbml.xml')

r.setIntegrator('gillespie')

print(r.getReactionRates())

r.getIntegrator().setValue('nonnegative', True)
res = r.simulate(0,10,10, ['time', 'ATP', 'GTP', 'CTP', 'UTP'])

#r.plot()
print(res)
