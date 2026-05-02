import os


def list_files(directory):
    return os.listdir(directory)

if __name__ == '__main__':
    print(list_files('.'))