from math import *
import numpy as np

def getTrans(x,y,z):
    return np.array([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])

def getRotX(theta):
    c = cos(theta)
    s = sin(theta)
    return np.array([[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]])

def getRotY(theta):
    c = cos(theta)
    s = sin(theta)
    return np.array([[c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]])

def getRotZ(theta):
    c = cos(theta)
    s = sin(theta)
    return np.array([[c,0,s,0],[0,1,0,0],[-s,0,c,0],[0,0,0,1]])

def getR(iTk):
    return iTk[0:3,0:3]

def getO(iTk):
    return iTk[0:3,3]

def getPi(iTk,Pk):
    Pk.append(1)
    return np.dot(iTk[0:4,:],np.array(Pk))

def getVi(iTk,Vk):
    Vk.append(0)
    return np.dot(iTk[0:4,:],np.array(Vk))

def getDh(th,a,d,alpha):
    T1=getRotZ(th)
    T2=getTrans(a,0,d)
    T3=getRotX(alpha)
    DH=np.dot(T1,T2)
    DH=np.dot(DH,T3)
    return DH

def getInvDH(iTk):
    iRk=getR(iTk)
    iOk=getO(iTk)
    kRi=np.transpose(iRk)
    kOi=np.dot(-kRi,iOk)
    #Ajoute la colonne contenant les informations en position
    kRi=np.column_stack((kRi,kOi))
    h_coordinates=np.array([0,0,0,1])
    kRi=np.append(kRi,h_coordinates)

    return kRi

R=getDh(90,2,0,60)
Rinv=getInvDH(R)
#print R
print Rinv
