def get_age():
    age = input("Enter your age: ")
    age_as_int = int(age)
    if age_as_int < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

    print("Thanks for using the age checker!")

if __name__ == "__main__":
    get_age()