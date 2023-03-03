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
