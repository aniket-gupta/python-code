import media
import fresh_tomatoes


toy_story = media.Movie('Toy Story',
                        'A story of boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13' +
                        '/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
# print toy_story.storyline

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/' +
                     'Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=cRdxXPV9GNQ')
# print avatar.storyline
# avatar.show_trailor()

bajragi_bhaijan = media.Movie('Bajrangi Bhaijaan',
                              'A man with a magnanimous spirit helps a mute ' +
                              'girl from Pakistan return home.',
                              'https://upload.wikimedia.org/wikipedia/en/d' +
                              '/dd//Bajrangi_Bhaijaan_Poster.jpg',
                              'https://www.youtube.com/watch?v=4nwAra0mz_Q')
# bajragi_bhaijan.show_trailor()

school_of_rock = media.Movie('School of rock',
                             'Rock music lessons and summer music camps for' +
                             'student musicians ages 7-18+ of all skill ' +
                             'levels.',
                             'https://upload.wikimedia.org/wikipedia/' +
                             'en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

andaz_apna_apna = media.Movie('Andaz Apna Apna',
                              "Two men (Aamir Khan, Salman Khan) try to " +
                              "improve their lot in life by wooing " +
                              "a millionaire's daughter (Raveena Tandon).",
                              "https://upload.wikimedia.org/wikipedia/" +
                              "en/1/15/Andaz_Apna_Apna.jpg",
                              'https://www.youtube.com/watch?v=MUc3Z5dYBOU')

hera_pheri = media.Movie('Hera Pheri',
                         'Three people in dire need of money become ' +
                         "involved in a gangster's plot to kidnap a " +
                         "wealthy man's grandson.",
                         'https://upload.wikimedia.org/wikipedia/en/' +
                         '5/51/Hera_Pheri_(poster).jpg',
                         'https://www.youtube.com/watch?v=PyfIDCJ5SsI')

movies = [toy_story, avatar, bajragi_bhaijan,
          school_of_rock, andaz_apna_apna, hera_pheri]

fresh_tomatoes.open_movies_page(movies)
