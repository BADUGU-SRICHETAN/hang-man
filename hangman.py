import random

def display_hangman(attempts):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---------
        ''',  # 0 attempts left
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ---------
        ''',  # 1 attempt left
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ---------
        ''',  # 2 attempts left
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
        ---------
        ''',  # 3 attempts left
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
        ---------
        ''',  # 4 attempts left
        '''
           ------
           |    |
           |    O
           |
           |
           |
        ---------
        ''',  # 5 attempts left
        '''
           ------
           |    |
           |
           |
           |
           |
        ---------
        '''   # 6 attempts left
    ]
    return stages[attempts]

def hangman():
    categories = {
    "Programming": ["python", "javascript", "function", "variable", "developer", "algorithm", "syntax", "compiler", "debugging", "library"],
    "Animals": ["elephant", "giraffe", "kangaroo", "alligator", "dolphin", "penguin", "ostrich", "tiger", "lion", "hippopotamus"],
    "Countries": ["canada", "germany", "australia", "brazil", "india", "japan", "mexico", "france", "italy", "argentina"],
    "Fruits": ["apple", "banana", "orange", "grape", "pineapple", "mango", "strawberry", "blueberry", "cherry", "watermelon"],
    "Vegetables": ["carrot", "broccoli", "spinach", "potato", "tomato", "cucumber", "onion", "lettuce", "pepper", "eggplant"],
    "Colors": ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"],
    "Sports": ["soccer", "basketball", "baseball", "tennis", "cricket", "hockey", "golf", "volleyball", "rugby", "swimming"],
    "Music": ["guitar", "piano", "drums", "violin", "flute", "saxophone", "trumpet", "lyrics", "concert", "melody"],
    "Movies": ["inception", "titanic", "avatar", "gladiator", "interstellar", "joker", "matrix", "rocky", "jaws", "frozen"],
    "Books": ["novel", "fiction", "biography", "thriller", "mystery", "romance", "fantasy", "poetry", "autobiography", "classics"],
    "Technology": ["computer", "internet", "software", "hardware", "robotics", "cybersecurity", "database", "network", "blockchain", "AI"],
    "Games": ["chess", "monopoly", "scrabble", "checkers", "poker", "mahjong", "clue", "jenga", "uno", "dominoes"],
    "Jobs": ["teacher", "engineer", "doctor", "nurse", "architect", "lawyer", "police", "firefighter", "plumber", "artist"],
    "Space": ["planet", "star", "galaxy", "comet", "asteroid", "satellite", "universe", "orbit", "meteor", "nebula"],
    "Transportation": ["car", "train", "plane", "bicycle", "motorcycle", "boat", "ship", "truck", "bus", "subway"],
    "Clothing": ["shirt", "pants", "dress", "skirt", "jacket", "sweater", "hat", "scarf", "shoes", "gloves"],
    "Body Parts": ["head", "arm", "leg", "eye", "nose", "mouth", "ear", "hand", "foot", "fingers"],
    "Buildings": ["house", "castle", "skyscraper", "hospital", "school", "library", "museum", "church", "stadium", "apartment"],
    "Food": ["pizza", "burger", "sushi", "pasta", "sandwich", "salad", "tacos", "steak", "soup", "curry"],
    "Drinks": ["water", "coffee", "tea", "juice", "milk", "soda", "beer", "wine", "smoothie", "lemonade"],
    "Weather": ["rain", "sun", "cloud", "storm", "snow", "hail", "fog", "hurricane", "tornado", "wind"],
    "Flowers": ["rose", "tulip", "sunflower", "daisy", "orchid", "lily", "lavender", "peony", "marigold", "hibiscus"],
    "Tools": ["hammer", "screwdriver", "wrench", "pliers", "drill", "saw", "chisel", "tape", "ladder", "level"],
    "Furniture": ["chair", "table", "sofa", "bed", "desk", "cabinet", "shelf", "dresser", "bench", "stool"],
    "Languages": ["english", "spanish", "french", "german", "chinese", "japanese", "russian", "korean", "italian", "hindi"],
    "Holidays": ["christmas", "easter", "halloween", "thanksgiving", "hanukkah", "valentine", "diwali", "ramadan", "newyear", "independence"],
    "Mythology": ["zeus", "hera", "apollo", "poseidon", "hades", "athena", "thor", "odin", "loki", "venus"],
    "Professions": ["chef", "mechanic", "writer", "actor", "dancer", "pilot", "farmer", "scientist", "photographer", "carpenter"],
    "Household Items": ["lamp", "mirror", "couch", "vacuum", "fridge", "microwave", "oven", "toaster", "fan", "clock"],
    "Nature": ["forest", "river", "mountain", "ocean", "desert", "valley", "beach", "waterfall", "meadow", "island"],
    "Insects": ["butterfly", "ant", "bee", "mosquito", "grasshopper", "beetle", "spider", "moth", "cockroach", "ladybug"],
    "Countries Capitals": ["paris", "london", "tokyo", "berlin", "rome", "ottawa", "moscow", "delhi", "beijing", "madrid"],
    "Brands": ["apple", "google", "nike", "adidas", "coca-cola", "pepsi", "microsoft", "samsung", "toyota", "honda"],
    "Hobbies": ["painting", "drawing", "fishing", "dancing", "cooking", "gardening", "reading", "knitting", "cycling", "photography"],
    "Desserts": ["cake", "brownie", "pudding", "icecream", "cookies", "cupcake", "tart", "pie", "mousse", "donut"],
    "Shapes": ["circle", "square", "triangle", "rectangle", "hexagon", "pentagon", "octagon", "diamond", "oval", "trapezoid"],
    "Gadgets": ["phone", "laptop", "tablet", "camera", "smartwatch", "headphones", "printer", "drone", "speaker", "microscope"],
    "Birds": ["sparrow", "eagle", "parrot", "owl", "penguin", "peacock", "flamingo", "hawk", "dove", "canary"],
    "Planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "moon"],
    "Cars": ["tesla", "ford", "audi", "bmw", "toyota", "nissan", "chevrolet", "jeep", "honda", "volvo"],
    "Movies Genres": ["action", "comedy", "drama", "horror", "thriller", "fantasy", "sci-fi", "romance", "documentary", "animation"]
    }

    print("Choose a category:")
    for i, category in enumerate(categories.keys(), start=1):
        print(f"{i}. {category}")
    category_choice = input("Enter the number of your choice: ")

    if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
        category_name = list(categories.keys())[int(category_choice) - 1]
        word = random.choice(categories[category_name])
        hint = f"Category: {category_name}"
    else:
        print("Invalid choice! Defaulting to 'Programming'.")
        word = random.choice(categories["Programming"])
        hint = "Category: Programming"

    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()
    score = 0

    print("\nWelcome to Hangman!")
    print(hint)
    print(display_hangman(attempts))
    print("Guess the word: ", ' '.join(guessed_word))
    
    while attempts > 0 and '_' in guessed_word:
        guess = input("\nEnter a letter or guess the entire word: ").lower()

        if not guess.isalpha():
            print("Please enter a valid letter or word.")
            continue

        if len(guess) > 1:  # Guessing the entire word
            if guess == word:
                guessed_word = list(word)
                break
            else:
                attempts -= 1
                print(f"Wrong! '{guess}' is not the correct word. Attempts left: {attempts}")
                print(display_hangman(attempts))
                continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong! '{guess}' is not in the word. Attempts left: {attempts}")
            print(display_hangman(attempts))

        print("Current word: ", ' '.join(guessed_word))

    if '_' not in guessed_word:
        score = attempts * 10
        print("\nCongratulations! You guessed the word:", word)
        print(f"Your score: {score}")
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()
