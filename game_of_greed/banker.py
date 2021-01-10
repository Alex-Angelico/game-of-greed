class Banker:
    """
    Description: Builds banker objects used for tracking points obtained from dice rolls, and permanent storage.

    Methods:
    __init__
        Args:
            self: Banker object instance containing logic for manipulating and storing points from dice rolls.
            shelved: Integer of points from dice rolls in temporary storage
            balance: Integer of shelved points in permanent storage
        Returns:
            None

    shelf
        Args:
            self: Banker object instance
            shelf_points: Integer of points being moved to shelved
        Returns:
            None

    bank
        Args:
            self: Shelf object instance of points
        Returns:
            balance: Shelved points moved to permanent storage

    clear_shelf
        Args:
            self: Shelf object instance of points
        Returns:
            None

    """

    def __init__(self, shelved=0, balance=0):
        self.shelved = shelved
        self.balance = balance

    def shelf(self, shelf_points):
        self.shelved += shelf_points

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0


if __name__ == "__main__":
    banker = Banker()
    banker.shelf(10000)
    banker.clear_shelf()
