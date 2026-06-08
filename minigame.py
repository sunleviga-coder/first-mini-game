import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("🎮 Willkommen beim Zahlenraten-Spiel!")
    print("Ich denke an eine Zahl zwischen 1 und 100. Kannst du sie erraten?")

    while True:
        try:
            guess = int(input("🔢 Dein Tipp: "))
            attempts += 1
            
            if guess < secret_number:
                print("📈 Zu niedrig! Versuch eine hoehere Zahl.")
            elif guess > secret_number:
                print("📉 Zu hoch! Versuch eine niedrigere Zahl.")
            else:
                print(f"🎉 Super! Du hast die Zahl in {attempts} Versuchen erraten!")
                break
        except ValueError:
            print("❌ Ungueltige Eingabe. Bitte gib eine Zahl ein.")

if __name__ == "__main__":
    guess_the_number()
  
