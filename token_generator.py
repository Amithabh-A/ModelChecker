"""
parser and AST generator for CTL formula 
"""

from ply import lex

# from ply import yacc

# List of token names
tokens = (
    "AND",
    "OR",
    "NOT",
    "IMP",
    "AG",
    "EG",
    #    "AU",
    #    "EU",
    "AX",
    "EX",
    "AF",
    "EF",
    "LPAREN",  # simple rule
    "RPAREN",  # simple rule
    "LSQUARE",  # simple rule
    "RSQUARE",  # simple rule
    "A",
    "E",
    "U",
    "VAR",  # simple rule
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
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LSQUARE = r"\["
t_RSQUARE = r"\]"
t_A = r"A"
t_E = r"E"
t_U = r"U"
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

# testing
data = input("input formula : ")

# input
lexer.input(data)

# Tokenise
while True:
    tok = lexer.token()
    if not tok:
        break  # no more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)

# # Grammar rules and precedence
# precedence = (
#     ("left", "OR"),
#     ("left", "AND"),
#     ("right", "NOT"),
#     ("left", "IMP"),
#     ("right", "AG"),
#     ("right", "EG"),
#     ("right", "AF"),
#     ("right", "EF"),
#     ("right", "AX"),
#     ("right", "EX"),
# )
#
# # def p_formula(p):
# #     '''
# #     formula : VAR
# #             | formula OR formula
# #             | formula AND formula
# #             | NOT formula
# #             | formula IMP formula
# #             | AX formula
# #             | EX formula
# #             | AF formula
# #             | EF formula
# #             | AG formula
# #             | EG formula
# #             | A [ formula U formula]
# #             | E [ formula U formula]
# #     '''
# #    # Define actions for each grammar rule
#
# # actions for AND
#
#
# def p_formula_paren(p):
#     """
#     formula : LPAREN formula RPAREN
#     """
#     p[0] = p[2]
#
#
# def p_formula_var(p):
#     """
#     formula : VAR
#     """
#     p[0] = ("VAR", p[1])
#
#
# def p_formula_and(p):
#     """
#     formula : formula AND formula
#     """
#     p[0] = ("AND", p[1], p[3])
#
#
# def p_formula_or(p):
#     """
#     formula : formula OR formula
#     """
#     p[0] = ("OR", p[1], p[3])
#
#
# def p_formula_not(p):
#     """
#     formula : NOT formula
#     """
#     p[0] = ("NOT", p[2])
#
#
# def p_formula_imp(p):
#     """
#     formula : formula IMP formula
#     """
#     p[0] = ("IMP", p[1], p[3])
#
#
# def p_formula_ax(p):
#     """
#     formula : AX formula
#     """
#     p[0] = ("AX", p[2])
#
#
# def p_formula_ex(p):
#     """
#     formula : EX formula
#     """
#     p[0] = ("EX", p[2])
#
#
# def p_formula_ag(p):
#     """
#     formula : AG formula
#     """
#     p[0] = ("AG", p[2])
#
#
# def p_formula_eg(p):
#     """
#     formula : EG formula
#     """
#     p[0] = ("EG", p[2])
#
#
# def p_formula_af(p):
#     """
#     formula : AF formula
#     """
#     p[0] = ("AF", p[2])
#
#
# def p_formula_ef(p):
#     """
#     formula : EF formula
#     """
#     p[0] = ("EF", p[2])
#
#
# def p_formula_au(p):
#     """
#     formula : A LSQUARE formula U formula RSQUARE
#     """
#     p[0] = ("AU", p[3], p[5])
#
#
# def p_formula_eu(p):
#     """
#     formula : E LSQUARE formula U formula RSQUARE
#     """
#     p[0] = ("EU", p[3], p[5])
#
#
# # Build the parser
# parser = yacc.yacc()
#
#
# def parse_input(s):
#     lexer.input(s)
#     ast = parser.parse(s)
#     return ast
#
#
# input_string = "NOT (p AND q)"
# ast = parse_input(input_string)
# print(ast)
