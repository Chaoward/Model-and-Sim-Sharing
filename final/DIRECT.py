import math as math
from sim import signal_sim

# 0 == empty
# 1 == wall
# 3 == receiver
m1 =[
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0]
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1]
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]

TERMINATE_FLOAT = 0.1
TRANSMIT_POWER = 10
ROOM_MAP = m1


#get reciever coords
R_COORD_LIST = []
for i in range( len(ROOM_MAP) ):
    for j in range( len(ROOM_MAP[i]) ):
        if ROOM_MAP[i][j] == 3:
            R_COORD_LIST.append( (i, j) )



class Rectangle:
    def __init__(self, center_coord, w, l):
        self.center = center_coord
        self.width = w
        self.length = l
        self.f_val = obj_f(center_coord)
        self.center_diameter = math.sqrt( (w*w) + (l*l) ) / 2
    
    def trisect(self):
        newRect = []
        if self.length > self.width or abs(self.length - self.width) < 1: #horizontal slices
            one_third = self.length / 3
            for i in range(3):
                newRect.append( 
                    Rectangle(
                        (
                            int(self.width / 2),
                            int( (self.length/6) + (one_third*i) )
                        ),
                        self.width,
                        self.length / 3
                    ) 
                )
        elif self.length < self.width:                           #vertical slices
            one_third = self.width / 3
            for i in range(3):
                newRect.append( 
                    Rectangle(
                        (
                            int( (self.width/6) + (one_third*i) ),
                            int(self.length / 2)
                        ),
                        self.width / 3,
                        self.length
                    ) 
                )


# Center-value Distance = 
# map [y] [x]
def direct_search():
    MAX_Y = len(ROOM_MAP)
    MAX_X = len(ROOM_MAP)

    lowest_bound = {} #<box diameter, f() value>
    rect_set = []

    #sample center of space
    rect_set.append( Rectangle((MAX_X*0.5, MAX_Y*0.5), MAX_X, MAX_Y) )
    
    #Select rectangles
    while len(rect_set) != 0:
        #TODO : sample
        curRect = rect_set.pop()
        if curRect:
            pass
    pass



def obj_f(t_coord):
    f_val = 0
    for receiver in R_COORD_LIST:
        f_val += TRANSMIT_POWER - signal_sim(t_coord, receiver, TRANSMIT_POWER, ROOM_MAP)
    f_val /= len(R_COORD_LIST)
    return f_val