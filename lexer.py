import re

KEYWORDS = {"int", "float", "if", "else", "while", "return"}

token_specification = [
    ("NUMBER",   r"\d+"),
    ("ID",       r"[A-Za-z_]\w*"),
    ("OP",       r"[+\-*/=]"),
    ("SEMI",     r";"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("SKIP",     r"[ \t\n]+"),
    ("MISMATCH", r"."),
]

def lexical_analyzer(code):
    tokens = []
    regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specification)

    for match in re.finditer(regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == "ID" and value in KEYWORDS:
            kind = "KEYWORD"
        if kind == "SKIP":
            continue
        if kind == "MISMATCH":
            raise RuntimeError(f"Unexpected character: {value}")

        tokens.append((kind, value))
    return tokens


with open("input.txt") as f:
    code = f.read()

tokens = lexical_analyzer(code)

with open("tokens.txt", "w") as f:
    for token in tokens:
        f.write(str(token) + "\n")
