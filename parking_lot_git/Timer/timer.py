import time
import datetime
from my_logging import MyLogger

class ParkingTimer:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.time_thread = None
        self.MyLogger = MyLogger("parking_lot.log", __name__) 
             
    
    def start_timer(self) -> float:
        """
        the object accept current time
        """
        
        self.start_time = time.time()  
        self.MyLogger.info(f"start time : {datetime.datetime.now()}")
        self.MyLogger.debug(f"start time in seconds: {self.start_time}")
        
    def end_timer(self) -> float:
        """
        the object accept current time

        """
       
        self.end_time = time.time()
        self.MyLogger.info(f"end time : {datetime.datetime.now()}")
        self.MyLogger.debug(f"end time in seconds: {self.end_time}")


        
    def calculation_time(self) -> float:
        """
        calculate elapsed time between entrance and the exit

        Returns:
            [float]: [returns the calculate of the time ]
        """
       
        return self.end_time - self.start_time
    
        

    def calculation_to_days(self) -> int:
        """
        calculate minute to days
        Returns:
            int: [number of days and minute]
        """
             
        parking_time = self.calculation_time()
        minute_in_day = 1440
        days = parking_time // minute_in_day 
        remaining_minute = parking_time % minute_in_day
        self.MyLogger.info(f"Parking time: {int(days)} days and {int(remaining_minute)} minutes")
        self.MyLogger.debug(f"Parking time in seconds: {parking_time}")
        return f"{int(days)} days and {int(remaining_minute)} minutes"
      
    def calculation_to_week(self) -> int:
        """
        calculate days to week
        Returns:
            int: [number of weeks and days]
        """

        parking_time = self.calculation_time()
        minute_in_week = 10080
        week = parking_time // minute_in_week 
        remaining_days = parking_time % minute_in_week
        self.MyLogger.info(f"Parking time: {int(week)} weeks and {int(remaining_days)} minutes")
        self.MyLogger.debug(f"Parking time in seconds: {parking_time}")
        return f"{int(week)} weeks and {int(remaining_days)} days"
    
    def calculation_to_months(self) -> int:
        """        
        calculate weeks to months
        Returns:
            int: [number of months and weeks]
        """

        parking_time = self.calculation_time()
        minute_in_months = 40320
        months = parking_time // minute_in_months
        remaining_days = parking_time % minute_in_months
        self.MyLogger.info(f"Parking time: {int(months)} months and {int(remaining_days)} minutes")
        self.MyLogger.debug(f"Parking time in seconds: {parking_time}")
        return f"{int(months)} months and {int(remaining_days)} weeks"


    def start_timer_to_one_hour(self, duration = 60) -> bool:
        """
        start timer 60 minute
        Returns:
            bool: [True if 60 minute have passed, False if not passed ]
        """
        start_timer = datetime.datetime.now()
        self.MyLogger.info(f'Started timer for "60" minute(s) {start_timer}.')
        start_time = time.time()
        stop_flag = False

        while (time.time() - start_time) < duration:
         
            if stop_flag:
                self.logger.info
                return False

        return True

        
    def stop_timer(self):
        """
        stop timer
        """
        
        global stop_flag
        stop_flag = True
        time_end = datetime.datetime.now()
        self.MyLogger.info (f'Stopped parking timer {time_end}')

        return True
        

# def main():
#     parking_timer = ParkingTimer()
#     parking_timer.start_timer()
#     time.sleep(1)
#     parking_timer.end_timer()

#     parking_time = parking_timer.calculation_time()
#     print(f"The car was parked for {parking_time:.2f} second")

    
#     print(parking_timer.calculation_to_days())
#     print(parking_timer.calculation_to_week())
#     print(parking_timer.calculation_to_months())

#     print(parking_timer.start_timer_to_one_hour(1))
#     print(parking_timer.stop_timer())


# if __name__ == "__main__":
#     main()