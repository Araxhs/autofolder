# autofolder
AutoFolder: AI-Powered Folder Structure Creator, ## Features - Parses tree-style input (e.g., `├──`, `└──`) from AI chatbots. - Creates both folders (ending with `/`) and files. - Ignores comments (after `#`) and empty lines for clean processing. - Lightweight with no external dependencies.
## How to Use
1. **Run the Batch File:**
   - On Windows, double-click `create_structure.bat` or run it from the command prompt.
2. **Paste the Structure:**
   - Copy the folder structure from your AI chatbot (e.g., ChatGPT).
   - Paste it into the terminal.
   - Press `Ctrl+Z` and then `Enter` to finish input.
3. **Watch It Work:**
   - The script creates the folders and files in your current directory.

## Example
Paste this:

project/
├── css/
│   └── style.css
├── lessons/
│   ├── lesson1.html
│   ├── lesson2.html
│   ├── lesson3/
│   │   ├── page1.html
│   │   ├── page2.html
│   │   └── page3.html
│   ├── lesson4.html
│   ├── lesson5/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson6/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson7/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson8.html
│   ├── lesson9/
│   │   ├── page1.html
│   │   ├── page2.html
│   │   └── page3.html
│   ├── lesson10/
│   │   ├── page1.html
│   │   ├── page2.html
│   │   └── page3.html
│   ├── lesson11/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson12/
│   │   ├── page1.html
│   │   ├── page2.html
│   │   ├── page3.html
│   │   └── page4.html
│   ├── lesson13/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson14/
│   │   ├── page1.html
│   │   └── page2.html
│   ├── lesson15.html
│   ├── lesson16.html
│   ├── lesson17.html
│   └── lesson18/
│       ├── page1.html
│       └── page2.html
└── index.html 


## Requirements
- **Operating System:** Windows (for the batch file).
- **Python:** Version 3.x installed (check with `python --version`).
