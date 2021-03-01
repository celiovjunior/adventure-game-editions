answer = input("What do you like to play? (yes / no)")
if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads. Would you like to left or right?").lower().strip()
    if answer == "left":
            answer = input("You encouter a monster! Would you like to run or attack?")

            if answer == "attack":
                print("That was not the greatest idea, you died.")
            else:
                print("Good choice. You made it safely")

                answer = input("you see a car and a plane. Which would you like to take?")
                
                if answer == "plane":
                    print("Yo dont know how to fly. Game over.")
                
                else:
                    print("You take the car and drive fast.")

    elif answer == "right":
        print("You walk to the right and fall to a patch of ice. Your leg is injure and you can't continue.")

    else:
            print("Invalid choice. You lost!")

else:
    print("that's to bad!")