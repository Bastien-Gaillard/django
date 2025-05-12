from reviews.models import Film
from datetime import date

def create_initial_data():
    films_data = [
        {
            'titre': 'The Shawshank Redemption',
            'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
            'genre': 'Drama',
            'date_sortie': date(1994, 9, 22),
            'realisateur': 'Frank Darabont',
            'acteurs': 'Tim Robbins, Morgan Freeman, Bob Gunton'
        },
        {
            'titre': 'The Godfather',
            'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
            'genre': 'Crime, Drama',
            'date_sortie': date(1972, 3, 24),
            'realisateur': 'Francis Ford Coppola',
            'acteurs': 'Marlon Brando, Al Pacino, James Caan'
        },
        {
            'titre': 'The Dark Knight',
            'description': 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.',
            'genre': 'Action, Crime, Drama',
            'date_sortie': date(2008, 7, 18),
            'realisateur': 'Christopher Nolan',
            'acteurs': 'Christian Bale, Heath Ledger, Aaron Eckhart'
        },
        {
            'titre': 'Forrest Gump',
            'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an extraordinary story to tell.',
            'genre': 'Drama, Romance',
            'date_sortie': date(1994, 7, 6),
            'realisateur': 'Robert Zemeckis',
            'acteurs': 'Tom Hanks, Robin Wright, Gary Sinise'
        },
        {
            'titre': 'Inception',
            'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.',
            'genre': 'Action, Adventure, Sci-Fi',
            'date_sortie': date(2010, 7, 16),
            'realisateur': 'Christopher Nolan',
            'acteurs': 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'
        },
        {
            'titre': 'The Matrix',
            'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
            'genre': 'Action, Sci-Fi',
            'date_sortie': date(1999, 3, 31),
            'realisateur': 'Lana Wachowski, Lilly Wachowski',
            'acteurs': 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss'
        },
        {
            'titre': 'Pulp Fiction',
            'description': 'The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
            'genre': 'Crime, Drama',
            'date_sortie': date(1994, 10, 14),
            'realisateur': 'Quentin Tarantino',
            'acteurs': 'John Travolta, Uma Thurman, Samuel L. Jackson'
        },
        {
            'titre': 'The Lord of the Rings: The Return of the King',
            'description': 'Gandalf and Aragorn lead the World of Men against Sauron\'s forces in a final battle for the survival of Middle-earth.',
            'genre': 'Action, Adventure, Drama',
            'date_sortie': date(2003, 12, 17),
            'realisateur': 'Peter Jackson',
            'acteurs': 'Elijah Wood, Viggo Mortensen, Ian McKellen'
        },
        {
            'titre': 'Gladiator',
            'description': 'A former Roman general sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.',
            'genre': 'Action, Adventure, Drama',
            'date_sortie': date(2000, 5, 5),
            'realisateur': 'Ridley Scott',
            'acteurs': 'Russell Crowe, Joaquin Phoenix, Connie Nielsen'
        },
        {
            'titre': 'Titanic',
            'description': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.',
            'genre': 'Drama, Romance',
            'date_sortie': date(1997, 12, 19),
            'realisateur': 'James Cameron',
            'acteurs': 'Leonardo DiCaprio, Kate Winslet, Billy Zane'
        }
    ]

    for film_data in films_data:
        Film.objects.create(**film_data)

    print("Données de films insérées avec succès !")

