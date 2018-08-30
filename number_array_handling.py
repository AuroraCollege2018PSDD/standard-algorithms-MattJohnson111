
import time

scores = []

print("\n\tWelcome to my Number Array Handling!\n")

def quitArray():
    print("\n\tThanks for using my number array handling!")
    time.sleep(1)
    quit()

def loadArray():
    global score, scores
    print("\n\tEnter 'menu' to return to the menu!")
    score = None
    score = str(input("\tWhat number would you like to put into the array?: "))
    if score.lower() == "menu":
        print("\n\tYou have been returned back to the menu!")
        main()
    else:
        scores.append(score)
        main()

def printArray():
    global scores
    print("\n\tThe array includes: ", scores)
    print("\n\tThe array contains: ", len(scores), "variables")
    main()

def sortArray():
    global scores
    print("\n\t1 - Lowest to Highest (LTH)")
    print("\t2 - Highest to Lowest (HTL)")
    direction = str(input("\n\tWhich way would you like the array to be aranged:"))
    if direction == "1" or direction.lower() == "lth":
        scores.sort()
        print("\n\tThe array from lowest to highest is: ", scores)
        main()
    elif direction == "2" or direction.lower() == "htl":
        scores.sort(reverse = True)
        print("\n\tThe array from highest to lowest is: ", scores)
        main()
    else:
        print("I am sorry but", direction, "is not an option!")
        sortArray()

def sumArray():
    global scores
    scores = str(scores)
    sums = sum(scores)
    print("\n\tThe total sum of the array is: ", sums)
    main()

def maxminArray():
    global scores
    print("\n\tThe stubs minimum & maximum was called...")
    print("\n\tThe minimum value in the array is: ", min(scores))
    print("\tThe maximum value in the array is: ", max(scores))
    main()

def clearArray():
    global scores
    yes = ""
    yes = str(input("\n\tAre you sure you want to clear the array?:  "))
    if yes.lower() == "yes":
        scores = []
        print("/n/tThe Array has been cleared, the Array is now", scores)
        main()
    else:
        print("\n\tThe Array was not cleared, the Array contains", scores)
        main()
          
def main():
    choice = None
    while choice != "0":
        try:
            print(
            """        
            0 - Quit (quit)
            1 - Load numbers into the array (load)
            2 - Print the array (print)
            3 - Sort the array (sort)
            4 - Sum the array (sum)
            5 - Find the minimum & maximum (max) or (min)
            6 - Clear the array (clear)
            """
            )
            choice = str(input("What would you like to do: "))
            if choice == "0" or choice.lower() == "quit":
                quitArray()
            elif choice == "1" or choice.lower() == "load":
                loadArray()
            elif choice == "2" or choice.lower() == "print":
                printArray()
            elif choice == "3" or choice.lower() == "sort":
                sortArray()
            elif choice == "4" or choice.lower() == "sum":
                sumArray()
            elif choice == "5" or choice.lower() == "max" or choice.lower() == "min":
                maxminArray()
            elif choice == "6" or choice.lower() == "clear":
                clearArray()
        except ValueError:
            print("Sorry, but", choice, "is an invalid choice.")
            main()
            
main()
