import numpy as np
from datetime import date
import pandas as pd

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
# 13 - projectid
# 14- service_ccid


## ------- Tool functions --------

def loadList(filename):
    # the filename should mention the extension 'npy'
    tempNumpyArray=np.load(filename)
    return tempNumpyArray.tolist()




def projection_vector_generator(index,length):
    dummmy = np.zeros(length)
    dummmy[index] = 1
    return dummmy

def sign_function(value):
    if value == 0:
        return int(0)
    else:
        return int(1)
        

## ------------------------------------------------------------------------##
## ----------- Create a sample service data for analysis-------------------##
## ------------------------------------------------------------------------##

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

# This is the service under analysis
X_test = [startDate,endDate,duration,submission,pu,uom,quantity,discount,total,well]
# This is where we load the potential candidates, the result of this should be coming to the python batch using the sql queries in the future in INVOICE
candidate_data = loadList('potentialCandidates.npy')





## Find the distance between the test and the candidates
def distance_f_X(X_test,candidate_data):
    dfX = []
    dfX_sign = []
    
    # dfX.append((X_test[0]-candidate_data[0]).days) 
    # dfX.append((X_test[1]-candidate_data[1]).days)
    # dfX.append(X_test[2]-candidate_data[2])
    # dfX.append((X_test[3]-candidate_data[3]).days)
    # dfX.append((X_test[4]-candidate_data[4]))
    # dfX.append(int(X_test[5] != candidate_data[5])) # the reason of r!= is that we want to receive 0 for the equalance
    # dfX.append(X_test[6]-candidate_data[6])
    # dfX.append(X_test[7]-candidate_data[7])
    # dfX.append(X_test[8]-candidate_data[8])
    # dfX.append(int(X_test[9] != candidate_data[9]))

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
    return np.asarray(dfX_sign)



# This is where we find the array type distance between the test data and all the candidates

# dfX = np.zeros((len(candidate_data),len(candidate_data[0])))
dfX_sign = np.zeros((len(candidate_data),len(candidate_data[0])))
for i in range(len(candidate_data)):
    dfX_sign[i,:]  = distance_f_X(X_test,candidate_data[i])

# print(dfX)

# print(dfX_sign)

## ------- OUTPUT matrix --------------

Major_class_output = np.zeros((len(candidate_data)))
Minor_class_output = np.zeros((len(candidate_data)))

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


### =============================================================================
### ====================== Read minor fraud class paterns =======================
### =============================================================================
# xls = pd.ExcelFile('Potential_fraud_classes.xls')
# sheetname = xls.sheet_names
# print(sheetname)

Minor_excell_file = {}
Minor_excell_file[0] =  pd.read_excel('Potential_fraud_classes.xls',sheet_name='0').values
Minor_excell_file[1] =  pd.read_excel('Potential_fraud_classes.xls',sheet_name='1').values
Minor_excell_file[2] =  pd.read_excel('Potential_fraud_classes.xls',sheet_name='2').values

# print(Minor_excell_file[2])






## ==============================================================================
## ================================== Analysis ===================================
## ==============================================================================

for i in range(dfX_sign.shape[0]):  # loop through all the candidates
    
    # iterate through major classes
    for j in Major_classes.keys():  # loop throughh the major fraud classes
 
        dummy_array = np.dot(dfX_sign[i,:],Major_classes[j])
 
        ## -------- Major class 0 -------- ##
        if (j == 0) :
            if np.linalg.norm(dummy_array,ord=2) == 0:
                Major_class_output[i] = j
                ## Identify the correct minor class for this major
                for minor in range(Minor_excell_file[j].shape[0]):  # loop throught the minor classes
                    
                    if (dfX_sign[i,:] == Minor_excell_file[j][minor,0:len(Minor_excell_file[j][0])-2]).all():
                        Minor_class_output[i] = minor
                        break
                    else:
                        Minor_class_output[i] = -100
                        
            

        ## -------- Major class 1 -------- ##
        elif (j == 1):
            if ( np.linalg.norm(dummy_array[0,0:3],ord=2) == 0 and dummy_array[0,3] == 1): ## If the vector pattern match
                Major_class_output[i] = j # This is where we identify which class of fraud is possible and selected 
                ## Identify the correct minor class for this major
                for minor in range(Minor_excell_file[j].shape[0]):  # loop throught the minor classes

                    if (dfX_sign[i,:] == Minor_excell_file[j][minor,0:len(Minor_excell_file[j][0])-2]).all():
                        Minor_class_output[i] = minor
                        break
                    else:
                        Minor_class_output[i] = -200
                
 

        ## -------- Major class 2 -------- ##
        elif (j == 2) :
            if np.linalg.norm(dummy_array[0,0:3],ord=2) != 0 and np.linalg.norm(dummy_array[0,3:],ord=2) == 0:
                # print('dfX_sign==>',dfX_sign[i,:])
                Major_class_output[i] = j
                ## Identify the correct minor class for this major
                for minor in range(Minor_excell_file[j].shape[0]):  # loop throught the minor classes

                    if (dfX_sign[i,:] == Minor_excell_file[j][minor,0:len(Minor_excell_file[j][0])-2]).all():
                        Minor_class_output[i] = minor
                        break
                    else:
                        Minor_class_output[i] = -300


        else:
            Major_class_output[i] = -1
            Minor_class_output[i] = -1

    
print('Major_class_output ===>',Major_class_output)
print('Minor_class_output ===>',Minor_class_output)





