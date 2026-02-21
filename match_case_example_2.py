def classify_kb_item(source):
    """Classify KB items by source"""
    match source:
        case "email":
            return "📧 Email Item"
        case "file" | "pdf" | "docx":  # Multiple patterns!
            return "📄 File Item"
        case "link" | "bookmark":
            return "🔗 Link Item"
        case "video":
            return "🎥 Video Item"
        case "note":
            return "📝 Note Item"
        case _:
            return "❓ Unknown"

# Test it
sources = ["email", "pdf", "docx", "video", "slack", "note"]
for source in sources:
    print(f"{source:10} → {classify_kb_item(source)}")