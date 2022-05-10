import sys
import yaml
import lexer
import parser

# cli tool for hix basic usage
# hix generate [model] [template]

arguments = len(sys.argv) - 1

# Reading arguments
print("\nReading terminal arguments")
position = 1
while arguments >= position:
    print("Argument %i: %s" % (position, sys.argv[position]))
    position = position + 1

# Reading Model
model = sys.argv[2]
print("\nReading model from the file:"+model+".yaml")
# with open(model + ".yaml", 'r') as stream:
    # try:
    #    print(yaml.dump(yaml.safe_load(stream)))
    # except yaml.YAMLError as exc:
    #    print(exc)

# Reading Schema
template = sys.argv[1]
file = open(template + ".hix.html", "r")
# print("Lexer executed for " + template + ".hix.html")

# print(file.read())
lexer_result = lexer.execute(file.read())
file.close()

# Parsing tree
parser_result = parser.execute(lexer_result)
