# the lexer must analyze a string and return a list of tokens for future parsing
# gibberish, are words that are (or appears to be) nonsense.


def execute(template):
    result = []
    gibberish = ""
    i = 0
    ln = 1
    col = 0
    position = "Ln 1, Col 0"
    position_behind = "Ln 1, Col 0"
    while i < len(template):
        c = template[i]
        if c == '\n':
            ln += 1
            col = 0
        else:
            col += 1
        if i + 1 == len(template):
            gibberish = gibberish + c
            result.append(("gibberish", gibberish, position))
            position = "Ln " + str(ln) + ", Col " + str(col)
            # for x in result:
            #    print(x[0])
            return result
            break
        if c + template[i + 1] == "[[":
            token_found = False
            for token in get_tokens():
                # print(i, template[i:len(token) + i], token)
                if token == template[i:len(token) + i]:
                    result.append(("gibberish", gibberish, position_behind))
                    position = "Ln " + str(ln) + ", Col " + str(col)
                    result.append((token, token, position))
                    position_behind = "Ln " + str(ln) + ", Col " + str(col + len(token))
                    i = i + len(token)
                    gibberish = ""
                    token_found = True
                    break
            if not token_found:
                gibberish = gibberish + c
                i = i + 1
        else:
            gibberish = gibberish + c
            i = i + 1


def get_tokens():
    return map(delimiters, tokens())


def tokens():
    return [
        "model",
        "/model",
        "model.name",
        "prop",
        "/prop",
        "prop.name"
    ]


def delimiters(t):
    return "[[" + t + "]]"
