import pandas as pd
import glob
import os
import re
from ckiptagger import WS, POS, NER


csv=pd.read_excel('D:/ntu content/Keywords/02chem.list.xlsx',header=None,keep_default_na=False)
data={}
words=[]
words1=[]
count=0
full_punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' + '→↓△▿⋄•！？?〞＃＄％＆』（）＊＋，－╱︰；＜＝＞＠〔╲〕 ＿ˋ｛∣｝∼、〃》「」『』【】﹝﹞【】〝〞–—『』「」…﹏'

for i in range(len(csv)):
    words=[]
    count+=1
    for j in csv:
        if csv[j][i]!='':
            words.append(csv[j][i])
    words1.append(words)
    #data={words[0]:words}
print(words1)
'''
c=[]
text1=[]
text2=[]
path='D:/ntu content/dataTrainComplete/'
files=os.listdir(path)
for f in files:
    f=re.sub("\D", "", f)
    c.append(f)
c_1=sorted(list(map(int, c)))
new_files=[(str(i)+'.txt') for i in c_1]
res='output.txt'
for i in new_files:
    text=pd.read_csv('D:/ntu content/dataTrainComplete/'+i,header=None,delimiter="\n")
    final_list = text.values.tolist()
    text2.append(final_list)
    #text1.append(text[0])

#rint(text2[0])

ws = WS('./data')
for i in range(3):
    for j in range(len(text2[i])):
        ws_result=ws(text2[i][j])
        print(ws_result)
'''