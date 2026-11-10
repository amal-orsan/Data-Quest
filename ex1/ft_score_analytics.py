import sys


def parse_score(arg: str) -> int | None:
    try:
        value = int(arg)
    except ValueError:
        print(f"Invalid parameter: '{arg}'")
        return None

    if value < 0:
        print(f"Invalid parameter: '{arg}'")
        return None

    return value


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    scores: list[int] = []

    for arg in args:
        score = parse_score(arg)
        if score is not None:
            scores = scores + [score]

    if len(scores) == 0:
        print("No scores provided."
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
