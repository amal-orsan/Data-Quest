import random


def gen_player_achievements(pool: list[str]) -> set[str]:
    count = random.randint(5, 8)
    return set(random.sample(pool, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    achievement_pool = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Strategist", "Speed Runner", "Survivor", "Treasure Hunter",
        "First Steps", "Sharp Mind", "Unstoppable", "Hidden Path Finder"
    ]

    player_names = ["Alice", "Bob", "Charlie", "Dylan"]
    player_sets: list[set[str]] = []

    for name in player_names:
        achievements = gen_player_achievements(achievement_pool)
        player_sets = player_sets + [achievements]
        print(f"Player {name}: {achievements}")

    all_distinct: set[str] = set()
    for achievements in player_sets:
        all_distinct = all_distinct.union(achievements)
    print(f"All distinct achievements: {all_distinct}")

    common_achievements = set(achievement_pool)
    for achievements in player_sets:
        common_achievements = common_achievements.intersection(achievements)
    print(f"Common achievements: {common_achievements}")

    for i in range(len(player_names)):
        others_combined: set[str] = set()
        for j in range(len(player_names)):
            if j != i:
                others_combined = others_combined.union(player_sets[j])
        unique = player_sets[i].difference(others_combined)
        print(f"Only {player_names[i]} has: {unique}")

    pool_set = set(achievement_pool)
    for i in range(len(player_names)):
        missing = pool_set.difference(player_sets[i])
        print(f"{player_names[i]} is missing: {missing}")


if __name__ == "__main__":
    main()
