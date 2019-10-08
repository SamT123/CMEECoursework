birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 


latin_names_lc = [bird_info[0] for bird_info in birds]
common_names_lc = [bird_info[1] for bird_info in birds]
weights_lc = [bird_info[2] for bird_info in birds]

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

latin_names_loop = []

for bird_info in birds:
    latin_names_loop.append(bird_info[0])


common_names_loop = []

for bird_info in birds:
    common_names_loop.append(bird_info[1])

weights_loop = []

for bird_info in birds:
    weights_loop.append(bird_info[2])
