import random as rd

############# DSA's functions #############
class stack_count_score():

    def __init__(self,current_number,name,picked_number):
        self.name = name
        self.current_number = current_number
        self.picked_number = picked_number
        self.stack_ = []
        self.set_used = {}
        self.count_hit = 0
        self.count_blow = 0
        self.set_dictionary()
        self.hitcal()
        self.blowcal()
    
    def set_dictionary(self):
        for i in self.current_number:
            if i not in self.set_used.keys():
                self.set_used[i] = 1
            else:
                self.set_used[i] += 1

    def hitcal(self):
                
        self.stack_hit = [i for i in self.current_number]
        self.picked_number_hit = [i for i in self.picked_number]
        pair_check = []
        while len(self.stack_hit)  > 0:
            pair = []
            pair.append(self.stack_hit.pop())
            pair.append(self.picked_number_hit.pop())
            pair_check.append(pair)

        for first,second in pair_check:
            if first == second:
                self.count_hit += 1
                self.set_used[first] -= 1

    def blowcal(self):
        self.picked_number_blow = [i for i in self.picked_number]