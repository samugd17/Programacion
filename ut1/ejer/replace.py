song = """You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness"""

song.index("voices")
word_index = song.index("voices")
song_part1 = song[word_index]
keyword = "voices"
word_end_index = word_index + len(keyword)
song_part2 = song[word_index:]

new_song = song_part1 + "sounds" + song_part2
print(new_song)