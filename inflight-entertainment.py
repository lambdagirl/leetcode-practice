'''
input: flight_length(in minutes) int, movie_lengths(in minutes)list[int]
output: Boollen (movie1 +movie2 == flight_length)

1.movie1 != movie2
2.runtime complicity 

### example 

input: 300 , [100,110,190,200,230]
output: True 300 = 100 + 200


input: 300, [100,110,130,220,230]
output: False

input: 90, [100,110,130,220,230]
output: False

edge case: 
input: 90, [100]/[]
output: False

1.O(n2)
2.sort n(logn) + binary search log(n) => nlogn
3. dic n constant time 
'''

 def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False
