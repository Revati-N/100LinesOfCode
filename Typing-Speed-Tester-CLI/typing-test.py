import time
import random
import sys

SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
    "coding is the closest thing we have to a superpower",
    "practice makes perfect but nobody is perfect so why practice",
    "python is a versatile language used in web development and data science",
    "open source contributions help developers grow and build their portfolios",
    "artificial intelligence is transforming the way humans interact with machines",
    "the best way to predict the future is to create it yourself",
    "every expert was once a beginner who refused to give up",
    "simplicity is the ultimate sophistication in software design",
    "debugging is twice as hard as writing the code in the first place",
    "the efficiency we have at removing trash has made creating trash more acceptable",
    "the only way to do great work is to love what you do",
]

def colored(text, code): return f"\033[{code}m{text}\033[0m"
def green(t): return colored(t, "92")
def red(t): return colored(t, "91")
def cyan(t): return colored(t, "96")
def bold(t): return colored(t, "1")

def compare(original, typed):
    result, correct = "", 0
    words_o, words_t = original.split(), typed.split()
    for i, word in enumerate(words_o):
        typed_word = words_t[i] if i < len(words_t) else ""
        if typed_word == word:
            result += green(word) + " "
            correct += 1
        else:
            result += red(word) + " "
    return result.strip(), correct, len(words_o)

def run():
    print(bold(cyan("\n⌨  Typing Speed Tester\n")))
    print("Type the sentence below as fast and accurately as you can.")
    print("Press Enter when done. Type 'quit' to exit.\n")

    scores = []
    while True:
        sentence = random.choice(SENTENCES)
        print(bold("─" * 55))
        print(f"\n{cyan(sentence)}\n")
        print(bold("─" * 55))

        try:
            input("Press Enter to start...")
            print("\033[1A\033[K", end="")  # clears the prompt line
            start = time.time()
            typed = input("> ").strip()
            elapsed = time.time() - start
        except (KeyboardInterrupt, EOFError):
            break

        if typed.lower() == "quit":
            break

        if elapsed < 0.5:
            print(red("Too fast — did you actually type that?\n"))
            continue

        wpm = round((len(sentence.split()) / elapsed) * 60)
        result, correct, total = compare(sentence, typed)
        accuracy = round((correct / total) * 100)

        print(f"\n{result}\n")
        print(f"  {bold('WPM')}      : {green(str(wpm))}")
        print(f"  {bold('Accuracy')}: {green(str(accuracy) + '%')} ({correct}/{total} words correct)")
        print(f"  {bold('Time')}     : {elapsed:.2f}s\n")

        scores.append((wpm, accuracy))

        again = input("Try again? (y/n): ").strip().lower()
        print()
        if again != "y":
            break

    if scores:
        avg_wpm = round(sum(s[0] for s in scores) / len(scores))
        avg_acc = round(sum(s[1] for s in scores) / len(scores))
        print(bold(cyan(" Session Summary: ")))
        print(f"  Rounds     : {len(scores)}")
        print(f"  Avg WPM    : {green(str(avg_wpm))}")
        print(f"  Avg Acc    : {green(str(avg_acc) + '%')}")
        best = max(scores, key=lambda s: s[0])
        print(f"  Best WPM   : {green(str(best[0]))} (at {best[1]}% accuracy)")
    print("\nGood session. See ya! \n")

if __name__ == "__main__":
    run()