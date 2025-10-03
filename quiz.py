import random

flashcards = {
    "Capital of India?": "Delhi",
    "2+2?": "4",
    "Python keyword for function?": "def"
}

def quiz():
    score = 0
    questions = list(flashcards.keys())
    random.shuffle(questions)

    for q in questions:
        ans = input(q + " ")
        if ans.lower() == flashcards[q].lower():
            print(" Correct")
            score += 1
        else:
            print(" Wrong | Answer:", flashcards[q])
    print("\nFinal Score:", score, "/", len(questions))

quiz()
