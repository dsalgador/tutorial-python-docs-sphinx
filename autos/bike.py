class Bike:

    def __init__(self, name: str):
        """Constructor

        Args:
            name (str): [description]
        """
        self.name = name

    def ride(self, road : str) -> bool:
        """Ride

        Args:
            road (str): Road name to ride on

        Returns:
            bool: True if successful
        """
        print("Riding: %s on road: %s" % (self.name, road))
        return True
