class Player:
    def __init__(self):
        self.nums = {}
        self.answer = None
        self.history = []
        self.win = None
        
    def make_step(self, stones_on_table : int, stones_for_win : int):
        
        """описание логики выбора хода
        1.Проверка наличия статистических данных возможного хода
        2. выбор между двумя вариантами хода"""
        
        if stones_on_table+1 not in nums: # проверка наличия данных
            nums[stones_on_table+1] = 0
        if if stones_on_table*2 not in nums:
            nums[stones_on_table*2] = 0
        if nums[stones_on_table+1] > nums[stones_on_table*2]: # выбор хода
            result = stones_on_table+1
        else:
            result = stones_on_table*2
        self.history.append(result) # запись ходов текущей партии
        
        return result
    
    def collecting_points(self):
        
        """получение очков за игру"""
        
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
                    win = True
                    break
                
                
        for player in self.players:
            player.collecting_points() # раздача очков
