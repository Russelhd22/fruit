validfruits = ["apple", "mango", "watermelon", "durian"]

for f in validfruits:
    fruits = input("enter a fruit: ")
    if fruits == "apple":
        print("hello, apple")
    elif fruits == "mango":
        print("hello, mango")
    elif fruits == "watermelon":
        print("hello, watermelon")
    elif fruits == "durian":
        print("hello, durian")
    else:
        print("error")
