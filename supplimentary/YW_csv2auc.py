import csv
import numpy as np
import sys
import glob

if sys.argv[1]:
    modelnum = int(sys.argv[1])
else:
    modelnum = 27

dir00 = '/home/yiwangtamu/HatefulMemes/predict/'
#f0 = 'save-0/hateful_memes_visual_bert_19674856/reports/hateful_memes_run_test_2021-05-05T22-19-51.csv'
f1 = 'save-18/hateful_memes_visual_bert_23185843/reports/hateful_memes_run_test_2021-05-05T22-25-55.csv'
f2 = 'save-19/hateful_memes_visual_bert_59437955/reports/hateful_memes_run_test_2021-05-05T22-26-31.csv'
f3 = 'save-8/hateful_memes_visual_bert_21513793/reports/hateful_memes_run_test_2021-05-05T22-22-53.csv'
f4 = 'save-16/hateful_memes_visual_bert_47074313/reports/hateful_memes_run_test_2021-05-05T22-25-19.csv'
f5 = 'save-7/hateful_memes_visual_bert_44229591/reports/hateful_memes_run_test_2021-05-05T22-22-17.csv'
f6 = 'save-21/hateful_memes_visual_bert_36039655/reports/hateful_memes_run_test_2021-05-05T22-27-08.csv'
f7 = 'save-6/hateful_memes_visual_bert_8173356/reports/hateful_memes_run_test_2021-05-05T22-21-40.csv'
f8 = 'save-15/hateful_memes_visual_bert_10359680/reports/hateful_memes_run_test_2021-05-05T22-24-42.csv'
f9 = 'save-0/hateful_memes_visual_bert_19674856/reports/hateful_memes_run_test_2021-05-05T22-19-51.csv'
f10 = 'save-2/hateful_memes_visual_bert_56173567/reports/hateful_memes_run_test_2021-05-05T22-20-28.csv'
f11 = 'save-9/hateful_memes_visual_bert_58533091/reports/hateful_memes_run_test_2021-05-05T22-33-30.csv'
f12 = 'save-20/hateful_memes_visual_bert_6854139/reports/hateful_memes_run_test_2021-05-05T22-36-38.csv'
f13= 'save-13/hateful_memes_visual_bert_33782778/reports/hateful_memes_run_test_2021-05-05T22-24-06.csv'
f14 = 'save-23/hateful_memes_visual_bert_43169235/reports/hateful_memes_run_test_2021-05-05T22-37-15.csv'
f15 = 'save-17/hateful_memes_visual_bert_30875404/reports/hateful_memes_run_test_2021-05-05T22-36-02.csv'
f16 = 'save-22/hateful_memes_visual_bert_12653335/reports/hateful_memes_run_test_2021-05-05T22-27-44.csv'
f17 = 'save-1/hateful_memes_visual_bert_8173031/reports/hateful_memes_run_test_2021-05-05T22-31-40.csv'
f18 = 'save-11/hateful_memes_visual_bert_34994315/reports/hateful_memes_run_test_2021-05-05T22-34-10.csv'
f19 = 'save-24/hateful_memes_visual_bert_20571530/reports/hateful_memes_run_test_2021-05-05T22-37-53.csv'
f20 = 'save-5/hateful_memes_visual_bert_21452522/reports/hateful_memes_run_test_2021-05-05T22-32-54.csv'
f21 = 'save-25/hateful_memes_visual_bert_57529238/reports/hateful_memes_run_test_2021-05-05T22-38-30.csv'
f22 = 'save-26/hateful_memes_visual_bert_48704705/reports/hateful_memes_run_test_2021-05-05T22-28-20.csv'
f23 = 'save-14/hateful_memes_visual_bert_53240255/reports/hateful_memes_run_test_2021-05-05T22-35-26.csv'
f24 = 'save-12/hateful_memes_visual_bert_15030536/reports/hateful_memes_run_test_2021-05-05T22-34-48.csv'
f25 = 'save-4/hateful_memes_visual_bert_44645910/reports/hateful_memes_run_test_2021-05-05T22-32-17.csv'
f26 = 'save-3/hateful_memes_visual_bert_32454834/reports/hateful_memes_run_test_2021-05-05T22-21-03.csv'
f27 = 'save-10/hateful_memes_visual_bert_57667120/reports/hateful_memes_run_test_2021-05-05T22-23-29.csv'

list00 = []
listid1 = []
filelist = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27]

xx = glob.glob(dir00+'save-18/*/reports/*.csv')
#print(xx)
a = np.loadtxt(xx[0],comments='#',delimiter=',')
for i in range(len(a)):
    list00.append(a[i][2])
    listid1.append(a[i][0])

for ifile in range(1,modelnum):
    a = np.loadtxt(dir00+filelist[ifile], comments='#', delimiter=',')
    for i in range(len(a)):
#        print(list00[i])
        list00[i] = list00[i] + a[i][2]# * 0.8**(ifile)
#        print(list00[i],a[i][2], 0.8**(ifile))
#print(list00)
    
import csv
list11 = []
listid0 = []
with open('dev_unseen.jsonl') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        list11.append(row[2][-1])
        listid0.append(row[0])
        line_count += 1

#print(list11)
#print(len(list00),len(list11))
list00.pop(477)

for i in range(len(list00)):
    if list00[i] > int(modelnum / 5):
        list00[i] = 1
    else:
        list00[i] = 0
    list00[i] = int(list00[i])
    list11[i] = int(list11[i])

#print(min(list00),max(list00))
#print(min(list11),max(list11))
#print(list00)
#list00 = list00[:400]
#list11 = list11[:400]

#for i in range(400,540):
#    print(i,listid0[i],list11[i],listid1[i],list00[i])

from collections import Counter
#print(Counter(list11))
import numpy as np
from sklearn import metrics

fpr, tpr, thresholds = metrics.roc_curve(list11[:-1], list00[:-1])#, pos_label=2)
print(metrics.auc(fpr, tpr))


