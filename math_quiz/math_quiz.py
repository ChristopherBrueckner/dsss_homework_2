import random

def generate_rand_int(min_val, max_val):
    """
    Generate a random integer between a specified minimum and maximum value.

    Parameters
    ----------
    min_val : int
        Minimum value for the random integer.
    max_val : int
        Maximum value for the random integer.

    Returns
    -------
    int
        A random integer within the specified range.
    """
    return random.randint(min_val, max_val)


def generate_rand_operator():
    """
    Randomly select an operator from '+', '-', or '*'.

    Returns
    -------
    str
        A random operator as a string.
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(num1, num2, operator):
    """
    Create a math problem and calculate its solution based on the operator.

    Parameters
    ----------
    num1 : int
        The first number for the problem.
    num2 : int
        The second number for the problem.
    operator : str
        The operator to use.

    Returns
    -------
    tuple
        A tuple containing:
        - str : The generated math problem in the format "num1 operator num2"
        - int : The answer to the generated problem
    """
    problem = f"{num1} {operator} {num2}"
    # create math problem based in given operator and caluclate answer
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2

    return problem, answer


def math_quiz():
    """
    Runs a math quiz where the user answers generated math problems.
    The quiz awards points for correct answers and displays the final score.

    Raises
    ------
    ValueError
        If the user's answer cannot be converted to an integer.
    """
    score = 0
    num_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        # Generate two random numbers and a random operator for the math problem
        num1 = generate_rand_int(1, 10)
        num2 = generate_rand_int(1, 5)
        operator = generate_rand_operator()

        # Create math problem and calculate answer
        problem, correct_answer = generate_math_problem(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            # Get the user's answer and convert it to an integer
            user_answer = int(input("Your answer: "))
            
            # Check if the user's answer is correct
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{num_questions}")


if __name__ == "__main__":
    math_quiz()
