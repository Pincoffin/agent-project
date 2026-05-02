import json

def list_tools():
    tools = [
        {'name': 'write_file', 'description': 'Write a file to disk.'},
        {'name': 'run_script', 'description': 'Run a .py or .bat script.'},
        {'name': 'list_tools', 'description': 'Show available tools.'}
    ]

if __name__ == '__main__':
    print(json.dumps(list_tools(), indent=4))