# Jungler Tracking

This is a program designed to track jungler movement in League of Legends using linear algebra techniques, specifically Markov Chains.  The program, when run, generates a series of images, designed to look like heatmaps, to show where the most probable location of the jungler could be.  Note that the transition matrix used is completely arbitrary and could (and should) be modified as the League of Legends meta shifts or other transition matricies are found to be more accurate.

Pull requests are encouraged and appreciated!

## Running the Program
To run the program, run

```bash
$ python track.py
```

This program is built on Python2, but the only Python3 issues should be the print statements which can be easily fixed.  Note that this does depend on numpy's linear algebra library, so you may have to run

```bash
$ pip install numpy
```
if numpy is not already installed.

While the code is running, it will output the numerical probabilities of each location at each iteration, followed by the eigenvector at the end.

At the top of the code, you will find MINR, MING, MINB, and MAXR, MAXG, MAXB variables.  These represent the RGB values of the minimum and maximum color that the heatmap can attain.  Also included is PROB_MAX, which scales down the maximum value (ex. suppose that a location has 10% probability that the jungler is in this location - despite how 10% is low compared to 100%, it still represents a high probability) so probabilities are scaled to a smaller range (and all larger probabilities are scaled to the maximum).

The variable BASE represents which side should the "base" location refer to - set to RED for blue side (enemy jungler is red side) or BLUE for red side (defaults to RED).

The large block of code in the middle represents the transition matrix, and these numbers are commented accordingly for ease of adjustment - ensure that all values within a section add to 1, or the code will not work properly.

Finally, we create the position vector, denoted as x, and initialize a 1 in a certain location to represent knowing with certainty the location of the jungler.  This location can be changed by modifying which position of the vector has the 1 (and thus the location is known to be there).

### Location to Index Table
<ol start=0>
<li>Blue Side Gromp</li>
<li>Blue Side Blue Buff</li>
<li>Blue Side Wolves</li>
<li>Blue Side Wraiths</li>
<li>Blue Side Red Buff</li>
<li>Blue Side Golems</li>
<li>Blue Side Tri-Bush</li>
<li>Baron Pit</li>
<li>Dragon Pit</li>
<li>Lower Scuttle Crab</li>
<li>Upper Scuttle Crab</li>
<li>Red Side Gromp</li>
<li>Red Side Blue Buff</li>
<li>Red Side Wolves</li>
<li>Red Side Wraiths</li>
<li>Red Side Red Buff</li>
<li>Red Side Golems</li>
<li>Red Side Tri-Bush</li>
<li>Top Lane</li>
<li>Mid Lane</li>
<li>Bot Lane</li>
<li>Base</li>
</ol>

## Mathematics of Jungler Tracking
A 22x22 stochastic matrix is constructed, representing the transition matrix (or adjacency matrix) between nodes on the map.  The matrix then acts on the position vector with probabilities of the location of the jungler to generate the next iteration of the position vector.  This process is repeated to generate future position vectors similar to a Markov Chain.  The position vector is updated with the probabilities which are then rendered as heatmaps.

Because the transition matrix is stochastic, we are guarenteed an eigenvalue of 1, as well as at least one eigenvector corresponding to the eigenvalue of 1, known as the Steady-State Vector.  Using numpy's linear algebra library, we are able to determine this eigenvector, which represents the probability distributions of the location of the jungler after a theoretical infinite amount of time.  The significance of this eigenvector is that given no initial conditions on the location of the jungler, the eigenvector represents the probability distribution at any given moment if no information regarding the location is known.

A better model could be created using a (or multiple) partial differential equations, similar to the [Heat Equation](https://en.wikipedia.org/wiki/Heat_equation), as the movement of the jungler is not discretized as a Markov Chain model would predict but instead continuous and a better fit for PDE modeling, but this is beyond my current mathematical scope and will be revisited at a future time.

<!---
## Intended Use
The intended use of this program was to eventually create a set of images that could be referenced at any given time to have an idea of where the jungler could be knowing its previous location.  These images would be consulted during a game of League of Legends, resetting the position vector to a definite state when the jungler is spotted at a certain location, and allowed to iterate when the location is not known.  Further work will be done to create a tool that can efficiently track the junglers' position in real time.
-->

## Screenshots

Heatmap of initial state - jungler position is known to be at Blue Side Blue Buff:
![Initial State](screenshots/minimap0.png?raw=true "Initial heatmap - jungler position known to be at Blue Side Blue Buff")
<br />Iteration 1:<br />
![1st Iteration](screenshots/minimap1.png?raw=true "Heatmap after 1 iteration")
<br />Iteration 2:<br />
![2nd Iteration](screenshots/minimap2.png?raw=true "Heatmap after 2 iterations")
<br />Iteration 3:<br />
![3rd Iteration](screenshots/minimap3.png?raw=true "Heatmap after 3 iterations")
<br />Iteration 4:<br />
![4th Iteration](screenshots/minimap4.png?raw=true "Heatmap after 4 iterations")
<br />Eigenvector:<br />
![Eigenvector](screenshots/eigenvector.png?raw=true "Eigenvector Heatmap")
