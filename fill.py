import numpy as np

p = np.zeros([190, 4], dtype=int)
point=np.loadtxt('exc.txt',delimiter=',',dtype=int)
#print(point)
maplabel=np.loadtxt('maplabel.txt',delimiter=' ',dtype=int)
#print(maplabel[31][39])
#print(maplabel[0][22])
#print(point.shape[0])
p[:,0]=point[:,1]
p[:,1]=point[:,0]
p[:,2]=point[:,2]
#print(p)
#print(point[0][1])
A=np.zeros([190,2],dtype=int)
A[:,0]=point[:,1]
A[:,1]=point[:,0]
#print(A)
#print(A[5])
#print(maplabel[A[11][0]][A[11][1]])
temp=[]
for i in range(190):
    p[i][3]=maplabel[A[i][0]][A[i][1]]
    # print(p[i][3])
    temp.append(p[i][3])
print(p[116])
temp.sort()
print(temp)



'''
for i in range(point.shape[0]):
    x[i]=point[i,0]
    y[i]=point[i,1]
    A=[point[i,0],point[i,1]]
print(x)

'''






'''    
for i in range(48):
    for j in range(190):
        if p[]

'''


