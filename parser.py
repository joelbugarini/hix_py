# The idea here will be to create a tree for the generator to work
import node


def execute(lexer_result):
    root = node.ParserNode("", "", "root", "root")
    for res in lexer_result:
        root.add(node.ParserNode(res.))