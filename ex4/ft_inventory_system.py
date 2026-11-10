import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]

    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name, qty_str = arg.split(":", 1)

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(qty_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    print(f"Got inventory: {inventory}")

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total_qty}")

    if total_qty > 0:
        for item in items:
            pct = (inventory[item] / total_qty) * 100
            print(f"Item {item} represents {round(pct, 1)}%")

        most_abundant = items[0]
        least_abundant = items[0]

        for item in items:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item
            if inventory[item] < inventory[least_abundant]:
                least_abundant = item

        print(f"Item most abundant:"
              f"{most_abundant} with quantity {inventory[most_abundant]}")
        print(f"Item least abundant:"
              f"{least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
