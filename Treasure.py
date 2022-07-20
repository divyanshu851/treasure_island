

print("Welcome to Tresure Island ")

ans = input("You are mid of the road where do you want to go? left or right :")

if ans == 'left':
    ans = input("Now you have come to lake. type wait for waiting for boat else type swim to swim through lake :")
    if ans == 'wait':
        ans = input("Now you have come to three doors red, green, and yellow type the color to go through :")
        if ans == "red":
            print("You Win")
        elif ans == "green":
            print("This room is full of snake and they all atteck you. Game Over")
        elif ans == "yellow":
            print("This is the room filled with fire. Game Over")
        else:
            print("Sorry game over")
    else:
        print("You didn't reach the other bank of the lake and drown. Game over")
else:
    print("There is snake present there who byte you. Game Over")