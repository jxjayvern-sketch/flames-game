def flames_result(name1: str, name2: str) -> str:
    """Compute the FLAMES relationship between two names.

    Steps:
    1. Strip out non-alphabetic characters and make names lowercase.
    2. Cancel common letters between the two names, one occurrence at a time.
    3. Count the remaining letters. This count is used to eliminate letters
       from the word ``FLAMES``.
    4. Repeatedly cycle through the remaining letters of ``FLAMES`` and
       eliminate the letter at the ``count`` position until only a single
       letter remains.
    5. Translate the final letter to its meaning.
    """
    # prepare lists of characters
    n1 = [c for c in name1.lower() if c.isalpha()]
    n2 = [c for c in name2.lower() if c.isalpha()]

    # remove common characters
    for c in n1[:]:
        if c in n2:
            n1.remove(c)
            n2.remove(c)

    count = len(n1) + len(n2)

    if count == 0:
        return "No relationship (names are identical or contain no letters)"

    flames = list("FLAMES")

    # eliminate letters until one remains
    while len(flames) > 1:
        # the index to remove: count mod len(flames) - 1
        idx = (count % len(flames)) - 1
        if idx >= 0:
            flames.pop(idx)
            # rotate so that counting starts from the next letter
            flames = flames[idx:] + flames[:idx]
        else:
            # when count is a multiple of len(flames), drop the last letter
            flames.pop()
        # continue with updated flames list

    meaning = {
        "F": "Friend",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sister",
    }
    return meaning.get(flames[0], "Unknown")


def main() -> None:
    """Simple command-line interface for playing FLAMES."""
    print("Welcome to FLAMES!")
    try:
        n1 = input("Enter name of first person: ").strip()
        n2 = input("Enter name of second person: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled.")
        return

    result = flames_result(n1, n2)
    print(f"Result for '{n1}' and '{n2}': {result}")


if __name__ == "__main__":
    main()
