# extract-GitHub-links

extract GitHub links from text files. 

# Extract GitHub Links from Text File

This project helps you extract all GitHub links from a large text file into a separate file. The script filters lines starting with `https://github.com/` and outputs them to a new file, making it easy to isolate and manage relevant links.

---

## Features
- Extracts valid GitHub repository links (e.g., `https://github.com/user/repo`) from a text file.
- Handles large files efficiently.
- Supports customizable input and output filenames.

---

## Prerequisites
- **Python**: Make sure Python 3.x is installed on your system.
  - Check your Python version:
    ```bash
    python --version
    ```

---

## Steps to Use

1. **Prepare Your Environment**:
   - Create or locate a folder where you'll store the script and files.
   - Ensure the text file you want to process is in the same folder. For example, name it `input.txt`.

2. **Create the Python Script**:
   - Open a text editor (e.g., Notepad, VS Code, or Sublime Text).
   - Copy and paste the script from the [`extract_github_links.py`](extract_github_links.py) file in this repository.
   - Save the file in the folder as `extract_github_links.py`.

3. **Run the Script**:
   - Open your terminal or command prompt.
   - Navigate to the folder where you saved the script:
     ```bash
     cd path/to/your/folder
     ```
   - Run the script using Python:
     ```bash
     python extract_github_links.py
     ```

4. **Check the Output**:
   - After running the script, a new file named `github_links.txt` will be created in the same folder.
   - This file will contain all the extracted GitHub links, one per line.

---

## Input and Output Example

### Input (`input.txt`):
```plaintext
Some random text
https://github.com/user/repo1
Another line of text
https://github.com/org/repo2
More random text
```

### Output (`github_links.txt`):
```plaintext
https://github.com/user/repo1
https://github.com/org/repo2
```

---

## Troubleshooting
- **Encoding Issues**: If you encounter errors related to character encoding (e.g., `UnicodeDecodeError`), ensure your input file is encoded in UTF-8. If the issue persists, adjust the script to use a different encoding (e.g., `latin-1` or `cp1252`).

- **File Not Found**: Ensure `input.txt` exists in the same directory as the script.

---

## Contributing
Feel free to suggest improvements or report bugs via issues!
