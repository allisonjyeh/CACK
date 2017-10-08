import copy
class layout:
    def __init__(self, isChair, weights):
        self.available = 0
        self.seats = self.transfer_data(isChair, weights)
        self.isChair = isChair


    def transfer_data(self, isChair, weights):
        self.available = 0
        index = 0
        temp = copy.deepcopy(isChair)
        for i in range(len(isChair)):
            for j in range(len(isChair[0])):
                if isChair[i][j]:
                    if weights[index] >= 80:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0
                        self.available += 1
                    index += 1
        return temp

    def update(self, more_weights):
        self.seats = self.transfer_data(self.isChair, more_weights)
        return self

    def seatsLeft(self):
        return self.available
