from collections import deque, Counter

def plutonian_pebbles(file_text, times):
    initial_queue = get_initial_queue(file_text)
    return enact_rules_on_queue_size_with_counts(initial_queue, times)

def get_initial_queue(file_text):
    numbers = map(int, file_text.split())
    return deque(numbers)

def enact_rules_on_queue_size_with_counts(initial_queue, iterations):
    current_counts = Counter(initial_queue)
    print(current_counts)
    memo = {} 

    for i in range(iterations):
        next_counts = Counter()

        for stone, count in current_counts.items():
            if stone in memo:
                contributions = memo[stone]
            else:
                if stone == 0:
                    contributions = [1]
                else:
                    stone_length = len(str(stone))
                    if stone_length & 1: #odd
                        contributions = [stone * 2024]
                    else:  #even
                        mid = stone_length // 2
                        stone_str = str(stone)
                        contributions = [int(stone_str[:mid]), int(stone_str[mid:])]

                memo[stone] = contributions
            for result in contributions:
                next_counts[result] += count
        current_counts = next_counts
        print(f"Iteration {i} complete: Queue size = {sum(current_counts.values())}")
    return sum(current_counts.values())