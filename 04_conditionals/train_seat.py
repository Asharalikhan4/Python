seat_type = input("Enter seat type (sleeper/AC/general/luxury").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds Available")
    case "ac":
        print("AC - Air Conditioned, comfy rides")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat types")