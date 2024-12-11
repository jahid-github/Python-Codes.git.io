if __name__ == '__main__':
    n = int(input())  # Number of scores (not used explicitly)
    scores = list(map(int, input().split()))  # Read the scores as a list of integers

    # Remove duplicates and find the second-highest score
    unique_scores = list(set(scores))  # Convert to set to remove duplicates, then back to list
    unique_scores.sort(reverse=True)   # Sort in descending order
    runner_up = unique_scores[1]       # The second-highest score is at index 1

    print(runner_up)  # Print the runner-up score
