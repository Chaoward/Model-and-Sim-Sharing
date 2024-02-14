RANDOM_OUT_PATH = "./random.out"
total = 0
counted = {}
for i in range(1, 11):
    dec = round(i * 0.1, 1)
    counted[dec] = 0


def count(value):
    global total
    value = round(value, 1)
    for i in counted.keys():
        if (i == value):
            counted[i] += 1
            total += 1
            return
    counted[1] += 1
    total += 1

def display():
    for num in counted.keys():
        squares = ""
        for i in range(0, round( (counted[num] / total) * 50 ) ):
            squares += "#"
        print(f"{num} {counted[num]} : {squares}")

    

#===== Start Counting =========================
with open(RANDOM_OUT_PATH, "r") as file:
    while file.readable():
        floatStr = file.readline().strip()
        if len(floatStr) == 0: break
        count(float(floatStr))
    file.close()
display()
 