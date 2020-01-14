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

## ------- Tool functions --------

def projection_vector_generator(index,length):
    dummmy = np.zeros(length)
    dummmy[index] = 1
    return dummmy

def sign_function(value):
    if value == 0:
        return 0
    else:
        return 1
        

## -------------------------------


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
# case 0
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 15),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 17),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 19),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 11),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])

# case 1
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,16,0,16*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 19),pu+2,uom,15,0,15*(pu+2)*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 11),pu,uom,20,0,20*pu*(100 - 0)/100,'well_num_2'])


# case 2
candidate_data.append([date(2019, 8, 3),date(2019, 8, 21),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 7),date(2019, 8, 10),int((endDate - startDate).days),date(2019, 8, 19),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 1),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 11),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 5),date(2019, 8, 9),int((endDate - startDate).days),date(2019, 8, 13),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])
candidate_data.append([date(2019, 8, 8),date(2019, 8, 12),int((endDate - startDate).days),date(2019, 8, 25),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_1'])
candidate_data.append([date(2019, 8, 9),date(2019, 8, 11),int((endDate - startDate).days),date(2019, 8, 11),pu,uom,15,0,15*pu*(100 - 0)/100,'well_num_2'])



## Find the distance between the test and the candidates
def distance_f_X(X_test,candidate_data):
    dfX = []
    dfX_sign = []
    
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

    dfX_sign.append(sign_function((X_test[0]-candidate_data[0]).days)) 
    dfX_sign.append(sign_function((X_test[1]-candidate_data[1]).days))
    dfX_sign.append(sign_function(X_test[2]-candidate_data[2]))
    dfX_sign.append(sign_function((X_test[3]-candidate_data[3]).days))
    dfX_sign.append(sign_function((X_test[4]-candidate_data[4])))
    dfX_sign.append(sign_function(int(X_test[5] != candidate_data[5]))) # the reason of r!= is that we want to receive 0 for the equalance
    dfX_sign.append(sign_function(X_test[6]-candidate_data[6]))
    dfX_sign.append(sign_function(X_test[7]-candidate_data[7]))
    dfX_sign.append(sign_function(X_test[8]-candidate_data[8]))
    dfX_sign.append(sign_function(int(X_test[9] != candidate_data[9])))
    return np.asarray(dfX), np.asarray(dfX_sign)



# This is where we find the array type distance between the test data and all the candidates

dfX = np.zeros((len(candidate_data),len(candidate_data[0])))
dfX_sign = np.zeros((len(candidate_data),len(candidate_data[0])))
for i in range(len(candidate_data)):
    dfX[i,:], dfX_sign[i,:]  = distance_f_X(X_test,candidate_data[i])

# print(dfX)

# print(dfX_sign)

## ------- OUTPUT matrix --------------

output = np.zeros((len(candidate_data),3))


## -------------------------------------
Major_classes = {}
Major_vector_classes = {}

## ---------- class zero (same date and same total) ------------###

Major_classes[0] = np.matrix([[1,0,0,0,0,0,0,0],
                          [0,1,0,0,0,0,0,0],
                          [0,0,1,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,1,0,0,0,0],
                          [0,0,0,0,1,0,0,0],
                          [0,0,0,0,0,1,0,0],
                          [0,0,0,0,0,0,1,0],
                          [0,0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,0,0]])
Major_vector_classes[0] = np.array([0,0,0,0,0,0,0,0])

# ## ---------- class one (same date and different total) ------------###
Major_classes[1] = np.matrix([[1,0,0,0],
                              [0,1,0,0],
                              [0,0,1,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,1],
                              [0,0,0,0]])
Major_vector_classes[1] = np.array([0,0,0,1])

# ## ---------- class two (different date and same total) ------------###
Major_classes[2] =  np.matrix([[1,0,0,0,0,0,0,0],
                               [0,1,0,0,0,0,0,0],
                               [0,0,1,0,0,0,0,0],
                               [0,0,0,0,0,0,0,0],
                               [0,0,0,1,0,0,0,0],
                               [0,0,0,0,1,0,0,0],
                               [0,0,0,0,0,1,0,0],
                               [0,0,0,0,0,0,1,0],
                               [0,0,0,0,0,0,0,1],
                               [0,0,0,0,0,0,0,0]])

Major_vector_classes[2] = np.array([1,1,1,0,0,0,0,0])

## ==============================================================================
##================================== Analysis ===================================
## ==============================================================================

for i in range(dfX_sign.shape[0]):
    # iterate through major classes
    for j in Major_classes.keys():
        
        theta = 0
        dummy_array = np.dot(dfX_sign[i,:],Major_classes[j])
 
        # print(i,j,dummy_array)
        # print(dummy_array[0,0:3])
        if j == 0 :
            if np.linalg.norm(dummy_array,ord=2) == 0:
                output[i,j] = 1
                break
        
        if (j == 1):
            theta = np.dot(dummy_array,Major_vector_classes[j])/(np.linalg.norm(dummy_array,ord=2)*np.linalg.norm
            (Major_vector_classes[j],ord=2)) # finding the cos of theta
            if ( theta == 1): ## If the vector pattern match
                output[i,j] = 1 # This is where we identify which class of fraud is possible and selected 
                break

        if (j == 2) :
            # print(dummy_array)
            if np.linalg.norm(dummy_array[0,0:3],ord=2) != 0 and np.linalg.norm(dummy_array[0,3:],ord=2) == 0:
                output[i,j] = 1
                break
    
print(output)





