from decorators.decorators import timer
from random import randint

@timer
def waste_some_time(num_times):
    """
    A sample function to demonstrate performance measurement.
    It performs a computationally intensive operation (sum of squares)
    multiple times to generate some measurable workload.
    """
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


def transform_matrix(matrix):
    """
    Transform a 2D matrix of integers into a dictionary mapping each value
    to its square. Demonstrates a nested comprehension.
    """
    return {value: value**2 for row in matrix for value in row}


def fruit_lengths(fruits):
    """
    Convert a list of fruit names into a dictionary mapping each fruit
    to the length of its name.
    """
    return {fruit: len(fruit) for fruit in fruits}


def create_inventory(parts, stocks):
    """
    Create a dictionary representing the inventory of parts and their stock counts.
    """
    return {part: stock for part, stock in zip(parts, stocks)}


def inventory_with_randomized_values(parts, stocks):
    """
    Example of adding some complexity by taking the stock of each part
    and raising it to a random power, then dividing by 100 to scale it.
    This could simulate some uncertain metric or 'score' for each part.
    """
    return {part: stock ** randint(1, 5) / 100 for part, stock in zip(parts, stocks)}


def compute_inventory_values(parts, stocks, costs):
    """
    Compute the total value of inventory (stock * cost) for each part.
    Returns a dictionary mapping each part to its total cost.
    """
    return {
        part: stock * cost
        for part, stock, cost in zip(parts, stocks, costs)
    }


def invert_dict(d):
    """
    Invert a dictionary mapping from key->value to value->key.
    Useful for reverse lookups.
    """
    return {value: key for key, value in d.items()}


def main():
    # 1. Performance Testing
    print("Measuring computational performance...\n")
    waste_some_time(100)

    # 2. Matrix Transformation
    matrix = [
        [9, 3, 8, 3],
        [4, 5, 2, 8],
        [6, 4, 3, 1],
        [1, 0, 4, 5],
    ]
    print("\nMatrix Transformation:")
    print(transform_matrix(matrix))

    # 3. Fruit Lengths
    fruits = ["apple", "banana", "cherry"]
    print("\nFruit Lengths:")
    print(fruit_lengths(fruits))

    # 4. Inventory Setup
    parts = [
        "CPU",
        "GPU",
        "Motherboard",
        "RAM",
        "SSD",
        "Power Supply",
        "Case",
        "Cooling Fan"
    ]
    stocks = [15, 8, 12, 30, 25, 10, 5, 20]
    print("\nInitial Inventory:")
    inventory = create_inventory(parts, stocks)
    print(inventory)

    # Another way to create the same inventory dictionary
    print("\nSame Inventory using dict and zip:")
    print(dict(zip(parts, stocks)))

    # Add complexity with random computations
    print("\nInventory Random Values (example metric):")
    print(inventory_with_randomized_values(parts, stocks))

    # Compute total values (stock * cost)
    part_costs = [250, 500, 150, 80, 100, 120, 70, 25]
    inventory_values = compute_inventory_values(parts, stocks, part_costs)
    print("\nInventory Total Values (Stock * Cost):")
    print(inventory_values)

    # Invert a dictionary of parts and their IDs
    part_ids = {
        "CPU": 10021,
        "GPU": 10022,
        "Motherboard": 10023,
        "RAM": 10024,
        "SSD": 10025,
        "Power Supply": 10027,
        "Case": 10026,
        "Cooling Fan": 10025, # Note: value not unique
    }
    print("\nInverted Parts Dictionary (IDs to Names):")
    print(invert_dict(part_ids))
    
    # Alternatively:
    print("\nInverted using zip (non-unique values may cause data loss):")
    print(dict(zip(part_ids.values(), part_ids.keys())))


if __name__ == "__main__":
    main()
