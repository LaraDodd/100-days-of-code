def get_tot_distance(house_number: int) -> int:
    """Takes in a house_number and returns the sum of the distances between each friend's house numbers

    Args:
        house_number - an integer representing Alice's potential house number.

    Returns:
        sum of the distances
    """

    # for each house number find distance from each friend's house
    distances = [abs(i - house_number) for house_number in house_numbers]

    # find sum of distances for particular house number
    return sum(distances)


house_numbers = [4, 3, 3, 5, 7]

# create empty dictionary. Dictionary better than list here as can pull out house number as well if you wanted to.
tot_distances = {}

# cycle through all possible house numbers. Curtail at max house number to save computation
for i in range(1, max(house_numbers)):
    tot_dist = get_tot_distance(house_number=i)

    # append total distance to dictionary, where key is house number and value is total distance
    tot_distances.update({i: tot_dist})

# # print house number which has minimum total distance
# print(min(tot_distances, key=tot_distances.get))
print(min(tot_distances.values()))
