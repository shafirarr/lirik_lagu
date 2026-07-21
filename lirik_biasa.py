import sys
import time

def lirik():

    lirik = [
        ("The look of love, the rush of blood", 0.065),
        ("The She's with me is the Gallic shrug", 0.060),
        ("The shutterbugs, the Camera Plus", 0.055),
        ("The black and white and the color dodge", 0.060),
        ("The good time girls, the cubicles", 0.065),
        ("The house of fun, the number one", 0.070),
        ("Party anthem", 0.080)
    ]

    delay = [
        1.3,
        1.8,
        1.9,
        1.9,
        1.8,
        2.8,
        3.0
    ]

    print("\nNo. 1 Party Anthem - Arctic Monkeys\n")
    time.sleep(2)

    for i, (line, delay_karakter) in enumerate(lirik):
        for karakter in line:
            print(karakter, end="")
            sys.stdout.flush()
            time.sleep(delay_karakter)

        print()
        time.sleep(delay[i])

    print("\nCode by: Shafira_028")

lirik()