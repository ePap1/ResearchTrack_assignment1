# ResearchTrack_assignment1
This package relies on the portable robot simulator developed by [Student Robotics](https://studentrobotics.org/). 

In the context of the Research Track 1 class of the Robotics Engineering master of the University of Genoa (UniGe), a robot programming problem has been implemented using the simulated environment and this package offers a solution to it. 

The part that I developped for this assignment is just one python executable named assignment1.py which controls the robot's mouvement in the simulation. 

## Installation and running

The Student Robotics' simulator requires a Python 2.7 installation, as well as the librairies [pygame](https://www.pygame.org/news), [PyPyBox2D](https://pypi.org/project/pypybox2d/2.1-r331/) and [PyYAML](https://pypi.org/project/PyYAML/).

Once the dependencies are installed, simply run the test.py script to test out the simulator.

To run this exercise's solution, assignment1.py, use the following command : python2 run.py assignment1.py

## Description of the environment

 The robot evolves in a 2D environment where we can find:

 * golden boxes, disposed in such ways to create the walls of a circuit
 * silver boxes, dispersed along the corridors

The functions already programmed in the simulator allow us to drive the robot forward, to make it turn, to survey its surroundings and to grab nearby objects.

## Assignemnent's goals

The code written should control the robot in such way that :

1. The robot drives along the circuit corridors in the counter-clockwise direction.
2. It should avoid touching the golden boxes at any time.
2. When it is close enough to a silver box, the robot should grab the box, move it behind him, then continue his journey in a counter-clockwise motion.

## Main Functions

* *find_silver* : this function looks for the closest silver box to the robot, limiting the area of search to a range of 1.5 unit of distance, and with a field of vision of \[-90°;+90°] (looks forward). It returns the distance and angle to the closest silver box.

* *orient* : Using find_silver, if any silver box was detected, this function orients the robot towards the box. It returns the distance to the silver box.

* *obstacle* : This functions survey the surroundings of the robot, in a given range and field of vision given as inputs. It looks for golden boxes and return the angle between the robot and the closest golden box.

* *avoid* and *corner*: These functions alter the course of the robot so that it follows the corridors. They use the function obstacle() to adjust the modification of the course according to where the obstacle was detected.

* *task* : With this function, the robot grabs a silver box and places it behind him.

## Code Flowchart

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1JvYm90XSAtLT4gQltkcml2ZSBhIGxpdHRsZSBmb3J3YXJkXVxuICAgIEIgLS0-IEN7SW5maW5pdGUgbG9vcH1cbiAgICBDIC0tPiBEKFNpbHZlciBib3ggbmVhcmJ5PylcbiAgICBEIC0tPiB8Tm98IEUoT2JzdGFjbGVzIG9uIGNvdXJzZT8pXG4gICAgRSAtLT4gfE5vfCBGW2RyaXZlIGEgc3RlcCBmb3J3YXJkXVxuICAgIEYgLS0-IENcbiAgICBEIC0tPiB8WWVzfCBHW21vZGlmeSBjb3Vyc2UgdG93YXJkIGJveF1cbiAgICBHIC0tPiBIKENsb3NlIGVub3VnaD8pXG4gICAgSCAtLT4gfE5vfCBFXG4gICAgSCAtLT4gfFllc3wgSVtncmFiIGJveCwgcGxhY2UgaXQgYmVoaW5kXVxuICAgIEkgLS0-IEVcbiAgICBFIC0tPiB8WWVzfCBKW21vZGlmeSBjb3Vyc2UgdG8gZ2V0IGF3YXldXG4gICAgSiAtLT4gfHNpZ24gb2YgYW5nbGUgdG8gb2JzdGFjbGV8IEsoSW4gYSBjb3JuZXI_KVxuICAgIEsgLS0-IHxZZXN8IExbdHVybiBjaXJjYSA5MCBkZWdyZWVzIHRvIGV4aXQgY29ybmVyXVxuICAgIEsgLS0-IHxOb3wgRVxuICAgIEwgLS0-IEVcbiAgICBcbiAgICIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit/#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1JvYm90XSAtLT4gQltkcml2ZSBhIGxpdHRsZSBmb3J3YXJkXVxuICAgIEIgLS0-IEN7SW5maW5pdGUgbG9vcH1cbiAgICBDIC0tPiBEKFNpbHZlciBib3ggbmVhcmJ5PylcbiAgICBEIC0tPiB8Tm98IEUoT2JzdGFjbGVzIG9uIGNvdXJzZT8pXG4gICAgRSAtLT4gfE5vfCBGW2RyaXZlIGEgc3RlcCBmb3J3YXJkXVxuICAgIEYgLS0-IENcbiAgICBEIC0tPiB8WWVzfCBHW21vZGlmeSBjb3Vyc2UgdG93YXJkIGJveF1cbiAgICBHIC0tPiBIKENsb3NlIGVub3VnaD8pXG4gICAgSCAtLT4gfE5vfCBFXG4gICAgSCAtLT4gfFllc3wgSVtncmFiIGJveCwgcGxhY2UgaXQgYmVoaW5kXVxuICAgIEkgLS0-IEVcbiAgICBFIC0tPiB8WWVzfCBKW21vZGlmeSBjb3Vyc2UgdG8gZ2V0IGF3YXldXG4gICAgSiAtLT4gfHNpZ24gb2YgYW5nbGUgdG8gb2JzdGFjbGV8IEsoSW4gYSBjb3JuZXI_KVxuICAgIEsgLS0-IHxZZXN8IExbdHVybiBjaXJjYSA5MCBkZWdyZWVzIHRvIGV4aXQgY29ybmVyXVxuICAgIEsgLS0-IHxOb3wgRVxuICAgIEwgLS0-IEVcbiAgICBcbiAgICIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)

## Possible improvements

For now, the robot uses the function obstacle(range, cone) with different parameters depending on the situation. If these parameters work well enough, it is still not easy to justify the different values (they were chosen after a number of tries). I think using slightly different approaches (instead of just different parameters) for theses different situation might improve the code. As of now, after several laps, the robot sometimes changes course and starts driving clock-wisen after he failed to pass a corner.
