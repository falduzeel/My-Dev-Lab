def main ():
    user_string = input ("enter any text here :")

    vowels = 0
    consonants = 0
    blanks = 0

    for ch in str.lower(user_string):
        if ch in "aeiou":
            vowels += 1
        elif ch in "bcdfghjklmnpqrstvwxyz":
            consonants += 1
        elif ch == ' ':
              blanks += 1

    print(f"Total vowels is in string : {vowels}")       
    print(f"Total consonants is in string : {consonants}")  
    print(f"Total blank is in string : {blanks}")  

if __name__ == "__main__":
    main()