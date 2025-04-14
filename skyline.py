# Add your clarifying questions here

def skyline(building_list):
    buildings = []
    max_height = 0

    for height in building_list:
        if height > max_height:
            buildings.append(height)
            max_height = height
    return buildings

print(skyline([1, 3, 7, 7, 3]))
print(skyline([-1, 3, 8, 7, 3]))
print(skyline([]))