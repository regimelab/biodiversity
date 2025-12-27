import os

def concatenate_md_files(directory='.'):
    content = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        content.append(f'# {filepath}\n\n{file_content}\n\n---\n\n')
                except Exception as e:
                    content.append(f'# Error reading {filepath}: {e}\n\n')
    return ''.join(content)

# Usage: prints the concatenated content
if __name__ == "__main__":
    result = concatenate_md_files()
    print(result)
  
