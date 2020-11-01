import os

# Display settings
DISPTYPE = "psychopy"
DISPSIZE = (1920, 1080)

# Background (BGC) and foreground (FGC) colours.
BGC = (128, 128, 128)
FGC = (0,0,0)

# Experiment specs.
WORDS = ["redwood", "stairs", "kitchen"]
NONWORDS = ["blorb", "glurgle", "tyrmon"]

# Log file name.
LOGFILENAME = raw_input("Participant number: ")

# Find where THIS file is.
DIR = os.path.dirname(__file__)
DATADIR = os.path.join(DIR, "data")

# Find out whether a data directory exists.
if not os.path.isdir(DATADIR):
    os.mkdir(DATADIR)

# Create the path to the log file.
LOGFILE = os.path.join(DATADIR, LOGFILENAME)
