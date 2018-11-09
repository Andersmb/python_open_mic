#!/usr/bin/env python3

import pandas
import sys

def freq(string):
	# how words and characters to show?
	num = int(sys.argv[1])

	# define the most common punctuation marks
	punctuation = ".,:;-_'´`<>!\"#$%&/()=?@*¨^§"

	# get a list of words with punctuations
	words = string.lower().split()

	# get a list of words without any punctuations by split-joining
	for p in punctuation:
		for i,w in enumerate(words):
			if p in w:
				words[i] = ''.join(w.split(p))
	
	# get string of characters only
	chars = ''.join(words)

	word_count = []
	counted_words = []
	char_count = []
	counted_chars = []
	
	# now count all unique words in words
	# and collect them
	for w in set(words):
		word_count.append(words.count(w))
		counted_words.append(w)

	# now count all unique characters in chars
	# and collect them
	for c in set(chars):
		char_count.append(chars.count(c))
		counted_chars.append(c)

	# now look for the 'num' highest counts, and extract all words and characters with those counts
	max_word_count = list(reversed(sorted(word_count)))[0:num]
	max_char_count = list(reversed(sorted(char_count)))[0:num]

	sortedwords = []
	for i in max_word_count:
		for w in set(words):
			if i == words.count(w):
				sortedwords.append(w)
	
	sortedchars = []
	for i in max_char_count:
		for c in set(chars):
			if i == chars.count(c):
				sortedchars.append(c)
		
	data_w = {"Word": sortedwords[:num],
		  "Frequency": max_word_count}

	data_c = {"Character": sortedchars[:num],
		  "Frequency": max_char_count}


	return data_w, data_c


poem = """For E’er and Hair.


    I said to my sweet in the morning,
      “We must start on our journey at ten”--
    She was up in her bedroom adorning,
      She’d been there a goodish time then;
    And she answered me tenderly, “Poppet,”
      As she came to the top of the stair,
    “If you see a cab pass you can stop it,
      For I’ve only to finish my hair.”

    It was ten by the clock of St. Stephen’s
      As I sat and looked glum in the hall,
    And I offered to wager her evens
      She would never be ready at all.
    I counted the half and the quarters--
      At eleven I ventured to swear;
    Then she answered, like one of Eve’s daughters,
      “All right, dear--I _must_ do my hair.”

    I waited till daylight was waning,
      I waited till darkness began,
    Upbraiding myself for complaining
      Like a selfish and bad-tempered man.
    But when midnight rang out from the steeple
      I ventured to whisper a prayer,
    And she answered, “I hate surly people;
      You _must_ let me finish my hair!”

    I paid for the cab and dismissed it,
      I took off my coat and my hat,
    I held her fair hand and I kissed it,
      And I curled myself up on the mat.
    And when I awoke on the morrow,
      I cried, “Oh, where art thou, my fair?”
    And she answered, “Oh, run out and borrow
      A hairpin or two for my hair.”

    The summers have faded to winters,
      The winters have melted to springs;
    My patience is shivered to splinters,
      And still, as she “puts on her things,”
    My sweet, though I’m weary of waiting,
      And groan in my bitter despair,
    Contents herself simply by stating
      “She’s just got to finish her hair.”

    If she’s here when the world’s at its finish,
      And lists to the last crack of doom,
    She will watch our poor planet diminish
      From the window upstairs in her room.
    And when the last trumpet is blowing,
      And the angel says, “Hurry up, there!”
    She will answer, “All right, sir, I’m going,
      But you _must_ let me finish my hair!”
"""

data_word = freq(poem)[0]
data_char = freq(poem)[1]


print(pandas.DataFrame(data_word))
print("")
print(pandas.DataFrame(data_char))









