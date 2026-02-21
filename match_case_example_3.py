def process_kb_value(value):
    """Process different types of KB values"""
    match value:
        case int():
            return f"Integer: {value}"
        case str():
            return f"String: {value}"
        case list():
            return f"List with {len(value)} items"
        case dict():
            return f"Dictionary with {len(value)} keys"
        case _:
            return "Unknown type"

# Test it
test_values = [42, "hello", ["a", "b", "c"], {"key": "value"}, 3.14]
for val in test_values:
    print(process_kb_value(val))