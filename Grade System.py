while True:
 marks=int(input('Enter your marks = '))
 if marks>=90 and marks<=100:
    print("your grade is 'A'.")
 elif marks<90 and marks>=80:
    print("your grade is 'B'.")
 elif marks<80 and marks>=70:
    print("your grade is 'C'.")
 elif marks<70 and marks>=60:
    print("your grade is 'D'.")
 else:
    print("your grade is 'F'.")

 print('Thank you')