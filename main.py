print(r"""
==================================================
 ____           ____         _______
/    \    /\   /         /\     |     /\    | /
|    |   /__\  \____    /__\    |    /__\   |/
|    |  /    \      \  /    \   |   /    \  |\
\___\/ /      \ ____/ /      \  |  /      \ | \
     \    

==================================================
""")

player_gender = input("Are you a boy or girl?\n: ")
player_name = input("Name? its not Abdulla ryt?\n: ")
player_age = input("Age\n: ")
player_favcolor = input("Favorite color? Let me guess, blue?\n:")

print("You open your eyes and realized you were sleeping, yawned and suddenly remember you had an interview today.")
ch = input("\n\t| a. Lie on bed becauze your tired and decides to apply for the interview again\n\t| b. Jump out of bed and run.")

if ch == 'a':
	print("You were too tired and lazy to get up from bed that you decided not to go to the interview, and unpause your wonderful dream. Thats when you remembered that last week your friend told you about a company whose name is 'Dream' handing out jobs to around 500 people and train them to do the job. You remember that your friend also mentioned there was a last date for applying.")
	ch = input("\n\t| One again\n\t| a. Would you lie on the bed and worry about it later \n\t| b. Jump out of bed and look at the calendar\n\t| c. Call your friend from the bed.")

	if ch == 'a':
		print("Even then you being lazy and tired overruled your worries for getting a job and you stayed there until you heard a knock.....")
	elif ch == 'b':
		print("This thought really triggered you and you jumped out of your bed only to realize that you were not in your house but rather some where so familiar...")
	elif ch == 'c':
		print("You being lazy and tired didn't move an inch from the bed rather you reached over to the bedside table for the phone and dialed....")

elif ch == 'b':
	print("You go worried all of a sudden and it felt like all your exhaust left your body for good. With some motivation and despite the fact that you couldn't unpause and watch the rest of your dream you jumped out of bed and checked the time. The interview already started and its 5 mins past.")

	ch = input("\n\t| Would you \n\n| a.pick up the phone and call the employer and request for a postpone or delay the interview 1 hour\n\t| b. Hurry up, dress up, drive full speed, reach there and face the consequences\n\t| c. Nah, don't even bother worrying about it. You will wait for their call or go there tomorrow. Too sleepy now")

	if ch == 'a':
		print("You pick up your phone and search for the employer and call. It rings for some time and someone picks up from the other side, but before you could speak anything, the call is cut...")

	elif ch == 'b':
		print("As you wanted that job so badly, you dress up as quickly as you can, have a snack and hurry outside but your car is missing...")

	elif ch == 'c':
		print("Well, you actually don't necessarily need this particular job. Moreover, there million other jobs out there, there is no way you wont get one. Anyway if the employers don't see you, probably they'll call you, so you'll just wait. Coincidence? \"I don't think so\", just immediately your phone rings...")