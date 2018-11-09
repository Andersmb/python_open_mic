#!/usr/bin/env python3
import pandas

obs = {
    'forest': ['cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['cow', 'horse', 'horse', 'sheep', 'horse'],
    'jungle': ['cow', 'ocelot', 'parrot', 'sheep', 'parrot'],
}

# make new dict for number of unique observations in each biome
unique_obs = {biome:len(set(animal)) for (biome,animal) in obs.items()}
print(f"Number of unique species in biomes: {unique_obs}")

# Count total number of sheep observations
total_sheep_obs = 0
for biome,animal in obs.items():
	total_sheep_obs += animal.count("sheep")

# make a list that contains all unique animal observations across biomes
all_unique_obs = []
all_obs = []
for el in obs.values():
	for animal in el:
		all_obs.append(animal)
		if animal not in all_unique_obs:
			all_unique_obs.append(animal)

# check if some animal was observed in all biomes and count observations of animals
in_all = []
t = []
counts = []
for key in obs.keys():
	for animal in all_unique_obs:

		# count all and unique observations
		counts.append((all_obs.count(animal), animal))
		
		if animal not in obs[key]:
			continue
		else:
			t.append((animal))
for animal in all_unique_obs:
	if t.count(animal) == len(obs):
		in_all.append(animal)

print(f"Animal(s) observed in all biomes: {', '.join(in_all)}")

# get rid of duplicates
counts = sorted(set(counts))

# determine the most frequently observed animal
most_freq_animal = max(counts)[1]
print(f"The most frequently observed animal was {most_freq_animal} ({max(counts)[0]} observations)")
sheep_count = [animal[0] for animal in counts if "sheep" in animal][0]

# count sheep specifically
print(f"Sheep were observed in total {sheep_count} times.")

# evaluate whether parrot only present in jungle
parrot_test = []
for biome in obs.keys():
	if "parrot" in obs[biome]:
		parrot_test.append(True)
	else:
		parrot_test.append(False)

if parrot_test == [False, False, True]:
	print("Parrot(s) were only observed in the jungle.")
else:
	print("Parrot(s) were not only observed in the jungle.")

