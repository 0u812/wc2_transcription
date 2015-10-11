import roadrunner as rr
import mass_list as mass

r = rr.RoadRunner('../model/transcription_sbml.xml')

r.setIntegrator('gillespie')

#print(r.getReactionRates())

r.getIntegrator().setValue('nonnegative', True)

H2O_initial = r.H2O
ATP_initial = r.ATP
GTP_initial = r.GTP
CTP_initial = r.CTP
UTP_initial = r.UTP
H_initial = r.H
#OH_initial = r.OH
PPI_initial = r.PPI

res = r.simulate(0,1,3, ['time', 'ATP', 'GTP', 'CTP', 'UTP'])

H2O_final = r.H2O
ATP_final = r.ATP
GTP_final = r.GTP
CTP_final = r.CTP
UTP_final = r.UTP
H_final = r.H
#OH_final = r.OH
PPI_final = r.PPI

H2O_delta = H2O_final - H2O_initial
ATP_delta = ATP_final - ATP_initial
GTP_delta = GTP_final - GTP_initial
CTP_delta = CTP_final - CTP_initial
UTP_delta = UTP_final - UTP_initial
H_delta = H_final - H_initial
#OH_delta = OH_final - OH_initial
PPI_delta = PPI_final - PPI_initial

print('Initial H2O: {}'.format(H2O_initial))
print('Final H2O: {}'.format(H2O_final))
print('Change in H2O: {}'.format(H2O_delta))
print('Change in ATP: {}'.format(ATP_delta))
print('Change in GTP: {}'.format(GTP_delta))
print('Change in CTP: {}'.format(CTP_delta))
print('Change in UTP: {}'.format(UTP_delta))
print('Change in H: {}'.format(H_delta))
#print('Change in OH: {}'.format(OH_delta))
print('Change in PPI: {}'.format(PPI_delta))

#r.plot()
print(res)
