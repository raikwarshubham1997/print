# user input
# Enter 'a' to adding a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to exit:
#starting point

# Adding movies
# Show movies
# find movies
# stopping running program!.....

# Ending point

movies = []

##'''{
##    'name': str()
##    'director': str()
##    'year': int()
##    }'''
## take user inputs
def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie, and 'q' to exit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input == 'f':
            find_by = input("What property of the movie is that? ") #one is year,name,director
            looking_for =input("What are you looking for?: ")
            movie =find_movie(looking_for, lambda x: x[find_by])

            print(movie or 'No movies found.')
        else:
             print("Unknown Commond-please try again")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie,and q to exit: ")

def add_movie():
     name = input("Enter the movie name: ")
     director = input("Enter the movie director: ")
     year = input("Enter the release year: ")

     movies.append({
        'name':name,
        'director': director,
        'year' : year
    })


def show_movie():
    for movie in movies:
        show_movie_details(movie)
def show_movie_details(movie):
        print(f"Name: {movie['name']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")     

def find_movie(expected,finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
        return found

menu()

