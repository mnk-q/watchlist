from django import forms

gen = [('all','All'),('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Biography', 'Biography'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'),
       ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Sport', 'Sport'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')]
order = [
    ('movie_imdb', 'Top Rated'),
    ('movie_popularity', 'Popular'),
    ('movie_release', 'New Released'),
]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)


class MovieFilterForm(forms.Form):
    orders = forms.ChoiceField(choices=order)
    genre = forms.ChoiceField(choices=gen)
