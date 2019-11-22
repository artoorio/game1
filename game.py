class Player:
    def __init__(self):
        self.nums = {}
        self.answer = None
        self.history = []
        self.win = None
        
    def make_step(self, stones_on_table : int, stones_for_win : int):
        
        """описание логики выбора хода""" 
        
        return stones_on_table+1
    
    def collecting_points(self):
        
        """получение очков за игру"""
        
        point = -1 + 2*self.win # если False, то point=-1, иначе +1
        for step in self.history:
            self.nums[step] += point
        
        return
    
    
class Game:
    def __init__(self, start: int, finish : int, players : list): 
        self.STONES_FOR_WIN = finish 
        self.players = players # List[player]
        self.stones_on_table = start # Last step
    
    def play(self):
        
        """сначала играем, а потом раздаем очки"""
        
        win = False
        while not win:
            for player in self.players:
                self.stones_on_table = player.make_step(self.stones_on_table,self.STONES_FOR_WIN) 
                if self.stones_on_table >= self.STONES_FOR_WIN: #если кто то победил, то заканчиваем цикл
                    player.win = True
                    win = True
                    break
                
                
        for player in self.players:
            player.collecting_points() # раздача очков
