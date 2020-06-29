class time(object): # this class is ussed manage the execution time of the app

    def __init__(self):
        self.seconds = 0 # 60 seconds = 1min
        self.minutes = 0 # 1min = 1hour
        self.hours = 0   # 24h = 1day
        self.days = 0    
        self.weeks = 0   # 7days = 1 week

    def addSeconds(self,value:int):
        self.seconds += value
    
    def addMinutes(self,value:int):
        self.minutes += value
    
    def addHours(self,value:int):
        self.hours += value

    def addDays(self,value:int):
        self.days += value

    def addWeeks(self,value:int):
        self.weeks += value

    def restart(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.days = 0
        self.weeks= 0

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__seconds = value
        while self.__seconds >= 60:
            self.__seconds -= 60
            self.minutes += 1
            
    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__minutes = value
        while self.__minutes >= 60:
            self.__minutes -= 60
            self.hours += 1

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self,value:int):
        if (value < 0):
            raise ValueError("cannot be more than 24 hours or negative")
        self.__hours = value
        while self.__hours >= 24 :
            self.__hours -= 24
            self.days += 1
        
    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self,value:int):
        if (value < 0):
            raise ValueError("cannot be more than 31 days")
        self.__days = value
        while self.__days >= 7:
            self.__days -= 7
            self.weeks += 1
        
    @property
    def weeks(self):
       return self.__weeks

    @weeks.setter
    def weeks(self,value:int):
        if (value < 0):
            raise ValueError("cannot be negative")
        self.__weeks = value
