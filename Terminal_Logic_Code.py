from functions_and_rules.quantifier_rules import universal_instantiation


def answer():
    user_aws = str(input("Would you like to to Enter a constant?: "))
    if (user_aws == "Yes") or (user_aws == "yes"):
        user_constant = str(input("Enter a Constant: "))
        print(universal_instantiation(formula, user_constant))
    else:
        print("Goodbye")


user_variable = str(input("Enter a variable from x, y, z: "))
formula = f"∀{user_variable}(S{user_variable} ⇒ P{user_variable})"
print(f'Your formula" {formula}')

answer()
