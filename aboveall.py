# program controller
import sys, subprocess, os

if len(sys.argv) < 2:
    print('Usage: python aboveall.py <script_id>')
    sys.exit(1)

script_id=sys.argv[1]

for file in os.listdir(): # loops through all files in current dir
    if file.endswith('.py') and file != os.path.basename(__file__): # if file ends with .py and is not the current program
        if file.startswith(script_id):
            print(f'Running: {file}')
            subprocess.run(['python',file])
            break
else:
    print(f'No script starting with {script_id} is found!')