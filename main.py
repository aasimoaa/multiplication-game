import random
import time
import os
import subprocess

def print_banner():
    print("=" * 60)
    print(" 🌟 🚀     LEGENDARY MULTIPLICATION CHALLENGE     🚀 🌟 ")
    print("=" * 60)

def play_mp3(filename):
    """Function to play external MP3 files using built-in Windows launcher"""
    if os.path.exists(filename):
        try:
            subprocess.Popen(['start', '', filename], shell=True)
        except Exception as e:
            print(f"Could not play audio: {e}")

# Dictionary for giant, clear ASCII text numbers
LARGE_NUMBERS = {
    '0': [" ███████ ", " ██   ██ ", " ██   ██ ", " ██   ██ ", " ███████ "],
    '1': ["   ███   ", "    ██   ", "    ██   ", "    ██   ", "  ███████"],
    '2': [" ███████ ", "      ██ ", " ███████ ", " ██      ", " ███████ "],
    '3': [" ███████ ", "      ██ ", " ███████ ", "      ██ ", " ███████ "],
    '4': [" ██   ██ ", " ██   ██ ", " ███████ ", "      ██ ", "      ██ "],
    '5': [" ███████ ", " ██      ", " ███████ ", "      ██ ", " ███████ "],
    '6': [" ███████ ", " ██      ", " ███████ ", " ██   ██ ", " ███████ "],
    '7': [" ███████ ", "      ██ ", "     ██  ", "    ██   ", "    ██   "],
    '8': [" ███████ ", " ██   ██ ", " ███████ ", " ██   ██ ", " ███████ "],
    '9': [" ███████ ", " ██   ██ ", " ███████ ", "      ██ ", " ███████ "],
    'x': ["         ", " ██   ██ ", "   ███   ", " ██   ██ ", "         "]
}

def print_giant_text(text):
    """Print numbers in a giant and very clear format"""
    lines = ["", "", "", "", ""]
    for char in str(text):
        if char in LARGE_NUMBERS:
            pattern = LARGE_NUMBERS[char]
            for i in range(5):
                lines[i] += pattern[i] + "  "
        else:
            for i in range(5):
                lines[i] += "         "
    
    print("\n")
    for line in lines:
        print("    " + line)
    print("\n")

def quiz_multiplication():
    print_banner()
    
    score = 0
    total_questions = 5  # Number of questions

    for i in range(1, total_questions + 1):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 * num2
        
        print(f"\n--- [Question {i} of {total_questions}] ---")
        print("   The challenge equation is:")
        
        # Print the math equation in giant text
        question_str = f"{num1}x{num2}"
        print_giant_text(question_str)
        
        try:
            user_answer = int(input("👉 Enter your answer here: "))
            
            if user_answer == correct_answer:
                score += 1
                print("\n" + "✨" * 20)
                print("     🎉 Correct Answer! Great job! ⭐ 🎯")
                print("✨" * 20 + "\n")
                play_mp3('success.mp3')
                
            else:
                print("\n" + "💥" * 20)
                print(f"     ❌ Oops! The correct answer is: {correct_answer} 💡")
                print("💥" * 20 + "\n")
                play_mp3('fail.mp3')
                
        except ValueError:
            print("⚠️ Warning: Please enter a valid whole number!")

    # Final score screen
    print("\n" + "=" * 60)
    print(f" 🏆 Game Over! Your final score is: {score} out of {total_questions} 🏆 ")
    print("=" * 60)
    
    if score == total_questions:
        print("🥇 Amazing! Perfect score! You are a Legendary Math Genius! 👑")
        play_mp3('success.mp3')
    elif score >= total_questions / 2:
        print("👍 Excellent effort! Keep practising and you will get even better! 💪")
        play_mp3('success.mp3')
    else:
        print("💪 Never give up! Practice makes perfect! Try again! 🌟")
        play_mp3('fail.mp3')
    
    time.sleep(2)
    print("=" * 60)

# Run the program
quiz_multiplication()
