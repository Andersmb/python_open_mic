#!/usr/bin/env python3

obs = {
    'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['horse', 'horse', 'sheep', 'horse'],
    'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
}

# make new dict for number of unique observations in each biome
unique_obs = {biome:len(set(animal)) for (biome,animal) in obs.items()}

total_sheep_obs = 0
for biome,animal in obs.items():
	total_sheep_obs += animal.count("sheep")

all_unique_obs = []
for el in obs.values():
	for animal in el:
		if animal not in all_unique_obs:
			all_obs.append(animal)


