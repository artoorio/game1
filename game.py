class Player:
    def __init__(self, ):
        self.nums = {}
        self.answer = 0
        self.history = []
        self.win = None
        
    def make_step(self,num_in : 'Last step number', num_win : 'Number for win'):
        
        '''описание логики выбора хода''' 
        
        return num_in+1
    def collecting_points(self):
        'получение очков за игру'
        return
    
class Game:
    
    def __init__(self, start: 'BeginingNumber', finish : 'NumberForWin', players: 'List[Player]'): 

        self.start = start
        self.finish = finish
        self.players = players
        self.step_result = None
        self.last_step = start
    
    def play(self):
        
        '''сначала играем, а потом раздаем очки'''
        
        while self.step_result < self.finish:
            for player in self.players:
                self.step_result = player.make_step(self.last_step,self.finish) # вот мы используем метод игрока в игре
                if self.step_result >= self.finish: #если кто то победил, то заканчиваем цикл
                    break
                self.last_step = self.step_result #
                
        for player in self.players:
            player.collecting_points() #раздача очков