# -*- coding: utf-8 -*-


from __future__ import print_function
print(__doc__)

import numpy as np
import sys,csv

sys.path.append('./py_files')


from SPAH4_metric import SPAH4
from figures import plot_SPAH4stats, plot_maps


mask_1km = np.loadtxt('./map_files/mask_1km.asc', delimiter=',')   # X is an array

dpi = 60 # Arbitrary. The number of pixels in the image will always be identical
height, width = [12,18]#np.array(aET_sim.shape, dtype=float) / dpi
font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }

obs=[]
sim=[]
############################################################ EXAMPLE: descent monthly match
obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_1.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]

Spah4_1, alpha1, beta1, gamma1, kappa1 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_1, alpha1, beta1, gamma1, kappa1, 'Case-1') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map1map') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case1',Spah4_1)

############################################################ EXAMPLE: better monthly match

obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_2.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]


Spah4_2, alpha2, beta2, gamma2, kappa2 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_2, alpha2, beta2, gamma2, kappa2,'Case-2') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map2map') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case2',Spah4_2)

############################################################ EXAMPLE: poor match
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_3.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]

   
Spah4_3, alpha3, beta3, gamma3, kappa3 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_3, alpha3, beta3, gamma3, kappa3,'Case-3') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map3map') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case3',Spah4_3)



############################################################ EXAMPLE: poor match
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_4.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]


Spah4_4, alpha4, beta4, gamma4, kappa4 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_4, alpha4, beta4, gamma4, kappa4,'Case-4') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map4map') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case4',Spah4_4)


############################################################ EXAMPLE: poor match
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_5.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]



Spah4_5, alpha5, beta5, gamma5, kappa5 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_5, alpha5, beta5, gamma5, kappa5,'Case-5shifted') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map5-shifted') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case5',Spah4_5)


############################################################ EXAMPLE: shifted cells
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_6.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]

Spah4_6, alpha6, beta6, gamma6, kappa6 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_6, alpha6, beta6, gamma6, kappa6,'Case-6') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map6map') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case6',Spah4_6)



############################################################ EXAMPLE: biased sim=obsx30 times greater values, locations unchanged
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/sim_shuffled.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=simm[np.isnan(obss)==False]


Spah4_7, alpha7, beta7, gamma7, kappa7 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_7, alpha7, beta7, gamma7, kappa7,'Case-7shuffled') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map7-shuffled') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case7',Spah4_7)



############################################################ EXAMPLE: biased sim=obs x 1.4 times greater values, locations unchanged
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/obs.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=obss*1.4


Spah4_8, alpha8, beta8, gamma8, kappa8 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_8, alpha8, beta8, gamma8, kappa8,'Case-8biased40%') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map8-biased40%') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case8',Spah4_8)

############################################################ EXAMPLE: add biased sim=obs+2 constant bias added, locations unchanged
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/obs.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=obss+2


Spah4_9, alpha9, beta9, gamma9, kappa9 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_9, alpha9, beta9, gamma9, kappa9,'Case-9PLUS2') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map9-PLUS2') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case9',Spah4_9)



############################################################ EXAMPLE: add biased sim=obs^2 (SQUARED) constant bias added, locations unchanged, the need for SPEERMAN
obs=[]
sim=[]
obss=[]
simm=[]

obs=np.loadtxt('./map_files/obs.asc')   
sim=np.loadtxt('./map_files/obs.asc') 

obs[mask_1km==0]=np.nan
sim[mask_1km==0]=np.nan

notnan=np.argwhere(np.isnan(obs)==False)

obss=obs[notnan[:,0],notnan[:,1]]  
simm=sim[notnan[:,0],notnan[:,1]]

obss=obss[np.isnan(obss)==False]
simm=obss**2


Spah4_10, alpha10, beta10, gamma10, kappa10 = SPAH4(simm,obss)
########################################################################        PLOT   MAPS and STATS

plot_SPAH4stats(simm,obss,Spah4_10, alpha10, beta10, gamma10, kappa10,'Case-10SQUARED') # first two inputs should be 1D vector

plot_maps(sim,obs,'Map10-SQUARED') # first two inputs should be 2D matrix (not vector)

print ('SPAH4_case10',Spah4_10)



val=np.array([['ID','SPAH4'],['Case1',np.around(Spah4_1,7)],['Case2',np.around(Spah4_2,7)],['Case3',np.around(Spah4_3,7)],['Case4',np.around(Spah4_4,7)],['Case5',np.around(Spah4_5,7)],['Case6',np.around(Spah4_6,7)],['Case7',np.around(Spah4_7,7)],['Case8',np.around(Spah4_8,7)],['Case9',np.around(Spah4_9,7)],['Case10',np.around(Spah4_10,7)]])


csvfile = "SPAH4_results.out"

#Assuming res is a flat list
with open('./results/'+csvfile, "w") as output:
    writer = csv.writer(output,delimiter =' ', lineterminator='\n')
    for val in val:
        writer.writerow(val) 
        
### 
output.close()








print ('Welldone')

#sys.modules[__name__].__dict__.clear()



