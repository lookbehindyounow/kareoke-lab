class Club:
    def __init__(self,name=str,till=float,fee=10):
        self.name=name
        self.till=till
        self.rooms=[]
        self.fee=fee

    def check_out(self,guest):
        [room.check_out(guest) for room in self.rooms]

    def pay_in(self,amount):
        self.till+=amount