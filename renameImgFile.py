import os

originalPath = "/Users/svenduve/HiDrive/vetData/HH_Pigment"


for i, el in enumerate(os.listdir(originalPath)):
    orgFile = os.path.join(originalPath, el)
    renamedFile = os.path.join(originalPath, "pigment_" + str(1000000 + i) + ".JPG")
    os.rename(orgFile, renamedFile)
    
    


