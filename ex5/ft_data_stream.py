import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move",
           "climb", "swim", "release", "use"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        p = random.choice(PLAYERS)
        a = random.choice(ACTIONS)
        yield (p, a)


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        item = random.choice(event_list)
        event_list.remove(item)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        player, action = next(stream)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for consumed in consume_event(ten_events):
        print(f"Got event from list: {consumed}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
