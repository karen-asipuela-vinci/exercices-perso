

# variables
txt = ""

def read_string():
    #variable globale
    global txt
    print("Write your text: ")
    txt += input()
    print(txt)
    return txt


def main():
    """
    Fonction principale du programme.
    """
    # Code principal ici
    print("Hello, world!")
    # Appelle d'autres fonctions, exécution des calculs principaux, etc.
    read_string()

if __name__ == "__main__":
    main()
