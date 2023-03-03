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
        num_group = []
        while len(self.picked_number_blow) > 0:
            num_group.append(self.picked_number_blow.pop())

        for element in num_group:
            if element in self.current_number:
                if element in self.set_used.keys() and self.set_used[element] != 0:
                    self.count_blow += 1
                    self.set_used[element] -= 1
        
    def get_hit(self):
        return self.count_hit
    
    def get_blow(self):
        return self.count_blow
    
    def get_total(self):
        return ((self.count_hit) * 0.75) + ((self.count_blow)*0.25)
        


class Play_queue():

    def __init__(self):
        self.queue = []

    def generate_queue(self,round_,players):
        self.round_ = round_
        self.players = players
        i = 0
        while i < self.round_:
            for player in self.players:
                self.queue.append(player)
        i+=1
        return self.queue
    
    def delete_queue(self,queue_):
        self.queue_ = queue_
        self.queue_.pop(0)
        return self.queue_
    


def selection_sort(x : list):
    less_index = 0
    for pin in range(len(x)):
        for search in range(pin+1,len(x)):
            if int(x[less_index]) > int(x[search]):
                less_index = int(search)
        x[pin],x[less_index] = x[less_index],x[pin]
    return x

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)    
    else:
        return -1 
    

#########################################################
class Bot():

    def __init__(self,current_number):
        self.name = "Computer"
        self.current_number = current_number
        self.choosed_num = ""
        self.score = 0
        self.count_hit = 0
        self.count_blow = 0

    def get_number(self):
        while len(self.choosed_num) < len(self.current_number):
            num = rd.randint(0,9)
            num = str(num)
            self.choosed_num += num

    def get_score(self):
        score = stack_count_score(self.current_number,self.name,self.choosed_num)
        self.score = score.get_total()
        self.count_hit = score.get_hit()
        self.score_blow = score.get_blow()

    def delete_previous(self):
        self.choosed_num = ""

    def bot_hit(self):
        return self.count_hit
    
    def bot_blow(self):
        return self.score_blow
    
    def bot_score(self):
        return self.score
    
def help(current_num):
    print("Seem like you need some help!")
    user_choice = input("Type in the number that you think it's in guessed number: ")
    num_section = []
    for i in range(0,len(current_num),len(user_choice)):
        num_section.append(current_num[i:i+len(user_choice)])
    print(f"Doing search with {len(user_choice)} length sections: ")
    num_section_sorted = selection_sort(list(map(int,num_section)))
    find = binarySearch(num_section_sorted,int(user_choice),0,len(num_section_sorted) - 1)
    if find != -1:
        print(f"Sadly, {user_choice} is not in guessed number")
    else:
        print(f"Found {user_choice} in guessed number")


print("="*25+' Welcome to the guessing game '+"="*25)
print("If you want help on guessing digits type \"H\"")
print('-'*60)

fname = input("Enter First name: ")
lname = input("Enter Last name: ")
name = fname + " " + lname
k = int(input('How many digits do you want to guess?: ',))
n = int(input("How many rounds do you wanna try? : "))
print("="*80)
print()

play_round = 0
num_gen = ''
helped = False

while len(num_gen) != k: # Generate num
    num = rd.randint(0,9)
    num = str(num)
    num_gen += num

bot = Bot(num_gen)
data = {name:0, bot.name:0 }
queue_option = Play_queue()
queue = queue_option.generate_queue(n,[name,bot.name])
found_winner = False
while len(queue) >= 0 and not found_winner:
    print(("-"*10)+" * "*5+("-"*10))
    if len(queue) == 0:
        print("="*50)
        print()
        print("Game ended!")
        winner_name = ""
        winner_score = 0