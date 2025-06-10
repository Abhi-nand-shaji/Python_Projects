def clean_poly(poly):
    """Remove zero coefficient terms and combine like terms."""
    cleaned_poly = {}
    for coef, exp in poly:
        if exp in cleaned_poly:
            cleaned_poly[exp] += coef
        else:
            cleaned_poly[exp] = coef
    return [(coef, exp) for exp, coef in cleaned_poly.items() if coef != 0]


def sort_poly(poly):
    """Sort polynomial terms in descending order of exponent."""
    return sorted(poly, key=lambda x: x[1], reverse=True)


def addpoly(p1, p2):
    """Add two polynomials."""
    # Convert polynomials to dictionaries for easier manipulation
    p1_dict = dict(p1)
    p2_dict = dict(p2)

    # Add coefficients of like terms
    for exp, coef in p2_dict.items():
        p1_dict[exp] = p1_dict.get(exp, 0) + coef

    # Convert back to list representation and clean up
    result_poly = clean_poly(p1_dict.items())

    # Sort the result by exponent
    result_poly = sort_poly(result_poly)

    return result_poly


def multpoly(p1, p2):
    """Multiply two polynomials."""
    result_poly = []
    for coef1, exp1 in p1:
        for coef2, exp2 in p2:
            result_poly.append((coef1 * coef2, exp1 + exp2))

    # Clean up and sort the result
    result_poly = clean_poly(result_poly)
    result_poly = sort_poly(result_poly)

    return result_poly


# Test cases

