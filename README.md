Authors: Antonio Marino, Zach Glaser, and Hugh Shanno

# Project: Christofides Serdyukov Algorithm Implementation for Rainbow International Route Scheduling
<img width="844" alt="Screen Shot 2022-02-12 at 12 06 01 AM" src="https://user-images.githubusercontent.com/17751446/153699354-f6df49bc-f136-45d0-9bfe-17f3a7cede9a.png">

This folder contains the following:

README.txt: this readme
Main.py: a python file that contains the algorithm
graph.txt: a small text file that contains an example graph for the algorithm to run on.
Files that we still need to edit:
distance.py
graph.txt
jobs.txt
main.py
PreprocessRoutes.py
README.txt

Installation Instructions:
The file can be downloaded as a zip and can be run through any python shell. In order to run the code, navigate to the appropriate directory in your terminal, install the networkx package on the shell by running the commandline "pip install networkx".
Likewise, install geopy -- a python map API -- through "pip install geopy".

File Instructions:
Locations must be a real number distance away from each other.

To perform the Christofides algorithm, graphs must be complete (every node must have an edge to every other node), and satisfy the triangle inequality (the shortest path between any two nodes is the edge between them).


Running Instructions:

## Step 1: 

Fill out the addresses.txt file with a list of addresses of the job sites you want to visit along with the description of the current equipment at that site. Make sure to end the file with a single blank line.

## Step 2: 

Run AddressesToCoordinates.py by typing "python3 AddressesToCoordinates.py". 

## Step 3: 

Any address for which geopy is unable to find the coordinates will produce coordinates of the following form: "ManuallyFill, ManuallyFill". This means that you need to go on google maps, type in the address of the job site and drop a pin near that address in order to get its coordinates. Make sure to end the file with a single blank line.

## Step 4: 

Run PreprocessRoutes.py by typing "python3 PreprocessRoutes.py", and you will see an ordered list of the route you should take. This route is within 1.5 times the optimal route through the job sites.

## Step 5: 

Run main.py by typing "python3 main.py", and you will see an ordered list of the route you should take. This route is within 1.5 times the optimal route through the job sites.

## Step 6: 

Now, You can type "python3 interactiveMap.py", and you will see a map of the route you should take. This route is within 1.5 times the optimal route through the job sites.

