from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

# Base class for all KB items
class KBItem(BaseModel):
    """Base class for any knowledge item in your KB"""
    id: str
    title: str = Field(..., min_length=1, max_length=200)
    content: str
    source: Literal["email", "file", "link", "video", "note"]
    source_id: str  # Gmail ID, file path, URL, video ID, etc.
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    url: str | None = None  # For links/videos


# Specific types
class Email(KBItem):
    """Email item from Gmail"""
    source: Literal["email"] = "email"
    sender: str
    recipients: list[str]
    subject: str


class PersonalFile(KBItem):
    """File item (PDF, DOCX, TXT)"""
    source: Literal["file"] = "file"
    filepath: str
    file_type: str  # pdf, docx, txt, md, etc.
    size_bytes: int


class Link(KBItem):
    """Bookmarked link"""
    source: Literal["link"] = "link"
    url: str = Field(..., min_length=5)
    domain: str  # example.com
    description: str = ""


class Video(KBItem):
    """Video item (YouTube, etc.)"""
    source: Literal["video"] = "video"
    url: str
    platform: str  # youtube, vimeo, etc.
    duration_seconds: int | None = None
    channel: str | None = None


class PersonalNote(KBItem):
    """Personal note or idea"""
    source: Literal["note"] = "note"
    category: str = "general"  # learning, insight, todo, idea, etc.


# Union type for any KB item
KBItemType = Email | PersonalFile | Link | Video | PersonalNote

import json
from pathlib import Path

class KBManager:
    """Manage KB items - add, list, search, save"""
    
    def __init__(self, storage_path: str = "kb_storage.json"):
        self.storage_path = Path(storage_path)
        self.items: dict[str, KBItemType] = {}
        self.load()
    
    def add_item(self, item: KBItemType) -> None:
        """Add item to KB"""
        self.items[item.id] = item
        print(f"✅ Added: {item.title} ({item.source})")
    
    def list_items(self, source: str | None = None) -> list[KBItemType]:
        """List all items, optionally filtered by source"""
        if source:
            return [item for item in self.items.values() if item.source == source]
        return list(self.items.values())
    
    def search(self, query: str) -> list[KBItemType]:
        """Search items by title or content"""
        query_lower = query.lower()
        results = [
            item for item in self.items.values()
            if query_lower in item.title.lower() or query_lower in item.content.lower()
        ]
        return results
    
    def save(self) -> None:
        """Save KB to JSON file"""
        data = {
            item_id: {
                "type": item.source,
                "data": item.model_dump()  # Pydantic method
            }
            for item_id, item in self.items.items()
        }
        with open(self.storage_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        print(f"💾 Saved {len(self.items)} items")
    
    def load(self) -> None:
        """Load KB from JSON file"""
        if not self.storage_path.exists():
            print("📁 No existing KB found, starting fresh")
            return
        
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
        
        for item_id, item_data in data.items():
            item_type = item_data["type"]
            item_dict = item_data["data"]
            
            # Reconstruct the right type
            if item_type == "email":
                self.items[item_id] = Email(**item_dict)
            elif item_type == "file":
                self.items[item_id] = PersonalFile(**item_dict)
            elif item_type == "link":
                self.items[item_id] = Link(**item_dict)
            elif item_type == "video":
                self.items[item_id] = Video(**item_dict)
            elif item_type == "note":
                self.items[item_id] = PersonalNote(**item_dict)
        
        print(f"📖 Loaded {len(self.items)} items")