import math
class point:
	"point"
p1=point()
p2=point()

def distance_between(a,b):
    dx=p1.x-p2.x
    dy=p1.y-p2.y
    dist=math.sqrt(dx**2+dy**2)
    print(dist)
p1.x=44
p2.x=55
p1.y=30
p2.y=40

distance_between(p1,p2)
