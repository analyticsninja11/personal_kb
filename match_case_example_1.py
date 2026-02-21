# The Problem: Old-style if/elif chains
def get_greeting_old(time_of_day):
    if time_of_day == "morning":
        return "Good morning! ☀️"
    elif time_of_day == "afternoon":
        return "Good afternoon! 🌤️"
    elif time_of_day == "evening":
        return "Good evening! 🌅"
    else:
        return "Hello! 👋"

# The Modern Way: Match/Case (cleaner!)
def get_greeting_new(time_of_day):
    match time_of_day:
        case "morning":
            return "Good morning! ☀️"
        case "afternoon":
            return "Good afternoon! 🌤️"
        case "evening":
            return "Good evening! 🌅"
        case _:  # _ means "anything else" (default)
            return "Hello! 👋"

# Test both
print("=== OLD WAY ===")
print(get_greeting_old("morning"))
print(get_greeting_old("evening"))
print(get_greeting_old("night"))

print("\n=== NEW WAY (Match/Case) ===")
print(get_greeting_new("morning"))
print(get_greeting_new("evening"))
print(get_greeting_new("night"))