# grep_iplayer

This started out as some functions to grep from iplayer pages.
Uses curl and wget (might want to turn on certificate checks for a laugh)

- ```main``` greps a bunch of href from some object in
the main page or a page it is given as $1
- ```picture``` gets a url to an image from one of the smaller
online resource caches,  takes the programme url, *note* the associated id is not the programme's id. hehe.
- ```description``` is an attempted to pull back the description of the program from the programmes's page url
- ```runme``` is the setup, thing, runs main and captures the output to cache/main, then runs down the list
and creates a pid+|+description file and uses wget to get images, putting them in cache/images

Starting to work on a pi-ready front end to at very least let you look at the pictures, uses pygame:

- ```grep_iplayer.py```

use arrow keys to scroll up and down throug the images in the ```cache/main``` file,
press enter to change the "mode", from *browse* to *pick*
