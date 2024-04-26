from math import sqrt, log10

class VectorLine:
    y_cross = 0
    slope = 0

    # sets line of transmitter to receiver
    def setLine(t_coord, r_coord):
        b_vector = (r_coord[0] - t_coord[0], r_coord[1] - t_coord[1])
        VectorLine.slope = b_vector[1] / b_vector[0]
        VectorLine.y_cross = t_coord[1] + ( -1 *(t_coord[0] / b_vector[0]) * b_vector[1] )   

    # returns slope
    def lineEquation(x):
        return int((VectorLine.slope * x) + VectorLine.y_cross) # convert to int to avoid float

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


def signal_sim(t_coord, r_coord, transmit_power, map_array):
    # Initialize power receiver Pr
    Pr = transmit_power
    VectorLine.setLine(t_coord, r_coord)

    #power lose from distance traveled
    dist = (r_coord[0] - t_coord[0], r_coord[1] - t_coord[1])
    dist = sqrt(dist[0]*dist[0]) + (dist[1]*dist[1])
    if dist > 1:
        Pr -= log10(dist/0.12)

    # Iterate through the vector line and update Pr
    last_wall = None
    x = t_coord[0]
    while x < r_coord[0]:  
        y = VectorLine.lineEquation(x)
        
        if 0 <= x < len(map_array) and 0 <= y < len(map_array[0]):
            cell_value = map_array[x][y]
            if cell_value == 1 and last_wall != (int(x), y):  # Wall encountered
                Pr -= 1
                last_wall = (int(x), y)
                print("Wall encountered at x:", x, " y:", y)  # Debugging
                print("Pr value: ", Pr)  # Debugging
        x += 0.2
    
    print("Final Power Receiver (Pr):", Pr)
    return Pr