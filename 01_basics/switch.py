command = "start"

match command:
    case "start":
        print("System Launching...")
    case "stop":
        print("System shutting down...")
    case _:
        print("Unknown command shortcut.")