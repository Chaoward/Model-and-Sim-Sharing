import math as math
from scipy import optimize as op
from sim import signal_sim

# 0 == empty
# 1 == wall
# 3 == receiver
m1 =[
    [3, 3, 3, 1, 3, 3, 1, 3, 3, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 1, 0, 0, 1, 0, 0, 3],
    [3, 0, 0, 1, 0, 0, 1, 0, 0, 3],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [3, 0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 3, 3, 1, 3, 3, 1, 3, 3, 3]
]

m2 =[
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 3, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 3, 1, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]

TERMINATE_FLOAT = 0.1
TRANSMIT_POWER = 100
ROOM_MAP = m1

FIRST_COORD = None


#get reciever coords
R_COORD_LIST = []
for i in range( len(ROOM_MAP) ):
    for j in range( len(ROOM_MAP[i]) ):
        if ROOM_MAP[i][j] == 3:
            R_COORD_LIST.append( (i, j) )


def toMapArray():

    pass




# Center-value Distance = 
# map [y] [x]
def direct_search():
    MAX_X = len(ROOM_MAP)
    MAX_Y = len(ROOM_MAP[0])

    bounds = op.Bounds([0, 0], [MAX_X-1, MAX_Y-1])
    results = op.direct( obj_f, bounds, maxiter=10000 )
    print(results.x)
    print(results.fun)
    print(results.nfev)
    print(results.message)


def obj_f(t_coord):
    global FIRST_COORD
    if type(FIRST_COORD) == None:
        FIRST_COORD = t_coord
    f_val = 0
    for receiver in R_COORD_LIST:
        f_val += TRANSMIT_POWER - signal_sim( (int(t_coord[0]), int(t_coord[1])), receiver, TRANSMIT_POWER, ROOM_MAP)
    f_val /= len(R_COORD_LIST)
    return f_val


########## PROGRAM START #######################
direct_search()
print(obj_f( FIRST_COORD ))
#print( obj_f( (5, 5) ) )