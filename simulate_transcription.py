import roadrunner as rr

r = rr.RoadRunner('transcription_sbml.xml')

r.setIntegrator('gillespie')

print(r.getReactionRates())

res = r.simulate(0,1,10, ['time', 'ATP', 'GTP', 'CTP', 'UTP'])

r.plot()
print(res)