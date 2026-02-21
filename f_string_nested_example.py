# Traditional nested approach (messy)
source = "email"
title = "Important Meeting"
sender = "boss@company.com"

formatted_old = f"[{source}] {title} from {sender}"
print("Traditional:", formatted_old)

print("\n=== Nested F-Strings (Python 3.10+) ===")

# Modern: nested f-strings (cleaner!)
items = {
    "email": "📧",
    "file": "📄",
    "link": "🔗",
    "video": "🎥"
}

icon = items.get("email")
formatted_new = f"{icon} [{source}] {title} from {sender}"
print("With nested:", formatted_new)

# Even more complex
items_data = [
    ("email", "Meeting notes", "alice@example.com"),
    ("link", "Python guide", "https://example.com"),
    ("note", "Remember this", "me")
]

print("\n=== Multiple Items ===")
for source, title, sender in items_data:
    icon = items.get(source, "❓")
    print(f"{icon} [{source:6}] {title:20} | {sender}")
