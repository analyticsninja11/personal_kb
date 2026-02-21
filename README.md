# Personal Knowledge Base (KB) CLI

A Python command-line application for managing your personal knowledge base. Store, organize, and search emails, files, links, videos, and notes all in one place.

**Status:** Week 1 Complete ✅

---

## Features

- **Add Items** - Create KB items from multiple sources:
  - 📧 Emails (sender, subject, recipients)
  - 📄 Files (PDF, DOCX, TXT, etc.)
  - 🔗 Links (bookmarks with domain info)
  - 🎥 Videos (YouTube links with channel info)
  - 📝 Notes (personal thoughts and ideas)

- **List Items** - View all KB items with filtering by source type
- **Search** - Find items by title or content with preview
- **Delete Items** - Remove items from your KB
- **Persistent Storage** - Save to JSON file, automatically loads on restart

- **Input Validation** - Immediate feedback on invalid input
- **Modern Python** - Uses Python 3.10+ features (match/case, union types, f-strings)
- **Type Safety** - Pydantic validation for all data models

---

## Installation

### Requirements
- Python 3.10+
- Pydantic v2

### Setup

```bash
# Clone the repository
git clone https://github.com/analyticsninja11/personal_kb.git
cd personal_kb

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install pydantic
```

---

## Usage

```bash
# Start the KB CLI
python kb_cli.py
```

### Menu Options

```
=== Personal KB ===
1. Add email
2. Add file
3. Add link
4. Add video
5. Add note
6. List items
7. Search
8. Delete item
9. Save & Exit
```

### Examples

**Add an Email:**
```
Choice (1-8): 1
Sender: alice@example.com
Subject: Python Learning Progress
Email content: Learning async/await patterns
✅ Added: Python Learning Progress (email)
```

**Search for Items:**
```
Choice (1-8): 7
Search query: async
🔍 Found len(results)=2 results for 'async':
1. 📧 Learning async patterns
   Study event loops and coroutines
2. 🎥 Async Python Tutorial
   Advanced async/await concepts
```

**List Items with Filter:**
```
Choice (1-8): 6
Filter by source (email/file/link/video/note/all): all
📚 Found len(items)=10 items:
1. 📧 Thanks and Congratulations on your new role
2. 🔗 Vibe coding - Andreas Horn
3. 📝 This is a great start to the week of learning
...
```

**Delete an Item:**
```
Choice (1-8): 8
📚 Found len(items)=10 items:
1. 📧 Important email
2. 🔗 Python docs
...
Enter item number to delete (or 0 to cancel): 1
✅ Deleted: Important email
```

---

## Project Structure

```
personal_kb/
├── kb_cli.py           # CLI interface and user interactions
├── kb_models.py        # Pydantic data models
├── kb_storage.json     # Persistent storage (auto-created)
└── README.md           # This file
```

---

## Data Models

All KB items are validated using **Pydantic v2**:

### Base Model
```python
class KBItem(BaseModel):
    id: str
    title: str (1-200 chars)
    content: str
    source: Literal["email", "file", "link", "video", "note"]
    source_id: str
    tags: list[str]
    created_at: datetime
    updated_at: datetime
    url: str | None
```

### Specific Types
- **Email**: sender, recipients, subject
- **PersonalFile**: filepath, file_type, size_bytes
- **Link**: url, domain, description
- **Video**: url, platform, duration_seconds, channel
- **PersonalNote**: category (learning/insight/todo/idea)

---

## Validation

### Input Validation
- Blank field detection (immediate feedback)
- Length constraints (min/max characters)
- Type checking via Pydantic

### Example Error Messages
```
❌ Sender cannot be empty
❌ Subject too long (max 200 chars)
❌ URL too short (min 5 chars, e.g., http://)
```

---

## Technologies & Patterns

### Modern Python (3.10+)
- ✅ Match/case statements (pattern matching)
- ✅ Union types with `|` operator
- ✅ F-string debug syntax `f"{var=}"`
- ✅ Walrus operator `:=`
- ✅ Type hints with `Literal` and `|`

### Design Principles
- ✅ DRY (Don't Repeat Yourself)
- ✅ Single Responsibility Principle
- ✅ Helper functions for reusability
- ✅ Layered validation (input + Pydantic)

### Code Quality
- Type hints throughout
- Input validation before Pydantic
- Immediate user feedback
- Clean, readable code structure

---

## Future Features (Planned)

- [ ] Edit existing items
- [ ] Filter by tags
- [ ] Export to text file
- [ ] View full item details
- [ ] Tag management
- [ ] Gmail API integration (Week 7)
- [ ] Google Drive integration (Week 7)
- [ ] YouTube integration (Week 7)
- [ ] Browser bookmarks import (Week 7)
- [ ] Vector database for semantic search (Week 9+)
- [ ] LLM-powered Q&A (Week 9+)

---

## Learning Context

This project is part of an **8-week Python mastery curriculum**:

**Week 1:** Modern Python Syntax (walrus, union types, match/case, f-strings)
- Completed: Personal KB CLI with validation ✅

**Weeks 2-8:** Progressive complexity
- Week 2: Type hints & Pydantic
- Week 3: Advanced patterns
- Week 4: Decorators & context managers
- Week 5: Generators & advanced decorators
- Week 6: Testing & code quality
- Week 7: Async/await & API integration
- Week 8: Production system architecture

---

## Notes

- KB items are stored in `kb_storage.json` (auto-created)
- Each item has a unique ID (timestamp-based)
- Datetime fields use ISO 8601 format
- JSON file is human-readable for inspection

---

## Author

Ghanasham Apte - Python Learning Journey 2026

---

## License

MIT

---

## Getting Help

**Issues?**
- Check that Python 3.10+ is installed: `python --version`
- Verify Pydantic installed: `pip list | grep pydantic`
- Check `kb_storage.json` exists and is readable

**Want to learn more?**
- See: `LESSON_1_MODERN_PYTHON_SYNTAX.md` for syntax deep-dive
- See: `PYDANTIC_EXPLAINED.md` for validation details
- See: `THURSDAY_SESSION_NOTES.md` for design principles

---

*Last updated: February 22, 2026*
*Week 1 Complete - Ready for Week 2!* 🚀
