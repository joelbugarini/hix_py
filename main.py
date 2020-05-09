import sys
import yaml

# cli tool for hix must contain
# hix generate [model] [template]

arguments = len(sys.argv) - 1

# Reading arguments
position = 1
while arguments >= position:
    print("Parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
model = sys.argv[2]

# Reading Model
with open(model + ".yaml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

# Reading Schema
template = sys.argv[3]
file = open(template + ".hix.html", "r")

print(file.read())

file.close()
