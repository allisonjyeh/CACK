from layout2 import layout
#
# testChair = [[True for i in range(6)], [True for i in range(6)], [False, True, True, True, True, False]]
# testWeights = [60, 80, 40, 100, 150, 0, 200, 250, 178, 35, 25, 134, 2, 7, 10, 100]
# test = layout(testChair, testWeights)
# print(test.seats)
# newWeights = [160, 80, 40, 100, 150, 0, 200, 250, 178, 35, 25, 134, 2, 7, 10, 100]
# print(test.seatsLeft())
# test = test.update(newWeights)
# print(test.seats)
# print(test.seatsLeft())

#math/stat library mezzanine
w, h = 23, 9;
floor_plan = [[False for x in range(w)] for y in range(h)]
for i in range(9):
    if i != 3:
        floor_plan[i][22] = True
for j in range(4,16):
    if j!=12 :
        floor_plan[8][j] = True

for k in range(19,23):
        floor_plan[8][k] = True;
floor_plan[8][1] = True;
floor_plan[1][1] = True;
floor_plan[1][2] = True;
# print(floor_plan)
numTrues = 0
# for i in range(len(floor_plan)):
#     for j in range(len(floor_plan[0])):
#         if floor_plan[i][j]:
#             numTrues += 1
# print(numTrues)
test_weights = [80, 100, 30, 30, 40, 0, 0, 0, 150, 150, 0, 0, 0, 150, 150, 50, 0, 0, 150, 0, 0, 0, 0, 0, 0]
test = layout(floor_plan, test_weights)
print(test.seats)
print(test.seatsLeft())
newWeights = [0, 100, 30, 30, 40, 0, 0, 0, 150, 150, 0, 0, 0, 150, 150, 50, 0, 0, 150, 0, 0, 0, 0, 0, 0]
test = test.update(newWeights)
print(test.seats)
print(test.seatsLeft())
