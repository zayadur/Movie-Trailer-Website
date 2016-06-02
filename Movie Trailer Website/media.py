# media.py provides the instance methods and variables that each instance uses.
# This file was modeled after Udacity's "Programming Foundations with Python"
#   Movie Website exercises, including the inheritance demonstration.

# Created by Zayadur Khan <http://www.zayadur.me">

import webbrowser

# overarching class for all video types
class Video():
    def __init__(self, title, image, description):
        self.title = title
        self.image = image
        self.description = description

# new class for movie video type
class Movie(Video):
    def __init__(self, title, year, rating, duration, image, description,
                 trailer):
        Video.__init__(self, title, image, description)  # declare instance...
        #   variables from Video class
        #  specific instance variables for Movie class
        self.year = year
        self.duration = duration
        self.rating = rating
        self.trailer = trailer
