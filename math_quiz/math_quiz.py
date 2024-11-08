import random


def generate_number(min, max):
    """ Randomly generates an integer for the operation.

    Args:
        min (int): The minimum integer.
        max (int): The maximum integer.

    Returns:
        int: A random integer between min and max.
    """
    return random.randint(min, max)


def generate_operator():
    """ Randomly selects an operator from +, -, or *.

        Returns:
            str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def problem_answer(num1, num2, operator):
    """Generates a problem and calculates its answer.

    Args:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The operator to apply ('+', '-', or '*').

    Returns:
        tuple: A tuple containing:
            - str: The problem.
            - int: The calculated correct answer.            
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """The math quiz, user need to answer questions and earn scores.

    This function generates a series of random math problems.
    The user needs to enter his/her calculated result.
    Each correct answer increments the user's score. The final score will be printed at the end.

    Raises:
        ValueError: If the user enters a non-integer when entering their answer.
    """
    score = 0
    total_questions_num = 3 # Define the total number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions_num):
        num1 = generate_number(1, 10); 
        num2 = generate_number(1, 6); 
        operator = generate_operator()
        problem, currect_answer = problem_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        # Error Handling
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break # Exit the loop if input is valid
            except ValueError:
                print("Invalid input! Please enter an integer.")

        # Check if the user's answer is correct
        if user_answer == currect_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {currect_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions_num}")

if __name__ == "__main__":
    math_quiz()
