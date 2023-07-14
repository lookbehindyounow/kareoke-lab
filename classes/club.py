class Club:
    def __init__(self,name=str):
        self.name=name
        self.rooms=[]

    def check_out(self,guest):
        [room.check_out(guest) for room in self.rooms]