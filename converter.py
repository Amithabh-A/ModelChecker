"""
parser and AST generator (represented by temporal operators {EG, EU, EX}) 
for CTL formula 
"""

import copy

from ply import yacc

from lexer import tokens

# Grammar rules and precedence
precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("right", "NOT"),
    ("left", "IMP"),
    ("right", "AG"),
    ("right", "EG"),
    ("right", "AF"),
    ("right", "EF"),
    ("right", "AX"),
    ("right", "EX"),
    ("right", "A"),
    ("right", "E"),
)


# Define parser rules here...
def p_formula_paren(p):
    """
    formula : LPAREN formula RPAREN
    """
    p[0] = p[2]


def p_formula_var(p):
    """
    formula : VAR
    """
    p[0] = ("VAR", p[1])


def p_formula_t(p):
    """
    formula : T
    """
    p[0] = ("T",)


def p_formula_n(p):
    """
    formula : N
    """
    p[0] = ("NOT", ("T",))


def p_formula_and(p):
    """
    formula : formula AND formula
    """
    p[0] = ("AND", p[1], p[3])


def p_formula_or(p):
    """
    formula : formula OR formula
    """
    p[0] = ("OR", p[1], p[3])


def p_formula_not(p):
    """
    formula : NOT formula
    """
    p[0] = ("NOT", p[2])


def p_formula_imp(p):
    """
    formula : formula IMP formula
    """
    p[0] = ("IMP", p[1], p[3])


def p_formula_ax(p):
    """
    formula : AX formula
    """
    # p[0] = ("AX", p[2])
    # AX ϕ = ¬ (EX ¬ϕ)
    p[0] = ("NOT", ("EX", ("NOT", p[2])))


def p_formula_ex(p):
    """
    formula : EX formula
    """
    p[0] = ("EX", p[2])


def p_formula_ef(p):
    """
    formula : EF formula
    """
    # p[0] = ("EF", p[2])
    # EF ϕ  = E [T U ϕ]
    p[0] = ("EU", ("T",), p[2])


def p_formula_ag(p):
    """
    formula : AG formula
    """
    # p[0] = ("ag", p[2])
    # ag ϕ = ¬(ef ¬ϕ) = ¬(eu (T, ¬ϕ ))
    p[0] = ("NOT", ("EU", ("T",), ("NOT", p[2])))


def p_formula_eg(p):
    """
    formula : EG formula
    """
    p[0] = ("EG", p[2])


def p_formula_af(p):
    """
    formula : AF formula
    """
    # p[0] = ("AF", p[2])
    # AF ϕ = ¬(EG ¬ϕ)
    p[0] = ("NOT", ("EG", ("NOT", p[2])))


def p_formula_au(p):
    """
    formula : A LSQUARE formula U formula RSQUARE
    """
    # p[0] = ("AU", p[3], p[5])
    p[0] = (
        "NOT",
        (
            "OR",
            (
                "EU",
                ("NOT", p[5]),
                ("AND", ("NOT", p[3]), ("NOT", p[5])),
            ),
            ("EG", ("NOT", p[5])),
        ),
    )


def p_formula_eu(p):
    """
    formula : E LSQUARE formula U formula RSQUARE
    """
    p[0] = ("EU", p[3], p[5])


# Error handling rule
def p_error(p):
    if p:
        print(
            f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'"
        )
    else:
        print("Syntax error: Unexpected end of input")


# Build the parser
parser = yacc.yacc()
