from typing import List, Dict
from collections import defaultdict


def favorite_genre(
    user_songs: Dict[str, List[str]], song_genres: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    # Step 1: Create a mapping of song -> genre
    song_to_genre = {}
    for genre, songs in song_genres.items():
        for song in songs:
            song_to_genre[song] = genre

    # Step 2: Process each user's song list
    user_fav_genres = {}
    for user, songs in user_songs.items():
        genre_count = defaultdict(int)
        max_count = 0

        # Count occurrences of each genre
        for song in songs:
            if song in song_to_genre:
                genre = song_to_genre[song]
                genre_count[genre] += 1
                max_count = max(max_count, genre_count[genre])

        # Step 3: Find the genres with the highest count
        favorite_genres = [
            genre for genre, count in genre_count.items() if count == max_count
        ]
        user_fav_genres[user] = favorite_genres

    return user_fav_genres


# Example usage
user_songs = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma": ["song5", "song6", "song7"],
}

song_genres = {
    "Rock": ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno": ["song2", "song4"],
    "Pop": ["song5", "song6"],
    "Jazz": ["song8", "song9"],
}

result = favorite_genre(user_songs, song_genres)
print(result)