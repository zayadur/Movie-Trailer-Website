# data.py contains the data, which in this case are my favorite movies.
# This file was modeled after Udacity's "Programming Foundations with Python"
#   Movie Website exercises.

# Created by Zayadur Khan <http://www.zayadur.me">

import media  # module containing Video and Movie classes
import render  # module that generates HTML page

# movie data
deadpool = media.Movie("Deadpool",
                       "2016",
                       "R",
                       "1 hour, 48 minutes",
                       "http://ia.media-imdb.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
                       "A former Special Forces operative turned mercenary " +
                       "is subjected to a rogue experiment that leaves him " +
                       "with accelerated healing powers, adopting the alter " +
                       "ego Deadpool.",
                       "https://youtu.be/ONHBaC-pfsk")

the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street",
                                      "2014",
                                      "R",
                                      "3 hours",
                                      "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                      "Based on the true story of Jordan " +
                                      "Belfort, from his rise to a wealthy " +
                                      "stock-broker living the high life to " +
                                      "his fall involving crime, corruption " +
                                      "and the federal government.",
                                      "https://youtu.be/iszwuX1AK6A")

big_hero_6 = media.Movie("Big Hero 6",
                         "2014",
                         "PG",
                         "1 hour, 42 minutes",
                         "http://ia.media-imdb.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg",
                         "The special bond that develops between plus-sized " +
                         "inflatable robot Baymax, and prodigy Hiro " +
                         "Hamada, who team up with a group of friends to " +
                         "form a band of high-tech heroes.",
                         "https://youtu.be/z3biFxZIJOQ")

spider_man_2 = media.Movie("Spider-Man 2",
                           "2004",
                           "PG-13",
                           "2 hours, 7 minutes",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0Njc1NDYzN15BMl5BanBnXkFtZTcwNjAxMzYyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "Peter Parker is beset with troubles in " +
                           "his failing personal life as he battles a " +
                           "brilliant scientist named Doctor Otto Octavius.",
                           "https://youtu.be/3jBFwltrxJw")

black_hawk_down = media.Movie("Black Hawk Down",
                              "2001",
                              "R",
                              "2 hours, 24 minutes",
                              "http://ia.media-imdb.com/images/M/MV5BMTQxODgzMjYyN15BMl5BanBnXkFtZTgwNDU4NTYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                              "123 elite U.S. soldiers drop into Somalia to " +
                              "capture two top lieutenants of a renegade " +
                              "warlord and find themselves in a desperate " +
                              "battle with a large force of heavily-armed " +
                              "Somalis.",
                              "https://youtu.be/QjouwbniJSs")

frozen = media.Movie("Frozen",
                     "2013",
                     "PG",
                     "1 hour, 42 minutes",
                     "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "When the newly crowned Queen Elsa accidentally uses " +
                     "her power to turn things into ice to curse her home " +
                     "in infinite winter, her sister, Anna, teams up with " +
                     "a mountain man, his playful reindeer, and a snowman " +
                     "to change the weather condition.",
                     "https://youtu.be/TbQm5doF_Uc")

# add each instance of media to media array
media = [deadpool, the_wolf_of_wall_street, big_hero_6, spider_man_2,
         black_hawk_down, frozen]
# render and open HTML file
render.open_movies_page(media)
