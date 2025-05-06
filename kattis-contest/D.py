p = int(input())

p_split = p / 2
shortest = p_split / 2
longest = p_split / 2

max_area = shortest * longest


str_max_area = str(max_area)
list_str_max_area = str_max_area.split(".")

str_shortest = str(shortest)
list_str_shortest = str_shortest.split(".")


if list_str_max_area[1] == "0":
    max_area = int(max_area)
    
if list_str_shortest[1] == "0":
    shortest = int(shortest)

print(f"{max_area} {shortest} {shortest}")