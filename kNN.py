from numpy import *
import cPickle

def getData():
#['labels','filenames','batch_label','data']    
    data={}
    fo = open('data_batch_1', 'rb')
    dict1=cPickle.load(fo)
    data.update(dict1)
    fo.close()
    fo = open('data_batch_2', 'rb')
    dict2=cPickle.load(fo)
    data.update(dict2)
    fo.close()
    fo = open('data_batch_3', 'rb')
    dict3=cPickle.load(fo)
    data.update(dict3)
    fo.close()
    fo = open('data_batch_4', 'rb')
    dict4=cPickle.load(fo)
    data.update(dict4)
    fo.close()
    fo = open('data_batch_5', 'rb')
    dict5=cPickle.load(fo)
    data.update(dict5)
    fo.close()
    num=0
    for item in data['labels']:
        num+=1
    return data,num

def getTestData():
#['batch_label','labels','data','filenames']
    testData={}
    fo = open('test_batch', 'rb')
    dict6=cPickle.load(fo)
    testData.update(dict6)
    fo.close()
    tnum=0
    for item in testData['labels']:
        tnum+=1
    return testData,tnum

def predict(data,num,testData,tnum):
    dis=zeros(tnum)
    label=zeros(tnum)
    for i in range(tnum):
        dis[i]=(sum((testData['data'][i]-data['data'])**2))**0.5
        label[i]=data['labels'][argsort(-dis)[0]]
    return label
    














