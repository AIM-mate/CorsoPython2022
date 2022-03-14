from module.base import Base

class Son(Base):
    def __init__(self, val1, val2):
        super().__init__(val1)
        self.val2 = val2
