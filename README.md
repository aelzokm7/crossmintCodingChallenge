## Crossmint Coding Challenge

# Background

This repository contains code written for the Crossmint Coding Challenge. The runnable solutions are in phase1.py and phase2.py. For Phase 1, the challenge was to make a given X shape on an 11x11 grid using polyanets with each of / and \ consisting of seven polyanets each. For Phase 2, the challenge was to recreate the Crossmint logo on a grid using polyanets, comeths, and soloons.

# Notes

* Since this was a command line program I used print statements for logging, since the logger would have essentially been doing the same thing. In a proper application, I would use a logger and its accompanying methods to appropriately log the application output.

* Adding tests wasn’t a priority since it wasn't in the criteria of the coding challenge. In an actual project, I would have written tests. 

# Running The Code

1. Clone the repository.
2. Create virtual environment.
    <br/>```python -m venv venv```
    <br />```source venv/bin/activate``` <br/>
3. Install dependencies using ```pip install -r requirements.txt.```
4. Create env file in root directory based on .env.example.
5. Run ```python phase1.py``` or ```python phase2.py``` depending on which challenge you are examining.


# Troubleshooting

* Check the alias of python on your machine. You may need to use python3 in the above commands instead of just python.

* If requirements.txt does not install dependencies, you can manually install them using pip. Again, depending on your configuration, you may need to use pip3 instead of pip.

This code was written using Python 3.13.0.
