"""
Logical_Symbols
==============

This module defines a dictionary of logical operator symbols. The dictionary
contains entries for different logical operators, such as negation, conjunction,
and material conditional, and provides a list of symbols that can be used to
represent each operator.

The dictionary can be used as a reference for logical operator symbols, and
can be easily updated and extended to add more operators or symbols.
"""

# A dictionary that maps logical operators to their corresponding symbols in various notation systems
Logical_Symbols = dict(
    # Negation: represents the logical operation of negation, which is the reversal of the truth value of a proposition
    Negation=["¬", "~", "!", "not"],
    # Conjunction: represents the logical operation of conjunction, which is the combination of two propositions in such a way that the resulting proposition is only true if both of the original propositions are true
    Conjunction=["∧", "&", "·", "and"],
    # Inclusive disjunction: represents the logical operation of inclusive disjunction, which is the combination of two propositions in such a way that the resulting proposition is true if either of the original propositions are true (or if both are true)
    Inclusive_Disjunction=["∨", "or"],
    # Material conditional: represents the logical operation of material conditional, which is a type of conditional statement in logic that is only considered true if the antecedent is false or the consequent is true
    Material_Conditional=["→", "⇒", "⊃", "if, then"],
    # Material biconditional: represents the logical operation of material biconditional, which is a type of conditional statement in logic that is only considered true if the antecedent and consequent are both true or both false
    Material_Bi_Conditional=["↔", "⇔", "≡"],
    # Universal quantifier: represents the universal quantifier, which is a logical symbol used to indicate that a statement holds for all possible values of a variable
    Universal_Quantifier="∀",
    # Existential quantifier: represents the existential quantifier, which is a logical symbol used to indicate that a statement holds for at least one possible value of a variable
    Existential_Quantifier="∃",
    # Falsum: represents the logical constant falsum, which is the symbol used to denote a false proposition in logic
    Falsum="⊥",
    # Verum: represents the logical constant verum, which is the symbol used to denote a true proposition in logic
    Verum="⊤",
    # Identical to: represents the symbol used to denote identity in logic
    Identical_to="=",
    # Variables: represents a list of common variables used in logical statements
    Variables=["x", "y", "z"],
)


# Add more entries to the dictionary using the update() method
Logical_Symbols.update(
    Exclusive_Disjunction=["⊕", "xor", "⊻"],
    Implication=["⊢", "→"],
    Equivalence=["≡", "::"],
)

# Lexicon for all non-logical symbols
Non_Logical_Symbols = {
    "Subscript": ["₀", "₁", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    "Predicate": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Constants": "abcdefghijklmopqrstuvw",
    "Function Symbol": "𝑓",
    "Punctuation marks": "(,) ,",
}

# Lambda expressions for logical connectives
connectives = {
    'not': lambda x: not x,
    'and': lambda x, y: x and y,
    'or': lambda x, y: x or y,
    'xor': lambda x, y: x != y,
    'implies': lambda x, y: not x or y,
    'iff': lambda x, y: x == y
}

# the principal of bivalnce is a semantic princiapl that states only two truth states are present (within a given logical system)
Bivalence = {"True": "T", "False": "F"}


def valuation(Forumla):  # The Defintion of the valuation Function

    if Forumla == Bivalence["True"]:
        Formula = True
    else:
        Formula = False

    return Formula


def negation(Proposition):

    if valuation(Proposition):
        Proposition = Bivalence["False"]
    else:
        Proposition = Bivalence["True"]

    return Proposition


def conjunction(Left_Hand_Proposition, Right_Hand_Proposition):

    if valuation(Left_Hand_Proposition) and valuation(Right_Hand_Proposition):
        Formula = Bivalence["True"]

    elif valuation(Left_Hand_Proposition) or valuation(Right_Hand_Proposition):
        Formula = Bivalence["False"]
    else:
        Formula = Bivalence["False"]

    return Formula


def disjunction(Left_hand_disjunct, Right_Hand_Disjunct):

    if valuation(Left_hand_disjunct) or valuation(Right_Hand_Disjunct):
        Formula = Bivalence["True"]

    elif valuation(Left_hand_disjunct) and valuation(Right_Hand_Disjunct):
        Formula = Bivalence["False"]
    else:
        Formula = Bivalence["False"]

    return Formula


def m_condtional(Left_Proposition, Right_Proposition):

    if valuation(negation(Left_Proposition)) or valuation(Right_Proposition):
        Formula = Bivalence["True"]
    else:
        Formula = Bivalence["False"]

    return Formula


def m_biconditional(Left_implication, right_implication):

    if (valuation(negation(Left_implication)) or valuation(right_implication)) and (
        valuation(negation(right_implication)) or valuation(Left_implication)
    ):
        Formula = Bivalence["True"]
    else:
        Formula = Bivalence["False"]

    return Formula


def truth_table(operator, values): # FIXME: Set the atomic propositions to the side, and the logical expression as the header
    """
    Generate a truth table for a given logical operator applied to a list of boolean values.

    Parameters:
    - operator: a function that takes two boolean values as input and returns a boolean value.
    - values: a list of boolean values.

    Returns:
    - A list of tuples, each containing two input values and the result of applying the operator to those values.
    """
    # Create a list to hold the truth table tuples
    truth_table = []

    # Iterate over the input values
    for value1 in values:
        for value2 in values:
            # Apply the operator to the values and add the result to the truth table
            truth_table.append((value1, value2, operator(value1, value2)))

    col_widths = [max(len(str(value)) for value in col) for col in zip(*truth_table)]

    # Print a header row
    print("  ".join(str(i).ljust(col_widths[i]) for i in range(len(col_widths))))
    print("-" * sum(col_widths))

    # Print the data rows
    for row in truth_table:
        print("  ".join(str(value).ljust(col_widths[i]) for i, value in enumerate(row)))


def Logical_operators():
    print(
        f'If P is false, then {Logical_Symbols["Negation"][0]}P shall return true: {negation("F")}'
    )  # negation should return true if false, and false if true
    print(
        f'If P is true, then {Logical_Symbols["Negation"][0]}P shall return false: {negation("T")}\n'
    )

    print(
        f'If P is true, and Q true; then P {Logical_Symbols["Conjunction"][0]} Q shall return true: {conjunction("T", "T")}'
    )  # the conjunction should return true if and only if both operands are true, and false otherwise
    print(
        f'If P is true, and Q is false; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("T", "F")}'
    )
    print(
        f'If P is false, and Q is true; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("F", "T")}'
    )
    print(
        f'If P is false, and Q is false; then P {Logical_Symbols["Conjunction"][0]} Q shall return flase: {conjunction("F", "F")}\n'
    )

    print(
        f'If P is true, and Q true; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("T", "T")}'
    )  # the inclusive disjunction should return false if and only if both operands are false, and true otherwise
    print(
        f'If P is true, and Q is false; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("T", "F")}'
    )
    print(
        f'If P is false, and Q is true; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return true: {disjunction("F", "T")}'
    )
    print(
        f'If P is false, and Q is false; then P {Logical_Symbols["Inclusive Disjunction"][0]} Q shall return false: {disjunction("F", "F")}\n'
    )

    print(
        f'If P is true, and Q true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("T", "T")}'
    )  # the material conditional should return false if and only if the right operand is false while leaving the left operand true; otherwise true
    print(
        f'If P is true, and Q is false; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("T", "F")}'
    )
    print(
        f'If P is false, and Q is true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return false: {m_condtional("F", "T")}'
    )
    print(
        f'If P is false, and Q is false; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_condtional("F", "F")}\n'
    )

    print(
        f'If P is true, and Q true; then P {Logical_Symbols["Material Conditional"][0]} Q shall return true: {m_biconditional("T", "T")}'
    )  # the material bi-conditional should return true if and only if both operands have the same truth value, and otherwise false
    print(
        f'If P is true, and Q is false; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return false: {m_biconditional("T", "F")}'
    )
    print(
        f'If P is false, and Q is true; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return false: {m_biconditional("F", "T")}'
    )
    print(
        f'If P is false, and Q is false; then P {Logical_Symbols["Material Bi-Conditional"][0]} Q shall return true: {m_biconditional("F", "F")}\n'
    )


def enumeration_of_logical_symbols():
    # Use the enumerate() function to iterate over the dictionary
    for i, (key, value) in enumerate(Logical_Symbols.items()):
        # Print the entry in a formatted and readable way
        print(f"{i+1}. {key}: {value}")


# Test the truth table function
truth_table(connectives["and"], [True, False])
# Output: 
# 0      1      2    
# ---------------
# True   True   True
# True   False  False
# False  True   False
# False  False  False
