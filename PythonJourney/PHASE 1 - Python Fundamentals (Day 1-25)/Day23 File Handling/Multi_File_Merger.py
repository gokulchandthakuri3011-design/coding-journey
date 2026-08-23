"""
### Assignment 6: Multi-File Merger (Hard)

Create a program that:
1. Takes multiple text files as input
2. Merges their contents into a single file
3. Adds a header before each file's content showing the filename
4. Handles missing files gracefully

**Expected Output in `merged.txt`:**
```
===== FILE: file1.txt =====
Content of file1...

===== FILE: file2.txt =====
Content of file2...
"""
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Reading any file gracefully
def read_file(filename):
    try:
        with open(os.path.join(BASE_DIR, filename), "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: {filename} not found — skipping.")
        return None

# Using main() for calling the function
def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    sections = []
    for name in files:
        content = read_file(name)
        if content is not None:
            sections.append(f"==== FILE: {name} ====\n{content}\n")

    # Writing all sections at once ("w" = fresh file each run, no duplicates)
    with open(os.path.join(BASE_DIR, "merged.txt"), "w") as file:
        file.write("\n".join(sections)) # adds \n between each elements in list

    # Printing the data in merged file for confirmation
    with open(os.path.join(BASE_DIR, "merged.txt"), "r") as file:
        print(file.read())

if __name__ == "__main__":
    main()
