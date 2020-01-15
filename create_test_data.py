import numpy as np
from datetime import date



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







def saveList(myList,filename):
    # the filename should mention the extension 'npy'
    np.save(filename,myList)
    print("Saved successfully!")

saveList(candidate_data, 'potentialCandidates.npy')



