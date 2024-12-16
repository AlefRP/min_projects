from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input("Choose difficulty (1, 2 or 3): "))
    calc: Calculate = Calculate(difficulty)

    print(f"Tell the answer of {calc.show_operation()}")

    answer: int = int(input("Your answer: "))
    if calc.check_result(answer):
        print("Correct!")
        points += 1
    else:
        print("Incorrect!")

    continue_game: str = input("Continue? (y/n): ")

    if continue_game == "y":
        play(points)
    else:
        print("You have finished with", points, "points!")
        print("Goodbye!")


if __name__ == "__main__":
    main()
