#### Fonction secondaire
"""d"""
def ispalindrome(p):
    """f"""
    p.translate(p.maketrans(',', ' '))
    if p != p[::-1]:
        return False
    print('p est pytest .python un palindrome')

    # votre code ici

#### Fonction principale


def main():
    """s"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
