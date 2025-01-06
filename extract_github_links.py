import re

# File names
input_file = 'input.txt'
output_file = 'github_links.txt'

try:
    # Open the input file with UTF-8 encoding and read all lines
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Use a list comprehension with regex to filter GitHub links
    github_links = [line.strip() for line in lines if re.match(r'^https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', line.strip())]

    # Check if we found any GitHub links
    if github_links:
        # Write the filtered links to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(github_links) + '\n')
        print(f"✅ Extracted {len(github_links)} GitHub links into '{output_file}'.")
    else:
        print("⚠️ No GitHub links were found in the input file.")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_file}' was not found. Please check the file name and try again.")
except UnicodeDecodeError as e:
    print(f"❌ Encoding error: {e}. Try opening the file with a different encoding.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
