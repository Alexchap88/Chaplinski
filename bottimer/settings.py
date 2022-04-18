import os

with open ('.env', 'r') as file:
    line = file.readline()
    try:
        os.environ[line[:line.find('=')]] = line[line.find('=') + 1:]
    except ValueError:
        pass
TOKEN = os.environ[TOKEN]