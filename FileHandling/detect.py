#File dectection

import os

file_path = "test.pdf"

if os.path.exists(file_path):
    print(f"File path {file_path} exists")
else:
    print(f"File path {file_path} does not exist")
