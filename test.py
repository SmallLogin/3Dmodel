import numpy
import math
xy_coordinate = []
# 转换后的XY坐标集
def millerToXY (lon, lat):

    L = 6381372*math.pi*2
    W = L
    H = L/2
    mill = 2.3
    x = lon*math.pi/180
    y = lat*math.pi/180
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    xy_coordinate.append((int(round(x)),int(round(y))))
    return xy_coordinate

lon = -122.6876
lat = 45.5302
xy = millerToXY(lon,lat)
print(xy)