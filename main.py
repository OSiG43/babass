# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def hello():
    print("hello world")


def demandeage():
    age = int(input("Quel age as-tu ?"))
    if age < 18:
        print("Tu es mineur")
    else:
        print("Tu es majeur")

hello()
demandeage()