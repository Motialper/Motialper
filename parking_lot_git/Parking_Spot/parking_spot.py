class Parking_Spot:
    """
    A class to represent a parking spot.

    Attributes:
        id (int): The unique identifier of the parking spot.
        location (str): The location of the parking spot.
        occupied (bool): The occupancy status of the parking spot.

    Methods:
        get_id() -> int: Returns the unique identifier of the parking spot.
        get_location() -> str: Returns the location of the parking spot.
        get_occupied() -> bool: Returns the occupancy status of the parking spot.
        get_info() -> None: Prints the parking spot's id, location, and occupancy status.
        set_id(new_id: int) -> None: Sets the unique identifier of the parking spot.
        set_location(new_location: tuple) -> None: Sets the location of the parking spot.
        set_occupied() -> None: Sets the occupancy status of the parking spot to True.
    """
    def __init__(self, id: int, location: tuple) -> None:
        self.id = id
        self.location = location
        self.occupied = False

    def get_id(self) -> int:
        """Returns the unique identifier of the parking spot."""
        return self.id 
    
    def get_location(self) -> tuple:
        """Returns the location of the parking spot."""
        return self.location 

    def get_occupied(self) -> bool:
        """Returns the occupancy status of the parking spot."""
        return self.occupied 
    
    def get_info(self) -> None:
        """Prints the parking spot's id, location, and occupancy status."""
        print(f"The ID is {self.id}, The location is {self.location}, To say that the spot is occupied is {self.occupied}")

    def set_id(self, new_id: int) -> None:
        """Sets the unique identifier of the parking spot."""
        self.id = new_id

    def set_location(self, new_location: tuple) -> None:
        """Sets the location of the parking spot."""
        self.location = new_location

    def set_occupied(self) -> None:
        """Sets the occupancy status of the parking spot to True."""
        if self.occupied == True:
            self.occupied = False
        else :
            self.occupied ==False

class MotorcycleSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a motorcycle parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)

class CarSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a car parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)

class BusSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a bus parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)
