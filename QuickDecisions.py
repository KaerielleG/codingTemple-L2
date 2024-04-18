attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#task2
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilites = "audio system" if attendees > 200 else "bose"
print(facilites)

#task3
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio system" if attendees > 200 else "bose"
print(facilities)

vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")
if vegetarian_choice.lower() == "yes":
    print("We recommend Veggie Delight Caterers.")
else:
    print("We recommend Gourmet Meals Caterers.")
