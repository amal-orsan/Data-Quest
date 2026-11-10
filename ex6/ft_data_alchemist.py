import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players = ["Alice", "bob", "Charlie", "dylan",
                       "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {initial_players}")

    all_capitalized = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_orig_cap = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_orig_cap}")

    scores_dict = {name: random.randint(50, 950) for name in all_capitalized}
    print(f"Score dict: {scores_dict}")

    all_scores: list[int] = []
    for name in all_capitalized:
        all_scores = all_scores + [scores_dict[name]]

    avg_score = sum(all_scores) / len(all_scores)
    print(f"Score average is {round(avg_score, 2)}")

    high_scores = {name: scores_dict[name] for name in all_capitalized
                   if scores_dict[name] > avg_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
