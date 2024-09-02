import random


def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "The journey of a thousand miles begins with one step. – Lao Tzu",
        "Life is what happens when you’re busy making other plans. – John Lennon",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
        "In the end, we will remember not the words of our enemies, but the silence of our friends. – Martin Luther King Jr.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
        "It is our choices that show what we truly are, far more than our abilities. – J.K. Rowling",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
        "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
        "The best way to predict the future is to invent it. – Alan Kay",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky",
        "I have not failed. I've just found 10,000 ways that won't work. – Thomas Edison",
        "Do not wait to strike till the iron is hot; but make it hot by striking. – William Butler Yeats",
        "Whether you think you can or you think you can’t, you’re right. – Henry Ford",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson",
        "If you look at what you have in life, you'll always have more. If you look at what you don’t have in life, you'll never have enough. – Oprah Winfrey"
    ]

    return random.choice(quotes)


def main():
    print("Here's your today's quote:")
    print(get_random_quote())


if __name__ == "__main__":
    main()
