import os
import re

def parse_line(line):
    """
    Parses a tree-style line.
    
    Removes any comment (anything after a '#'), then uses a regex to extract:
      - indent: leading whitespace (including any '│' characters which are replaced by spaces)
      - name: the folder or file name.
    Returns a tuple (indent_level, name).
    """
    # Remove comment portion and trailing spaces
    line_no_comment = line.split('#')[0].rstrip()
    # Pattern: capture any leading indent (spaces or vertical bars), optionally a branch symbol, then the name.
    pattern = r'^(?P<indent>[\s│]*)(?:├── |└── )?(?P<name>.*)$'
    match = re.match(pattern, line_no_comment)
    if match:
        indent_str = match.group('indent')
        # Replace any vertical bar with a space so only spaces remain.
        indent_spaces = indent_str.replace('│', ' ')
        # Assume 4 spaces per indent level.
        indent_level = len(indent_spaces) // 4
        name = match.group('name').strip()
        return indent_level, name
    else:
        return None, None

def create_structure_from_text(text):
    base_dir = os.getcwd()
    lines = text.splitlines()
    stack = []  # keeps track of folder names corresponding to indent levels

    for line in lines:
        indent_level, name = parse_line(line)
        if name is None or name == "":
            continue  # Skip empty lines
        
        # Determine if this is a folder (ends with '/') or a file.
        is_folder = name.endswith("/")
        # Remove trailing slash from folder names.
        name = name.rstrip("/")
        
        # Adjust the folder stack to the current indentation level.
        while len(stack) > indent_level:
            stack.pop()
        
        # Determine the current path from the stack.
        if stack:
            current_path = os.path.join(base_dir, *stack)
        else:
            current_path = base_dir

        full_path = os.path.join(current_path, name)
        if is_folder:
            os.makedirs(full_path, exist_ok=True)
            # Push folder name to stack so that any children are created within it.
            stack.append(name)
        else:
            # Ensure the parent folder exists, then create an empty file.
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(full_path, 'w').close()

def main():
    input_file = "folder_structure.txt"
    if os.path.exists(input_file):
        # Using errors="ignore" to bypass any decoding issues.
        with open(input_file, "r", encoding="utf-8", errors="ignore") as file:
            structure_text = file.read()
        create_structure_from_text(structure_text)
        print("✅ Folder structure created successfully!")
        os.remove(input_file)
    else:
        print("❌ No input file found!")

if __name__ == "__main__":
    main()
