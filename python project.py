import time
import random

# List of sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick waltzing zebras jump",
    "Bright vixens jump; dozy fowl quack",
    "The five boxing wizards jump quickly"
]

def calculate_wpm(input_sentence, elapsed_time):
    num_chars = len(input_sentence)
    wpm = (num_chars / 5) / (elapsed_time / 60)
    return wpm

def typing_test():
    print("Welcome to the WPM typing test!")
    print("Type the following sentence: ")

    # Choose a random sentence
    sentence = random.choice(sentences)
    print(sentence)

    # Start the timer
    start_time = time.time()

    # Get the user's input
    user_input = input()

    # Stop the timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate the WPM
    if user_input == sentence:
        wpm = calculate_wpm(sentence, elapsed_time)
        print(f"Your WPM is: {wpm:.2f}")
    else:
        print("Error: Sentence does not match.")

if __name__ == "__main__":
    typing_test()
