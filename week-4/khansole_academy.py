import random

MIN_RANDOM = 10
MAX_RANDOM = 99
COUNTER = 3

def main():
    print("Khansole Academy")
    # TODO: your code here
    row = 0
    while row < COUNTER:
        sum = generate_nums()
        answer = ask_questions()
        counter_row = sum == answer
        if counter_row:
            row += 1
        else:
            row = 0
        check_answer(answer, sum, row)
    print("Congratulations! You mastered addition.")

def generate_nums():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print(f"What is {num1} + {num2}?")
    sum = num1 + num2
    return sum

def ask_questions():
    answer = int(input("Your answer: "))
    return answer

def check_answer(answer, sum, row):
    if answer != sum:
        print("Incorrect.")
        print(f"The expected answer is {sum}")
    else:
        print("Correct!")
        print(f"You've gotten {row} correct in a row.")


if __name__ == '__main__':
    main()
