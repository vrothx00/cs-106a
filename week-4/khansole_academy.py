import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    sum = generate_nums()
    answer = ask_questions()
    check_answer(answer, sum)

def generate_nums():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    print(f"What is {num1} + {num2}?")
    sum = num1 + num2
    return sum

def ask_questions():
    answer = int(input("Your answer: "))
    return answer

def check_answer(answer, sum):
    if answer != sum:
        print("Incorrect.")
        print(f"The expected answer is {sum}")
    else:
        print("Correct!")


if __name__ == '__main__':
    main()
