def main ():
    sentence_list = []
    for i in range (5):
        sentence = input ("Enter sentence : ")
        sentence_list.append(sentence)

    for sentence in sentence_list:
        print(f"{sentence}, total_char : {len(sentence)}")


if __name__ == "__main__" :
    main()