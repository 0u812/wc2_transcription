import roadrunner as rr

r = rr.RoadRunner('../model/rnadecay_sbml.xml')

r.setIntegrator('gillespie')
res = r.simulate(0,10,10)
#r.plot()
print(res)
