## Movie Trailer Website
My final project for "Programming Foundations with Python" under the Full Stack Web Developer Nanodegree [(View on Udacity)](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

#

### Project overview
Built with Python, this project makes use of classes, objects, inheritance, and data from the Internet in order to render a website displaying my favorite movies.

### Summary
`media.py`
Contains main classes for all instances of media
* `Video` class contains common instance variables
* `Movie` class inherits from `Video` class and instantiates movie-specific variables

`data.py`
Contains the main data for the website
* Instances of `Movie` class representing my favorite movies
* Stored in array for use by `render.py`

`render.py`
Contains instructions to render an HTML page to display data
* Modified from Udacity's `fresh_tomatoes.py` [(View on GitHub)](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py)
* Generates an HTML file to display data

_Movie information from [IMDb](http://www.imdb.com/), trailers from [YouTube](https://www.youtube.com)_

### Running the project
_Procedures may vary for non-Windows platforms_
#### Initial steps
1. Please make sure you have [Python v2.7.*](https://www.python.org/downloads/release/python-2711/) installed and configured on your machine
2. Download or clone this repository (optionally, clone using Visual Studio)
3. Take note of where the contents are saved

#### IDLE (Python GUI) instructions
1. Open IDLE
2. Click on `File > Open` and open the 3 `*.py` modules under `Movie-Trailer-Website`
3. Switch to the `data.py` module window, click on `Run > Run Module`

#### Visual Studio instructions
1. Clone repository using Visual Studio
2. Open project solution in Visual Studio
2. Open the 3 `*.py` modules within the IDE
3. Run the project, and select `data.py` as the main file

