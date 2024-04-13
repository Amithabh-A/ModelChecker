s = "AG"


def test(s):
    if s == "AG":
        return "¬EF"
    if s == "EG":
        return s
    if s == "AF":
        return "¬EG"
    if s == "EF":
        return "E[T∪F]"
    if s == "AU":
        return None
    if s == "EU":
        return s
    if s == "AX":
        return "¬EX¬ϕ"
    if s == "EX":
        return s
