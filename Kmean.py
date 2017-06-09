from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
import numpy as np
import sys
import os.path
## Check Args ##
try:
    Args = sys.argv
    if(len(Args)!=3):
        raise EnvironmentError
except:
    print("Error !!")
    print("Plese add 2 arguments {file:Story_header} {file:Story_header_seller}\n")
    exit()

#### Read file ####
novel_header = list()
data = list()
label = list()
Group_filter = ["26","27","28","29","30","19"]
check = ""
with open(Args[1],"r+",encoding="utf8") as test:
    for i in test:
        i = i.replace("\n","")
        ckeck = check + i 
        buf = ckeck.split(",")
        if(len(buf)==45):
            check = ""
            if(not buf[4] in Group_filter):
                bf = []
                bf.append(buf[21])
                bf.append(buf[0])
                bf.append(buf[3])
                bf.append(buf[4])
                novel_header.append(bf)
                bf = []
                bf.append(buf[9])
                bf.append(buf[10])
                bf.append(buf[17])
                bf.append(buf[27])
                data.append(bf)
                bf = []
                if(buf[42]=="0" and buf[43]=="0"):
                    label.append("0")
                else:
                    label.append("1")
        else:
            check = check + i


with open(Args[2],"r+",encoding="utf8") as test:
    for i in test:
        i = i.replace("\n","")
        ckeck = check + i 
        buf = ckeck.split(",")
        if(len(buf)==45):
            check = ""
            if(not buf[4] in Group_filter):
                bf = []
                bf.append(buf[21])
                bf.append(buf[0])
                bf.append(buf[3])
                bf.append(buf[4])
                novel_header.append(bf)
                bf = []
                bf.append(buf[9])
                bf.append(buf[10])
                bf.append(buf[17])
                bf.append(buf[27])
                data.append(bf)
                bf = []
                if(buf[42]=="0" and buf[43]=="0"):
                    label.append("0")
                else:
                    label.append("1")
        else:
            check = check + i

del novel_header[0]
del data[0]
del label[0]
#########################################################
################# function ##############################
#########################################################
def sort():
    global Result_value
    global novel_header
    global data
    global label
    global train_data
    for x in range(len(Result_value)):
        for y in range(len(Result_value)):
            if(Result_value_all[x]>Result_value_all[y]):
                Result_value_all[x], Result_value_all[y] = Result_value_all[y],Result_value_all[x]
                novel_header[x], novel_header[y] = novel_header[y], novel_header[x]
                data[x], data[y] = data[y], data[x]
                label[x], label[y] = label[y], label[x]
                train_data[x], train_data[y] = train_data[y], train_data[x] 
                
def process(predict, cls):
    global final
    global final_all
    global Result_value_all
    global Result_value
    if not Result_value_all:
        for k in range(cls):
            count = 0
            count_pls = 0
            for loop in range(len(predict)):
                if(predict[loop]==k):
                    count = count + 1
                    if(label[loop]=="1"):
                        count_pls = count_pls + 1
            final.append(count_pls)
            final_all.append(count)
            buffer = list()
        for k in range(len(predict)):
            val = (float(final[predict[k]])/float(final_all[predict[k]]))*(1-(float(final_all[predict[k]])/len(train_data)))
            Result_value_all.append(val)
            buffer.append(val)
        Result_value.append(buffer)
        final = list()
        final_all = list()
    else:
        for k in range(cls):
            count = 0
            count_pls = 0
            for loop in range(len(predict)):
                if(predict[loop]==k):
                    count = count + 1
                    if(label[loop]=="1"):
                        count_pls = count_pls + 1
            final.append(count_pls)
            final_all.append(count)
            buffer = list()
        for k in range(len(predict)):
            val = (float(final[predict[k]])/float(final_all[predict[k]]))*(1-(float(final_all[predict[k]])/len(train_data)))
            buffer.append(val)
            if(val>Result_value_all[k]):
                Result_value_all[k] = val
                
        Result_value.append(buffer)
        final = list()
        final_all = list()
        
################################################
####################  Main  ####################
################################################

final = list()
final_all = list()
Result_value_all = list()
Result_value = list()
sep = list()
train_data = np.asarray(data)
ite = 11


for i in range(2,ite):
    kmeans = KMeans(n_clusters=i, max_iter=500 ,random_state=0).fit(train_data)
    result = kmeans.labels_
    result = result.tolist()
    process(result, i)
    sort()
with open("Result.csv","w") as test:
    for i in range(0,len(Result_value_all)):
        head = ",".join(novel_header[i])
        buf = str(head)+","+str(Result_value_all[i])+"\n"
        test.write(buf)

