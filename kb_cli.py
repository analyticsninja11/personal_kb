import sys
from datetime import datetime
from kb_models import KBManager, Email, PersonalFile, Link, Video, PersonalNote
# ===== INPUT VALIDATION HELPER =====

def get_valid_input(prompt: str, min_length: int = 1, max_length: int = 200) -> str:
    """Get and validate user input with immediate feedback"""
    while True:
        value = input(prompt).strip()
        
        if not value:
            print("❌ Cannot be empty")
            continue
        
        if len(value) < min_length:
            print(f"❌ Too short (min {min_length} chars)")
            continue
        
        if len(value) > max_length:
            print(f"❌ Too long (max {max_length} chars)")
            continue
        
        return value  # ✅ Valid input, return it

def delete_item(kb: KBManager):
    """Delete an item from KB"""
    # First, list items so user can see what to delete
    items = kb.list_items()
    
    if not items:
        print("❌ No items to delete")
        return
    
    print(f"\n📚 Found {len(items)=} items:")
    for i, item in enumerate(items, 1):
        icon = get_source_icon(item.source)
        print(f"{i}. {icon} {item.title}")
    
    # Ask which one to delete
    try:
        choice = get_valid_input("\nEnter item number to delete (or 0 to cancel): ", min_length=1, max_length=3)
        item_num = int(choice)
        
        if item_num == 0:
            print("❌ Cancelled")
            return
        
        if item_num < 1 or item_num > len(items):
            print("❌ Invalid item number")
            return
        
        # Delete the item
        item_to_delete = items[item_num - 1]
        del kb.items[item_to_delete.id]
        print(f"✅ Deleted: {item_to_delete.title}")
        
    except ValueError:
        print("❌ Please enter a valid number")

def main():
    kb = KBManager()
    
    while True:
        print("\n=== Personal KB ===")
        print("1. Add email")
        print("2. Add file")
        print("3. Add link")
        print("4. Add video")
        print("5. Add note")
        print("6. List items")
        print("7. Search")
        print("8. Delete item")  # ← NEW!
        print("9. Save & Exit")  # Changed from 8 to 9
        
        choice = input("\nChoice (1-9): ").strip()
        
        match choice:
            case "1":
                add_email(kb)
            case "2":
                add_file(kb)
            case "3":
                add_link(kb)
            case "4":
                add_video(kb)
            case "5":
                add_note(kb)
            case "6":
                list_items(kb)
            case "7":
                search_items(kb)
            case "8":
                delete_item(kb)  # ← NEW!
            case "9":
                kb.save()
                print("👋 Goodbye!")
                break
            case _:
                print("❌ Invalid choice")
                
def get_source_icon(source: str) -> str:
    """Get emoji icon for KB source"""
    match source:
        case "email":
            return "📧"
        case "file":
            return "📄"
        case "link":
            return "🔗"
        case "video":
            return "🎥"
        case "note":
            return "📝"
        case _:
            return "❓"
        
def add_email(kb: KBManager):
    """Add an email to KB with immediate validation"""
    sender = get_valid_input("Sender: ", min_length=1, max_length=100)
    subject = get_valid_input("Subject: ", min_length=1, max_length=200)
    content = get_valid_input("Email content: ", min_length=1, max_length=5000)
    
    email = Email(
        id=f"email_{datetime.now().timestamp()}",
        title=subject,
        content=content,
        source_id=f"gmail_{datetime.now().timestamp()}",
        sender=sender,
        recipients=["you@example.com"],
        subject=subject
    )
    kb.add_item(email)


def add_file(kb: KBManager):
    """Add a file to KB with immediate validation"""
    filepath = get_valid_input("File path: ", min_length=1, max_length=500)
    title = get_valid_input("Title: ", min_length=1, max_length=200)
    
    file_item = PersonalFile(
        id=f"file_{datetime.now().timestamp()}",
        title=title,
        content=f"File: {filepath}",
        source_id=filepath,
        filepath=filepath,
        file_type=filepath.split(".")[-1] if "." in filepath else "unknown",
        size_bytes=0
    )
    kb.add_item(file_item)


def add_link(kb: KBManager):
    """Add a link to KB with immediate validation"""
    url = get_valid_input("URL: ", min_length=5, max_length=500)
    title = get_valid_input("Title: ", min_length=1, max_length=200)
    description = input("Description (optional): ").strip()  # Optional, no validation
    
    # Extract domain from URL using walrus + string manipulation
    if (domain := url.replace("https://", "").replace("http://", "").split("/")[0]):
        link = Link(
            id=f"link_{datetime.now().timestamp()}",
            title=title,
            content=description,
            source_id=url,
            url=url,
            domain=domain,
            description=description
        )
        kb.add_item(link)

def add_video(kb: KBManager):
    """Add a video to KB with immediate validation"""
    url = get_valid_input("Video URL: ", min_length=5, max_length=500)
    title = get_valid_input("Title: ", min_length=1, max_length=200)
    channel = input("Channel (optional): ").strip()  # Optional, no validation
    
    video = Video(
        id=f"video_{datetime.now().timestamp()}",
        title=title,
        content=f"Video: {title}",
        source_id=url,
        url=url,
        platform="youtube",
        channel=channel if channel else None
    )
    kb.add_item(video)


def add_note(kb: KBManager):
    """Add a personal note with immediate validation"""
    title = get_valid_input("Note title: ", min_length=1, max_length=200)
    content = get_valid_input("Note content: ", min_length=1, max_length=5000)
    category = input("Category (learning/insight/todo/idea): ").strip()  # Optional
    
    note = PersonalNote(
        id=f"note_{datetime.now().timestamp()}",
        title=title,
        content=content,
        source_id=f"note_{datetime.now().timestamp()}",
        category=category if category else "general"
    )
    kb.add_item(note)


def list_items(kb: KBManager):
    """List all items with fancy formatting"""
    source_filter = input("Filter by source (email/file/link/video/note/all): ").strip()
    
    items = kb.list_items() if source_filter == "all" else kb.list_items(source_filter)
    
    if not items:
        print("❌ No items found")
        return
    
    print(f"\n📚 Found {len(items)=} items:")
    for i, item in enumerate(items, 1):
        icon = get_source_icon(item.source)
        title = item.title[:30].ljust(30)  # ← Truncate and pad separately
        print(f"{i:2}. {icon} {title} ({item.source})")
        
def search_items(kb: KBManager):
    """Search KB items with fancy output"""
    query = input("Search query: ").strip()
    
    # Using walrus from Lesson 1!
    if (results := kb.search(query)):
        print(f"\n🔍 Found {len(results)=} results for '{query}':")
        for i, item in enumerate(results, 1):
            icon = get_source_icon(item.source)
            print(f"{i}. {icon} {item.title}")
            # Optional: show first 50 chars of content
            preview = item.content[:50] + "..." if len(item.content) > 50 else item.content
            print(f"   {preview}")
    else:
        print(f"❌ No results found for '{query}'")


def debug_item(item):
    """Debug print an KB item (useful for testing)"""
    print("\n=== KB Item Debug ===")
    print(f"{item.id=}")
    print(f"{item.title=}")
    print(f"{item.source=}")
    print(f"{item.created_at=}")
    print(f"{len(item.tags)=}")
    if hasattr(item, 'url'):
        print(f"{item.url=}")
    print("====================\n")
if __name__ == "__main__":
    main()