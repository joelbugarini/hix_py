# The idea here will be to create a tree for the generator to work
import node

def execute(lexer_result):
    for x in lexer_result:
        print(x[0] + " " +x[2])

#def syntax_checker(lexer_result):
#    for token in lexer_result:

