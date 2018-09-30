import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def col(x,j):
    return np.array([i[j] for i in x])

def plot(mse):
    with mpl.rc_context(rc={'font.family': 'serif', 'font.size': 11}):
        fig = plt.figure(figsize=(5,5))
        ax1 = fig.add_subplot(111)
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('MSE')
        plt.plot(mse)
        plt.legend(['MSE'], loc='upper right')

def BP_BACK(training_example,eta):
    n = len(training_example)
    w = np.random.random((2,3))-0.5
    v = np.random.random((3,2))-0.5
    u = np.random.random((2,3))-0.5
    
    mse = []
    for count in range(n):
        one_sample = training_example[count]
        x = np.array(one_sample[:3])
        y = np.array(one_sample[3:])
        net2 = np.dot(w,x)
        hidden1 = np.array([sigmoid(i) for i in net2])
        net3 = np.dot(v,hidden1)
        hidden2 = np.array([sigmoid(i) for i in net3])
        net4 = np.dot(u,hidden2)
        o = np.array([sigmoid(i) for i in net4])
        
        delta3 = np.array([(y[i]-o[i])*o[i]*(1-o[i]) for i in range(2)])
        delta2 = np.array([hidden2[j]*(1-hidden2[j])*np.dot(delta3,col(u,j)) for j in range(3)])
        delta1 = np.array([hidden1[k]*(1-hidden1[k])*np.dot(delta2,col(v,k)) for k in range(2)])
        
        for i in range(2):
            for j in range(3):
                u[i][j] += eta*delta3[i]*hidden2[j]
        for i in range(3):
            for j in range(2):
                v[i][j] += eta*delta2[i]*hidden1[j]
        for i in range(2):
            for j in range(3):
                w[i][j] += eta*delta1[i]*x[j]
        e = o-y
        mse.append(np.dot(e,e)/2)
    plot(mse)

def Read_Data(filename):
    f = open(filename,'r')
    readlist = [x.rstrip('\n') for x in f]
    f.close()
    data = []
    for i in readlist:
        words = i.split()
        data.append([float(k) for k in words])
    return data

BP_BACK(Read_Data('data.txt'),0.9)