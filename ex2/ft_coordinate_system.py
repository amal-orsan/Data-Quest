import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompts user for 3D coordinates until valid format is provided."""
    while True:
        try:
            user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            )
            parts = user_input.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            x_str, y_str, z_str = parts
            x, y, z = (
                float(x_str.strip()),
                float(y_str.strip()),
                float(z_str.strip())
            )
            return (x, y, z)

        except ValueError as e:
            err_msg = str(e)
            invalid_param = err_msg.split(":")[-1].strip()
            print(f"Error on parameter {invalid_param}: {err_msg}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coord1 = get_player_pos()

    print(f"Got a first tuple: {coord1}")

    x, y, z = coord1
    print(f"It includes: X={x}, Y={y}, Z={z}")

    dist_to_center = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("Get a second set of coordinates")
    coord2 = get_player_pos()

    # --- TUPLE UNPACKING USED HERE ---
    x2, y2, z2 = coord2
    dist_between = math.sqrt(
        (x2 - x)**2 +
        (y2 - y)**2 +
        (z2 - z)**2
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
