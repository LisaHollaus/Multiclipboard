import sys
import clipboard
import json

# clipboard.copy('Hello world!')  # copies the string 'Hello world!' to the clipboard
SAVED_DATA = 'clipboard.json'


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}


if 2 <= len(sys.argv) <= 3:  # sys.argv is a list of command line arguments
    command = sys.argv[1]  # get the command from the command line
    if len(sys.argv) > 2:
        key = sys.argv[2] # get the key from the command line if it exists
    else:
        key = None
    data = load_data(SAVED_DATA)  # load the data from the file

    if command == 'save':
        if key is None:
            key = input('Enter the key: ')
        data[key] = clipboard.paste()  # gets the clipboard's content
        save_data(SAVED_DATA, data)  # save the data to the file
        print('Data saved successfully!')

    elif command == 'load':
        if key is None:
            key = input('Enter the key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data loaded successfully!')
        else:
            print('The key does not exist.')

    elif command == 'list':
        print('Listing clipboard content...')
        for key, value in data.items():
            print(f'{key}: {value}')

    # optional: add a delete command
    # (not necessary for the project, because we can just use the save command to overwrite the key)

    else:
        print('Invalid command. Please use save, load or list.')

else:
    print('Please provide a command. Use save, load or list.')