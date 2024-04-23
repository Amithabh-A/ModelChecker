"""
parser and AST generator for CTL formula 
"""

from ply import lex

# List of token names
tokens = (
    "AND",
    "OR",
    "NOT",
    "IMP",
    "AG",
    "EG",
    "AX",
    "EX",
    "AF",
    "EF",
    "A",
    "E",
    "U",
    "LPAREN",  # simple rule
    "RPAREN",  # simple rule
    "LSQUARE",  # simple rule
    "RSQUARE",  # simple rule
    "VAR",  # simple rule
    "T",  # Added token for true
    "N",  # Added token for false
)

# Regular expression rules for simple tokens
t_AND = r"AND"
t_OR = r"OR"
t_NOT = r"NOT"
t_IMP = r"IMP"
t_AG = r"AG"
t_EG = r"EG"
# t_AU = r"AU"
# t_EU = r"EU"
t_AX = r"AX"
t_EX = r"EX"
t_AF = r"AF"
t_EF = r"EF"
t_A = r"A"
t_E = r"E"
t_U = r"U"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LSQUARE = r"\["
t_RSQUARE = r"\]"
t_T = r"T"  # Regular expression for token "T"
t_N = r"N"
# t_VAR = r"[a-zB-DF-TV-Z_][a-zA-Z0-9_]*"


# define VAR token after reserved keywords.
def t_VAR(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    # check if token matches any keyword :
    reserved = {
        "AND",
        "OR",
        "NOT",
        "IMP",
        "AG",
        "EG",
        "AX",
        "EX",
        "AF",
        "EF",
        "A",
        "E",
        "U",
        "T",
        "N",
    }
    if t.value in reserved:
        t.type = t.value
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# # testing
# data = input("input formula : ")
#
# # input
# lexer.input(data)
#
# # Tokenise
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # no more input
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)

"""
additional things that are said in the documentation : 
1. Tokens defined by strings are 
    added next 
    by sorting them 
    in order of decreasing regular expression length
    (long expressions are added first. )
    -> DONE :)
2. All tokens 
    defined by functions are 
    added in the same order as they appear in the lexer file. 
    -> DONE :)
"""
