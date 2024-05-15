from math import sqrt, log10

class VectorLine:
    parallel_vector = ()
    start_point = ()
    max_t = 0

    # sets line of transmitter to receiver
    def setLine(t_coord, r_coord):
        b_vector = (r_coord[0] - t_coord[0], r_coord[1] - t_coord[1])
        vector_mag = sqrt( (b_vector[0] * b_vector[0]) + (b_vector[1] * b_vector[1]) )
        if vector_mag != 0:
            b_vector = (b_vector[0] / vector_mag, b_vector[1] / vector_mag)
        VectorLine.parallel_vector = b_vector
        VectorLine.start_point = t_coord
        if b_vector[0] == 0 and b_vector[1] == 0:
            VectorLine.max_t = 0
        elif b_vector[1] == 0:
            VectorLine.max_t = (r_coord[0] - t_coord[0]) / b_vector[0]
        else:
            VectorLine.max_t = (r_coord[1] - t_coord[1]) / b_vector[1]

    # returns coord on vector line based on t parameter
    def lineEquation(t):
        return (
            int( VectorLine.start_point[0] + (t * VectorLine.parallel_vector[0]) ),
            int( VectorLine.start_point[1] + (t * VectorLine.parallel_vector[1]) ),
        )

# Set up the vector line from power transmitter Pt to power receiver Pr
VectorLine.setLine((0, 1), (2, 2))

# Example map array
"""
map_array = [
    ['0', 'Pt', '0'],
    ['0', '1', '1'],
    ['0', '0', 'Pr']
]
"""

def sameCoord(first, second):
    if first is None or second is None:
        return False
    return first == second
    
    #if type(last_wall) != tuple or type(location) != tuple:
    #    return False
    #return last_wall[0] == location[0] and last_wall[1] == location[1]


def signal_sim(t_coord, r_coord, transmit_power, map_array):
    # Initialize power receiver Pr
    Pr = transmit_power
    VectorLine.setLine(t_coord, r_coord)

    #power lose from distance traveled
    dist = (r_coord[0] - t_coord[0], r_coord[1] - t_coord[1])
    dist = sqrt(dist[0]*dist[0]) + (dist[1]*dist[1])
    if dist > 1:
        Pr -= 20 * log10(dist/0.12)

    # Iterate through the vector line and update Pr
    last_wall = None
    cur_location = VectorLine.start_point
    t = 0
    while not sameCoord(cur_location, r_coord) and t < VectorLine.max_t:
        cell_value = map_array[int(cur_location[0])][int(cur_location[1])]
        if cell_value == 1 and not sameCoord(last_wall, cur_location):  # Wall encountered
            Pr -= 4.6
            last_wall = cur_location
        t += 0.1
        cur_location = VectorLine.lineEquation(t)
        #print(cur_location)
        
    return Pr