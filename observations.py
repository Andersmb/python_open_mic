#!/usr/bin/env python3

obs = {
    'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['horse', 'horse', 'sheep', 'horse'],
    'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
}

# make new dict for number of unique observations in each biome
unique_obs = {biome:len(set(animal)) for (biome,animal) in obs.items()}

# Count total number of sheep observations
total_sheep_obs = 0
for biome,animal in obs.items():
	total_sheep_obs += animal.count("sheep")

# make a list that contains all unique animal observations across biomes
all_unique_obs = []
for el in obs.values():
	for animal in el:
		if animal not in all_unique_obs:
			all_unique_obs.append(animal)

# check if some animal was observed in all biomes
in_all = False
t = []
for key in obs.keys():
	for animal in all_unique_obs:
		if animal not in obs[key]:
			continue
		else:
			t.append((animal))
for animal in all_unique_obs:
	if t.count(animal) == len(obs):
		in_all = (animal, True)






