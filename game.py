class Player:
    def __init__(self, ):
        self.nums = {}
        self.answer = None
        self.history = []
        self.win = None
        
    def make_step(self,stones_on_table : 'Last step number', stones_for_win : 'Number for win'):
        
        '''описание логики выбора хода''' 
        
        return stones_on_table+1
    
    def collecting_points(self):
        'получение очков за игру'
        return
    
    
class Game:
    def __init__(self, start: int, finish : int, players : list): 
        self.STONES_FOR_WIN = finish 
        self.players = players # List[player]
        self.stones_on_table = start # Last step
    
    def play(self):
        
        '''сначала играем, а потом раздаем очки'''
        
        while self.stones_on_table < self.STONES_FOR_WIN:
            for player in self.players:
                self.stones_on_table = player.make_step(self.stones_on_table,self.STONES_FOR_WIN) 
                if self.stones_on_table >= self.STONES_FOR_WIN: #если кто то победил, то заканчиваем цикл
                    break
                
                
        for player in self.players:
            player.collecting_points() # раздача очков
