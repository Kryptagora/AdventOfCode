def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    caloriesList = input_data.split("\n\n")

    max_calories = 0 
    curr_calories = 0
    for item in caloriesList:
        for number in item.split("\n"):
            curr_calories += int(number)
        if curr_calories > max_calories:
            max_calories = curr_calories

        curr_calories = 0

    return max_calories

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    caloriesList = input_data.split("\n\n")
    # Store all the calories in a list
    totalCalories = []
    curr_calories = 0

    for item in caloriesList:
        for number in item.split("\n"):
            curr_calories += int(number)

        totalCalories.append(curr_calories)
        curr_calories = 0

    # get three largest elements in the list
    totalCalories.sort(reverse=True)
    
    
    return sum(totalCalories[:3])
    


