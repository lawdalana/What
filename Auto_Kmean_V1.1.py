from optparse import OptionParser
from sklearn.cluster import KMeans
import numpy as np
import sys
import codecs
import csv
import gc
from copy import deepcopy
def sort():
    global Result_value
    global novel_header
    global data
    for x in range(len(Result_value)):
        for y in range(len(Result_value)):
            if(Result_value_all[x]>Result_value_all[y]):
                Result_value_all[x], Result_value_all[y] = Result_value_all[y],Result_value_all[x]
                novel_header[x], novel_header[y] = novel_header[y], novel_header[x]
                data[x], data[y] = data[y], data[x]
                label[x], label[y] = label[y], label[x]

def process(predict, cls):
    global final
    global final_all
    global Result_value
    global Result_value_all
    
    if not Result_value_all:
        for k in range(cls):
            count = 0
            count_pls = 0
            for loop in range(len(predict)):
                if(predict[loop]==k):
                    count = count + 1
                    if(label[loop]==1):
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
                    if(label[loop]==1):
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

if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog -i <story_header.csv> -s <story_header_sell_all.csv>",
                        version="%prog 1.0")

    parser.add_option("-i", "--input",
                    action="store",
                    dest="inputfile",
                    type="string",
                    help="Filename of story_header -- type(csv)")

    parser.add_option("-s", "--sell",
                    action="store", # optional because action defaults to "store"
                    dest="inputfile_seller",
                    type="string",
                    help="Filename of story_header_sell_all -- type(csv)")

    parser.add_option("-o", "--output",
                    action="store", # optional because action defaults to "store"
                    dest="outputfile",
                    type="string",
                    default="Result.csv",
                    help="[Optional] Set output filename -- type(csv)")

    parser.add_option("-N",
                    action="store", # optional because action defaults to "store"
                    dest="Kn",
                    type="int",
                    default="11",
                    help="[Optional] Set K in kmean")

    (options, args) = parser.parse_args()

    if options.inputfile is None or options.inputfile_seller is None:
        print("python <filename.py> -i <story_header.csv> -s <story_header_sell_all.csv>")
        sys.exit(0)

    else:
        # create variable #
        novel_header = list()
        data = list()
        label = list()
        Group_filter = ["26","27","28","29","30","19"]
        final = list()
        final_all = list()
        Result_value_all = list()
        Result_value = list()
        K = options.Kn
        index = 0

        # Read file #

        with open(options.inputfile,"r+",encoding="utf8") as test:
            reader = csv.reader(test)
            for row in reader:
                if(not row[2] in Group_filter):
                    novel_header.append(row[0:-4])
                    data.append(row[-4:])
                    label.append(0)
        del novel_header[index]
        del data[index]
        del label[index]
        index = len(novel_header)

        # Read file Seller#
        with open(options.inputfile_seller,"r+",encoding="utf8") as test:
            reader = csv.reader(test)
            for row in reader:
                novel_header.append(row[0:-4])
                data.append(row[-4:])
                label.append(1)
        del novel_header[index]
        del data[index]
        del label[index]

        # Normalize #
        Trans = np.asarray(data).T.tolist()
        Max_value = [float(max(Trans[0])), float(max(Trans[1])), float(max(Trans[2])), float(max(Trans[3]))]
        Min_value = [float(min(Trans[0])), float(min(Trans[1])), float(min(Trans[2])), float(min(Trans[3]))]
        dif_value = [Max_value[0]-Min_value[0], Max_value[1]-Min_value[1], Max_value[2]-Min_value[2], Max_value[3]-Min_value[3]]
        datax = deepcopy(data)
        for i in range(len(data)):
            datax[i][0] = (float(datax[i][0]) - Min_value[0]) / dif_value[0]
            datax[i][1] = (float(datax[i][1]) - Min_value[1]) / dif_value[1]
            datax[i][2] = (float(datax[i][2]) - Min_value[2]) / dif_value[2]
            datax[i][3] = (float(datax[i][3]) - Min_value[3]) / dif_value[3]
        del Trans
        del Min_value
        del Max_value
        del dif_value
        gc.collect()

        # convert data to array
        train_data = np.asarray(datax)

        for i in range(2,K):
            print("Clustering Kmean model ---- K = ",i)
            kmeans = KMeans(n_clusters=i, max_iter=500 ,random_state=0).fit(train_data)
            result = kmeans.labels_
            result = result.tolist()
            process(result, i)
            print("Clustering K = ",i," Success!")
        sort()

        with codecs.open(options.outputfile,"w","utf-8") as test:
            for i in range(0,len(Result_value_all)):
                if(label[i]==0):
                    head = ",".join(novel_header[i])
                    body = ",".join(data[i])
                    buf = str(head)+","+str(body)+","+str(Result_value_all[i])+"\n"
                    test.write(buf)

        print("Successful!")
        gc.collect()
        sys.exit(0)