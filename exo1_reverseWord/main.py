

# variables
txt = ""
char_list = []
txt_reverse = ""

def read_string():
    #variable globale
    global txt
    print("Write your text: ")
    txt += input()
    return txt

def string_to_char():
    global txt, char_list
    char_list = list(txt)
    return char_list

def char_to_reverse_string():
    global char_list, txt_reverse
    char_list.reverse()
    txt_reverse = ''.join(char_list)
    print(txt_reverse)
    return txt_reverse

def main():
    read_string()
    string_to_char()
    char_to_reverse_string()

if __name__ == "__main__":
    main()
