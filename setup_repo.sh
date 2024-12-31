#!/bin/bash

# Define directory structure
DIRS=("serve_folder" "tests" "docs")

# Ensure necessary directories exist
for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir "$dir"
        echo "Created directory: $dir"
    else
        echo "Directory already exists: $dir"
    fi
done

# Check LICENSE file (do not modify if it exists and is not empty)
if [ -f "LICENSE" ] && [ -s "LICENSE" ]; then
    echo "LICENSE file exists and is not empty. Skipping modification."
else
    echo "LICENSE file is missing or empty. Please add an MIT License manually if needed."
fi

# Populate README.md (if empty)
if [ ! -s "README.md" ]; then
    cat <<EOF > README.md
# HalcyonHTTPServer

A lightweight HTTP server designed for payload delivery, data collection, and file hosting. Perfect for educational purposes and initial red-teaming phases.

## Features
- File hosting from a specified directory.
- Optional payload delivery in Base64 format.
- Handles and logs POST requests.

## Installation
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/<username>/HalcyonHTTPServer.git
   cd HalcyonHTTPServer
   \`\`\`

2. Run the server:
   \`\`\`bash
   python3 http_server.py
   \`\`\`

## Usage
- Access files via \`http://<IP>:8080/<filename>\`.
- Retrieve payloads (if enabled) at \`http://<IP>:8080/payload\`.
- Send POST data to the server for logging.

## License
[MIT License](LICENSE)
EOF
    echo "Populated README.md with basic project description."
else
    echo "README.md exists and is not empty. Skipping modification."
fi

# Check http_server.py (ensure it exists but do not modify it)
if [ ! -f "http_server.py" ]; then
    touch http_server.py
    echo "Created an empty http_server.py file."
else
    echo "http_server.py exists. No modifications made."
fi

# Add placeholder content to serve_folder
if [ ! -f "serve_folder/example.txt" ]; then
    echo "This is an example file for testing HalcyonHTTPServer." > serve_folder/example.txt
    echo "Added example file to serve_folder."
else
    echo "Example file already exists in serve_folder."
fi

# Add placeholder test file
if [ ! -f "tests/test_server.py" ]; then
    cat <<EOF > tests/test_server.py
# Test script for HalcyonHTTPServer

def test_placeholder():
    assert True, "Replace this with actual tests."
EOF
    echo "Added placeholder test file to tests/test_server.py."
else
    echo "Test file already exists in tests directory."
fi

# Add placeholder documentation
if [ ! -f "docs/usage.md" ]; then
    echo "# Usage Guide" > docs/usage.md
    echo "Detailed usage instructions for HalcyonHTTPServer will go here." >> docs/usage.md
    echo "Added placeholder documentation to docs/usage.md."
else
    echo "Documentation file already exists in docs directory."
fi

# Summary
echo "Repository setup complete! Files and directories are now ready for use."

