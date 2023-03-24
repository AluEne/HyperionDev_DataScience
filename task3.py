# create a program that awards a triathlon candidate an award based on their qualifying time
qualifying_time = 100
swimming = int(input("Kindly input your swimming qualifying round time: ")) # Atheletes swimming time
running = int(input("Kindly input your runnung qualifying round time: ")) # Athletes running time
cycling = int(input("Kindly input your cycling qualifying round time: ")) # Athletes cycling time
total_time = swimming + running + cycling
print("Your total time across all events is: " + " " + str(total_time))

if total_time >= qualifying_time:
    print("Congratulations! /n You have been awarded with Provincial Colors")
elif total_time >= qualifying_time - 5 and total_time <= qualifying_time - 0.01:
    print("Congratulations! /n You have been awarded with Provincial Half Colors")
elif total_time >= qualifying_time - 10 and total_time <= qualifying_time - 5.01:
    print("Congratulations! /n You have been awarded with Provincial Scroll")
else:
    print("Unfortunately you will be receving no award")