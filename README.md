# Traffic Simulation
a)"mp2.pdf" is the report

b) Sections of code are separated by a header. There are 8 sections:

Global Variables (change number of cars, dally factor, and max speed)
Car Class
Initialization functions
4 Steps of CA Model (accelerate, decelerate, dally, move)
Models (one lane, two lane)
Helper functions (distance, switch lanes, checklanes)
Plotting
Verification (annotates cells and shows each car's speed)
I created a car class to organize the information of each car. The "road" is made up of a list and I put cars in the list (empty cells contain a -1). The plotting functions are at the end of the code and I kept track of the velocities in a matrix.

The CA_model2 is the two lane model. It contains the same logic as the first one except it adds lane changes.
