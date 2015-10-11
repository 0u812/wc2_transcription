import roadrunner as rr

r = rr.RoadRunner('transcription_sbml.xml')

r.setIntegrator('gillespie')

print(r.getReactionRates())

res = r.simulate(0,10,10, ['ATP', 'RNA_POLYMERASE'])

#r.plot()
print(res)