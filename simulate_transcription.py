import roadrunner as rr

r = rr.RoadRunner('transcription_sbml.xml')

r.setIntegrator('gillespie')
res = r.simulate(0,10,10, ['ATP'])
#r.plot()
print(res)