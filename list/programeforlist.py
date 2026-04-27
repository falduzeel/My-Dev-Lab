def main():
    total_cnt = int(input("enter total numbers: "))
    student_list = []
    
    for i in range (total_cnt):
        item = input("Enter list item :")
        student_list.append(item)

    print(f"final all student list :")
    for student in student_list :
        print (f" {student}",end= " ")

if __name__ == "__main__":
    main()