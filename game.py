class Player:
    def __init__(self, ):
        self.nums = {}
        self.answer = None
        self.history = []
        self.win = None
        
    def make_step(self,num_in : 'Last step number', num_win : 'Number for win'):
        
        '''описание логики выбора хода''' 
        
        return num_in+1
    
    def collecting_points(self):
        'получение очков за игру'
        return
    
    
class Game:
    def __init__(self, start: int, finish : int, players : list): 
        self.start = start # Starting number
        self.finish = finish # Winning number
        self.players = players # List[player]
        self.step_result = None # Step result
        self.last_step = start # Last step
    
    def play(self):
        
        '''сначала играем, а потом раздаем очки'''
        
        while self.step_result < self.finish:
            for player in self.players:
                self.step_result = player.make_step(self.last_step,self.finish) 
                if self.step_result >= self.finish: #если кто то победил, то заканчиваем цикл
                    break
                self.last_step = self.step_result 
                
        for player in self.players:
            player.collecting_points() #раздача очков
