import sys
major,minor,patch = 0,0,0

with open('gradle.properties','r') as f:
    versionnumber = f.readline().split("=")
    major,minor,patch = versionnumber[1].split(".")


#print(major,minor,patch)

# take user input
inp = sys.argv[1]

def switch_func(inp):
    global major, minor, patch
    if inp == 'major':
        major = int(major)+1
        minor = 0
        patch =0

        return(str(major)+'.'+str(minor)+'.'+str(patch))

    elif inp == 'minor':
        major = int(major)
        minor = int(minor)+1
        patch = 0

        return(str(major)+'.'+str(minor)+'.'+str(patch))

    elif inp == 'patch':
        major = int(major)
        minor = int(minor)
        patch = int(patch)+1

        return(str(major)+'.'+str(minor)+'.'+str(patch))

    else:
        major = int(major)
        minor = int(minor)
        patch = int(patch)

        return(str(major)+'.'+str(minor)+'.'+str(patch))

print(switch_func(inp))
