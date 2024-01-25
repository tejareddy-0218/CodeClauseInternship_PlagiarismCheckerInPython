from Levenshtein import distance

def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts using Levenshtein distance.
    Returns a value between 0 (completely different) and 1 (identical).
    """
    max_len = max(len(text1), len(text2))
    if max_len == 0:
        return 1.0  # Both texts are empty

    lev_distance = distance(text1, text2)
    similarity = 1.0 - lev_distance / max_len
    return similarity

def check_plagiarism(text1, text2, threshold=0.8):
    """
    Check if two texts are similar (plagiarized) based on a given threshold.
    """
    similarity = calculate_similarity(text1, text2)
    return similarity >= threshold

if __name__ == "__main__":
    # Example usage
    document1 = "This is a sample text for testing plagiarism."
    document2 = "This is a sample text for testing purposes."

    plagiarism_threshold = 0.8
    is_plagiarized = check_plagiarism(document1, document2, plagiarism_threshold)

    if is_plagiarized:
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")
