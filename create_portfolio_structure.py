import os

# Define base folder path
base_path = "E:/wangdi_portfolio"

# Subfolders to create
folders = [
    "files",
    "images",
    "scripts"
]

# HTML files to create
html_files = [
    "index.html",
    "about.html",
    "research_projects.html",
    "publications.html",
    "skills.html",
    "awards.html",
    "cv.html",
    "contact.html"
]

# Other files
other_files = [
    "style.css",
    "README.md"
]

# Create base folder
os.makedirs(base_path, exist_ok=True)

# Create subfolders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create HTML files
for file in html_files:
    file_path = os.path.join(base_path, file)
    with open(file_path, 'w') as f:
        f.write('')  # create empty HTML files

# Create other files
for file in other_files:
    file_path = os.path.join(base_path, file)
    with open(file_path, 'w') as f:
        f.write('')  # create empty other files

print(f"Website structure with all 8 sections created successfully at {base_path}")
