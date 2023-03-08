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
    for pin in range(len(x)):
        less_index = pin
        for search in range(pin+1,len(x)):
            if x[less_index]  >  x[search]:
                less_index = search
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
    print("\n\t\t  Seem like you need some help!")

    while True:
        user_choice = input("\t\t  Type in the number that you think it's in guessed number: ")
        if len(user_choice) > len(current_num):
            print("\n\t\t  Invalid input! try again!!!")
        else:
            break

    num_section = []
    i = 0
    while i < len(current_num)-(len(user_choice)-1):
        j = i
        section = ''
        while len(section) < len(user_choice) and j < len(current_num):
            section += current_num[j]
            j+=1
        num_section.append(section)
        i+=1

    print(f"\n\t\t  Doing search with {len(user_choice)} length sections... ")
    num_section = list(map(int,num_section))
    num_section_sorted = selection_sort(num_section)

    find = binarySearch(num_section_sorted,0,len(num_section_sorted) - 1,int(user_choice))
    if find == -1:
        print(f"\n\t\t  Sadly, {user_choice} is not in guessed number")
    else:
        print(f"\t\t\t Found {user_choice} in guessed number")

print("")
print("\t\t","="*25+'  WELCOME TO  '+"="*26)
print("\t\t","#"*20 +'  NUMBER GUESSING GAME! '+"#"*21)
print("\t\t"," "*13+'  ✯✯✯ PREPARE TO GET HIT AND BLOW ✯✯✯  '+" "*20)
print("\n\t\t","~"*15 +'  programmed by Nathaniel Finuliar  '+"~"*14)

print("\n\n\t\t  If you want help on guessing digits type \"H\"")
print("\t\t",'-'*65)

fname = input("\t\t  Enter First name: ")
lname = input("\t\t  Enter Last name: ")
name = fname + " " + lname
k = int(input('\n\t\t  How many digits do you want to guess?: ',))
n = int(input("\t\t  How many rounds do you wanna try? : "))
print("\t\t",'-'*65)
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
    # print("\t\t ----------" + " * "*3+ "-----------")
    if len(queue) == 0:
        print("\t\t", "="*65)
        print()
        print("\t\t\t\t\t  GAME ENDED!")
        winner_name = ""
        winner_score = 0
        if len(set(data.values()))== 1:
                print("\t\t\t\t\t     DRAW!")
                print("\n\t\t  Unfortunately Both Players didn't guess the correct random Number")
                print("\t\t\t\t     Better Luck Next Time!")
                print("\n\t\t\t"," "*8+"The correct number was "+num_gen+" ✔")  
                break
        else:
            for name,score in data.items():
                if score > winner_score:
                    winner_name = name
                    winner_score = score
            print(f"\n\t\t  The Winner is ✯ ✯ ✯ {winner_name} ✯ ✯ ✯ with the score {winner_score} points!")
            print("\n\t\t\t"," "*8+"The correct number was "+num_gen+" ✔")            
            print("")
            break
    else:
        if queue[0] == name:
            print(f"\t\t  {queue[0]}'s Turn!")
            while True:
                guess_num = input(f"\n\t\t  Enter {k} digits number or \"H\" for help:  ")[:k:]
                if guess_num == num_gen:
                    print("\t\t", "="*5+" Win!!!! You got the correct number : "+num_gen+"!!! "+"="*5)
                    found_winner = True
                    break
                else:
                    if (guess_num.isdigit() and len(guess_num) == k) or guess_num.lower() == 'h':
                        if guess_num.isdigit():
                            player_score = stack_count_score(num_gen,name,guess_num)
                            player_hit = player_score.get_hit()
                            player_blow = player_score.get_blow()
                            player_total = player_score.get_total()
                            print(f"\t\t  You got {player_hit} Hits {player_blow} Blows result in {player_total} points!")
                            data[name] += player_total
                        elif guess_num.upper() == 'H':
                            if not helped:
                                helped = True
                                help(num_gen)
                            else:
                                print("\t\t  You already asked for help")
                            continue
                        break
                    else:
                        print("\t\t  Invalid input try again!")
        elif queue[0] == bot.name:
            print("\t\t  Bot Turn!")
            bot.get_number()
            bot_pick = bot.choosed_num
            if bot_pick == num_gen:
                print("\t\t     ","="*5+" Win!!!! "+bot.name+" got the correct number : "+num_gen+"!!! "+"="*5)
                found_winner = True
            else:
                bot.get_score()
                bot_hit = bot.bot_hit()
                bot_blow = bot.bot_blow()
                bot_score = bot.bot_score()
                print(f"\n\t\t  {bot.name} guessed {bot_pick} ")
                print(f"\t\t  {bot.name} got {bot_hit} Hits {bot_blow} Blows result in {bot_score} points!")
                data[bot.name] += bot_score
                bot.delete_previous()
        queue = queue_option.delete_queue(queue)
        play_round += 1
        print()