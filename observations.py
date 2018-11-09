#!/usr/bin/env python3

obs = {
    'forest': ['cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['cow', 'horse', 'horse', 'sheep', 'horse'],
    'jungle': ['cow', 'ocelot', 'parrot', 'sheep', 'parrot'],
}

# make new dict for number of unique observations in each biome
unique_obs = {biome:len(set(animal)) for (biome,animal) in obs.items()}

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
		in_all.append((animal, True))

# get rid of duplicates
counts = sorted(set(counts))

# determine the most frequently observed animal
most_freq_animal = max(counts)[1]




