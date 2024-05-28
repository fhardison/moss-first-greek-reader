import sys
import json

# Load the JSON data
with open(sys.argv[1], "r") as f:
    data = json.load(f)

key = sys.argv[2]
print(data.keys())
# Get the "test" dict
test_dict = data.get(key)

# Check if "test" dict exists
if not test_dict:
    print("Error: 'test' key not found in JSON data.")
    exit()

for text_lines_dict in test_dict:
    # Get the "text_lines" dict

    # Check if "text_lines" dict exists
    if not text_lines_dict:
        print("Error: 'text_lines' key not found in 'test' dict.")
        exit()
    lines = text_lines_dict['text_lines']
    # Loop through each sub-dict in "text_lines" and print the "text" element
    for sub_dict in lines:
        text = sub_dict.get("text")
        if text:
            print(text)
        else:
            print("Error: 'text' key not found in sub-dict.")
