print("Smart School Day Planner")
print("Answer 3 quick questions and I will plan your day!\n")

day       =input("What day is it? (Monday-Sunday):").strip().capitalize()
weather  = input("What is the weather? (sunny/rainy/cloudy):").strip().lower()
homework = input("Is your homework done? (yes/no):").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

if day in ("Saturdy", "Sunday"):
    print("Day type    : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type    : First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type    : Last school day. Return library books today.")
elif day in  ("Tuesday", "Wednesday", "Thursday"):
    print("Day type    :  Regular. Stay foucsed! ")
else: 
    print("Day not recognised")

if weather == "sunny" and "homework" == "yes":
    print("Haed to the park")

if weather == "rainy" or weather == "cloudy": 
    print("Pack an umbrella")

if not (homework == "yes"):
    print("Homework    : Not done yet.")

if weather == "rainy" and not (homework == "yes"):
    print("Finish homework and wtach a show")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday", "Sunday")):
    print("All set!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Perfect weather")
else:
    print("One step at a time")

print("Plan complete!")