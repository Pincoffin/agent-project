def create_python_tool(name, description, code):
    tool_code = f"'''
{name}
{description}
'''
    return {{
        'type': 'tool',
        'name': '{name}',
        'code': {code},
        'description': '{description}'
    }}"

# Example usage:
tool = create_python_tool('example_tool', 'An example tool for demonstration.', "{'type': 'object', 'args': {'path': 'string (required)', 'content': 'string (required)'}}")
print(tool)
