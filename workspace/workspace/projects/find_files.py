import os

def find_files(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))

if __name__ == '__main__':
    find_files('.', '.py')