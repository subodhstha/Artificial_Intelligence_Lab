from collections import defaultdict
jug1=6 
jug2=4 
aim=2 
processed = defaultdict(lambda: False) 
def waterJug(amt1, amt2):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2) 
        return True
    if processed[(amt1, amt2)] == False: 
        print(amt1, amt2) 
        processed[(amt1, amt2)] = True
        return (waterJug(0, amt2) or 
                waterJug(amt1, 0) or 
                waterJug(jug1, amt2) or
                waterJug(amt1, jug2) or 
                waterJug(amt1 + min(amt2, (jug1-amt1)),amt2 - min(amt2, (jug1-amt1))) or 
                waterJug(amt1 - min(amt1, (jug2-amt2)),amt2 + min(amt1, (jug2-amt2)))) 
    else:
        return False
print("--Water Jug Problem--\n") 
print("Capacity of jugs are {jug1} and {jug2} liters. \n")
print("Initially both jugs are empty.\n") 
print("Steps: ") 
waterJug(0, 0)
