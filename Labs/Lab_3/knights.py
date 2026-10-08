from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


def says(knight, knave, statement):
    return And(Implication(knight, statement),
               Implication(knave, Not(statement)))


def kind(knight, knave):
    return And(Or(knight, knave), Not(And(knight, knave)))


knowledge0 = And(
    kind(AKnight, AKnave),
    says(AKnight, AKnave, And(AKnight, AKnave))
)

knowledge1 = And(
    kind(AKnight, AKnave), kind(BKnight, BKnave),
    says(AKnight, AKnave, And(AKnave, BKnave))
)

same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
different = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    kind(AKnight, AKnave), kind(BKnight, BKnave),
    says(AKnight, AKnave, same),
    says(BKnight, BKnave, different)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
    ]

    for name, knowledge in puzzles:
        print(name)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"    {symbol}")


if __name__ == "__main__":
    main()