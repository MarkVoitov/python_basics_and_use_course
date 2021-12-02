class MoneyBox:
    def __init__(self, capacity):
        """конструктор с аргументом – вместимость копилки"""
        self.capacity = capacity
        self.total = 0
        
    def can_add(self, v):
        """True, если можно добавить v монет, False иначе"""
        if self.total + v <= self.capacity:
            return True
        else:
            return False
        
    def add(self, v):
        """положить v монет в копилку"""
        self.total += v
        return self.total