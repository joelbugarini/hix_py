# the lexer must analyze a string and return a list of tokens for future
def execute(template):
    print("lexer started" + template)
    result = []
    token_list = get_tokens()
    giberish = ""
    for i, c in enumerate(template):
        print(i + giberish)


#        if c == "[":


def tokens():
    return [
        "model",
        "/model",
        "model.name",
        "prop",
        "/prop",
        "prop.name"
    ]


def get_tokens():
    return map(delimiters, tokens())


def delimiters(t):
    return "[[" + t + "]]"
