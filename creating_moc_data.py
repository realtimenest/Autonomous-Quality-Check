import numpy as np
import pandas as pd
import time
from datetime import date


##   Service line item properties:
# 1- serviceName 
# 2- serviceCode 
# 3- startDate (x1)
# 4- endDate (x2)
# 5- jobDuration (x3)
# 6- submissionDate (x4)
# 7- pu (x5)
# 8- uom (x6)
# 9- quantity (x7)
# 10- discount (x8)
# 11- total (x9)
# 12- assignedWell
# 13 - project


## Create a sample service information
startDate = date(2019, 8, 7)
endDate = date(2019, 8, 11)
duration  = int((endDate - startDate).days)
submission = date(2019, 8, 13)
pu = 120
uom = 'days'
quantity = 15
discount = 0
total = quantity*pu*(100 - discount)/100
well = 'well_num_1'


X_test = [startDate,endDate,duration,submission,pu,uom,quantity,discount,total,well]

candidate_data = []
# case 1
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 15),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 17),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 19),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 11),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])

# case 2

## Find the distance between the test and the candidates
def distance_f_X(X_test,candidate_data):
    dfX = []
    
    dfX.append((X_test[0]-candidate_data[0]).days) 
    dfX.append((X_test[1]-candidate_data[1]).days)
    dfX.append(X_test[2]-candidate_data[2])
    dfX.append((X_test[3]-candidate_data[3]).days)
    dfX.append((X_test[4]-candidate_data[4]))
    dfX.append(int(X_test[5] != candidate_data[5])) # the reason of r!= is that we want to receive 0 for the equalance
    dfX.append(X_test[6]-candidate_data[6])
    dfX.append(X_test[7]-candidate_data[7])
    dfX.append(X_test[8]-candidate_data[8])
    dfX.append(int(X_test[9] != candidate_data[9]))
    return dfX





dfX = []
for i in range(len(candidate_data)):
    dfX.append(distance_f_X(X_test,candidate_data[i]))

print(dfX)


## ---------- class one (same date and same total) ------------###
cv1 = np.array([1,1,1,0,1,1,1,1,1,0,0,0])

# write a matrix that only returns those variables that are important for this scenario. MAybe this is not the best way because we need to eventually know whic variables are similar or not similar and report the result, therefore think about it.


## ---------- class two (same date and same total) ------------###
cv1 = np.array([1,1,1,0,0,0,0,0,1,0,0,0])


## ---------- class three (same date and same total) ------------###
cv1 = np.array([1,1,1,0,1,1,1,1,1,0,0,0])










