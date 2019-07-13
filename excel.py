import xlrd
import math
import xlwt

from xlutils.copy import copy
import numpy as np


def extract(inpath):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号
    point = np.zeros([190, 3],dtype=int)
    '''
    newbook = copy(data)
    newsheet = newbook.get_sheet(0)
    # 在末尾增加新行
    str = 'point'
    newsheet.write(ncols, 0, str)
    #newbook.save(inpath)
    '''
    count=0
    for i in range(1, nrows):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result1 = alldata[4]  # 取出表中第4列数据
        result2 = alldata[3]  # 取出表中第5列数据
        y =round(alldata[2])

        #print(result1,result2)
        '''
        math.ceil(f)  # 向上取整
        math.floor(f)  # 向下取整
        round(f)  # 四舍五入'''
        x=round(abs(result1-g1[1])/LONG)
        z=round(abs(result2-g1[0])/LAT)
        #point=[x,z,y]
        if result1 == -122.68804944:
            print(g1[1],abs(result1-g1[1])/LONG, abs(result2-g1[0])/LAT,x,z,y)

        point[i-1]=[x,z,y]
        #print(type(point[2]))


        #alldata[5]=point
        #print(alldata[5])
        count+=1
        #newsheet.write(ncols,5)
       # newbook.save(inpath)
    print(count)
    #print(type(point))
    #print(point)
    return point



g1=[45.5348,-122.6940]
g2=[45.5348,-122.6876]
g3=[45.5302,-122.6940]
g4=[45.5302,-122.6876]
#print(round(g1[0]-g3[0],4))

LAT=round(abs(g1[0]-g3[0])/50,6)

LONG=round(abs(g1[1]-g2[1])/50,6)
print(LAT,LONG)


inpath = '1.xlsx'  # excel文件所在路径
point=extract(inpath)
print(point)
print(point[116])
np.savetxt("exc.txt",point,fmt='%d',delimiter=',')