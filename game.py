import random

class Player:
    def __init__(self):
        self.nums = {}
        self.answer = None
        self.history = []
        self.win = None
     
    def add_one_stone(self, stones: int) -> int:
        return stones+1


    def add_two_stones(self, stones: int) -> int:
        return stones*2
        
    def make_step(self, stones_on_table : int):
        
        """описание логики выбора хода
        1.Проверка наличия статистических данных возможного хода
        2. выбор между двумя вариантами хода"""
        
        if stones_on_table+1 not in self.nums: 
            self.nums[stones_on_table+1] = 0
        if stones_on_table*2 not in self.nums:
            self.nums[stones_on_table*2] = 0
        if self.nums[stones_on_table+1] > self.nums[stones_on_table*2]: 
            result = self.add_one_stone(stones_on_table)
        else:
            result = self.add_two_stones(stones_on_table)
        self.history.append(result) 
        
        return result
    
    def collecting_points(self):
        
        """получение очков за игру"""
        
        point = -1 + 2*self.win # если False, то point=-1, иначе +1
        for step in self.history:
            self.nums[step] += point
        
        return
    
    
class Game:
    STONES_FOR_WIN = 65
    
    def __init__(self, players : list): 
        self.players = players # List[player]
        self.stones_on_table = random.randint(1, 23) # Last step
    
    def play(self):
        
        """сначала играем, а потом раздаем очки"""
        
        win = False
        for player in self.players:
            player.win = False
            player.history = []
        while not win:
            for player in self.players:
                self.stones_on_table = player.make_step(self.stones_on_table) 
                if self.stones_on_table >= self.STONES_FOR_WIN: #если кто то победил, то заканчиваем цикл
                    player.win = True
                    win = True
                    break
        self.stones_on_table = random.randint(1, 23)
                
    def give_rewards(self):
        for player in self.players:
            player.collecting_points()        
        
