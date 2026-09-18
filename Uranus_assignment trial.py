#AINEMABAZI ADRINE GIFT
#S26B38/003
##B39105
#GROUP ASSIGNMENT INDIVIDUAL TRIAL (URANUS)



try:
    number_of_guests = int((input("How many guests are checking in?")))
except ValueError:
    print("Please enter valid number of guests")
    number_of_guests = 0

#keeping track of our results
successful_checkins = 0 # starts at 0 because evertime a guest checks in we add 1
total_revenue =0 #same with above

for i in range(number_of_guests):
    print(number_of_guests, i + 1)

    name = input("Enter guest name:")

    def calculate_rate(room_type): #what is in brackets is the information(parameter) needed to exeecute the function
        if room_type == "Single":
            return 80000
        elif room_type == "Double":
            return 120000
        elif room_type == "Suite":
            return 250000
        else:
            return 0

    def calculate_total(rate,nights): #same as above
        total = rate*nights  #method used to calculate total

        if nights>= 3: #since the question says 3 or more nights gets 10% dicount
            total =total*0.90  # 0.9 because we are charging 90% of the price(discount)
        return total

    try:
        nights = int(input("Enter number of nights:"))
    except ValueError:
        print("Inavlid number of nights. Checkin rejected.")
        continue

    if nights<=1: #code must reject 0 or -ves
        print("Number of nights must be at least 1. Checkin rejected.")
        continue #this means stop processing and move to next guest

    room_type = input("Enter room type(Single/Double/Suite:)")

    rate = calculate_rate(room_type)

    #Check if room type is valid
    if rate == 0:
        print('Invalid room type. Checkin rejected.')
        continue

    total = calculate_total(rate,nights)

    print("Guest:", name)
    print("Total payment:", total, "UGX")

    successful_checkins = successful_checkins + 1 #since successful checkins began at 0, we add the one
    total_revenue = total_revenue + total #same as above

    print("---FINAL RESULTS---")
    print("Successful checkins:", successful_checkins)
    print("Total revenue:", total_revenue, "UGX")


    