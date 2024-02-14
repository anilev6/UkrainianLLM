import re

def normalize_string_to_filename(s):
    # Remove any non-word character
    s = re.sub(r'\W+', '_', s)
    # Remove any leading or trailing underscores
    s = s.strip('_')
    # Convert to lowercase
    s = s.lower()
    return s
