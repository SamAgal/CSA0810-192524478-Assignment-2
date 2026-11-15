"""Task 5: Functions, Parameters and Scope (College Canteen Order System)."""

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

if __name__ == "__main__":
    print("--- Buggy Function Calls ---")
    print("Customer 1:", add_item_buggy("Tea"))
    print("Customer 2:", add_item_buggy("Vada"))
    
    print("\n--- Corrected Function Calls ---")
    print("Customer 1:", add_item("Tea"))
    print("Customer 2:", add_item("Vada"))
    
    print("\nadd_item_buggy.__defaults__:", add_item_buggy.__defaults__)
