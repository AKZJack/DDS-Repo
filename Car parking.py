import datetime

class CarNode:
    """Represents a node in the linked list for a parked car."""
    def __init__(self, car_number, slot_number, entry_time):
        self.car_number = car_number
        self.slot_number = slot_number
        self.entry_time = entry_time
        self.next = None

class SmartParkingLot:
    """Manages the parking lot with a linked list for parked cars."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied_slots = 0
        self.parking_slots = [None] * capacity  # Dynamic memory allocation for slots
        self.head = None  # Head of the linked list of parked cars

    def park_car(self, car_number):
        """Parks a car in an available slot."""
        if self.occupied_slots >= self.capacity:
            print("Parking lot is full! Cannot park the car.")
            return

        # Find the first available slot
        slot_number = -1
        for i in range(self.capacity):
            if self.parking_slots[i] is None:
                slot_number = i
                break
        
        # This check is redundant due to the capacity check, but good practice
        if slot_number == -1:
            print("Error: No empty slot found.")
            return

        # Create a new car node and add it to the linked list
        new_car_node = CarNode(car_number, slot_number, datetime.datetime.now())
        new_car_node.next = self.head
        self.head = new_car_node

        # Update parking lot status
        self.parking_slots[slot_number] = car_number
        self.occupied_slots += 1
        
        print(f"Car '{car_number}' parked in slot {slot_number + 1}.")
        print(f"Entry time: {new_car_node.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def unpark_car(self, car_number):
        """Removes a car from the parking lot."""
        current = self.head
        previous = None

        # Search for the car in the linked list
        while current and current.car_number != car_number:
            previous = current
            current = current.next

        # Car not found
        if current is None:
            print(f"Car '{car_number}' is not found in the parking lot.")
            return

        # Unlink the node from the linked list
        if previous is None:
            # The car to unpark is the head
            self.head = current.next
        else:
            previous.next = current.next

        # Update parking lot status
        self.parking_slots[current.slot_number] = None
        self.occupied_slots -= 1

        # Calculate parking duration and cost (example logic)
        exit_time = datetime.datetime.now()
        duration = exit_time - current.entry_time
        hours = duration.total_seconds() / 3600
        cost = hours * 2  # Example: $2 per hour

        print(f"Car '{car_number}' unparked from slot {current.slot_number + 1}.")
        print(f"Duration: {duration.seconds // 3600} hours, {(duration.seconds % 3600) // 60} minutes.")
        print(f"Total cost: ${cost:.2f}")

        # In Python, memory deallocation is automatic; no explicit `free()` call needed.
        # The `current` object will be garbage collected when no longer referenced.

    def display_status(self):
        """Displays the current status of the parking lot."""
        print("\n--- Parking Lot Status ---")
        print(f"Total Slots: {self.capacity}")
        print(f"Occupied Slots: {self.occupied_slots}")
        print(f"Available
