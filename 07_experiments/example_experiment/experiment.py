import random

from constants import *

from pygaze.display import Display
from pygaze.screen import Screen
from pygaze.sound import Sound
from pygaze.keyboard import Keyboard
from pygaze.logfile import Logfile
import pygaze.libtime as timer

# Create a new Display instance.
disp = Display()

# Create a new Keyboard instance.
kb = Keyboard()

# Create a new Logfile instance.
log = Logfile()
log.write(["trialnr", "trial_type", "stimulus", \
    "fix_onset", "stim_onset", "response", "RT", \
    "correct"])

# Create a BAD sound.
bad_sound = Sound(osc="whitenoise", length=200)
bad_sound.set_volume(1)
good_sound = Sound(osc="sine", freq=440, length=200)
good_sound.set_volume(0.5)

# Create a new Screen instance.
scr = Screen()
scr.draw_text("Welcome!", fontsize=100, \
    colour=(255,100,100))

# Pass the screen to the display.
disp.fill(scr)
disp.show()
timer.pause(3000)

# Create a list of all trials.
trials = []
# Add all the words.
for word in WORDS:
    t = {}
    t["type"] = "word"
    t["stimulus"] = word
    trials.append(t)
# Add all the nonwords.
for word in NONWORDS:
    t = {}
    t["type"] = "nonword"
    t["stimulus"] = word
    trials.append(t)
# Randomise the order.
random.shuffle(trials)

# Loop through all trials.
for i, trial in enumerate(trials):

    # Draw the fixation screen.
    fixscr = Screen()
    fixscr.draw_fixation(fixtype="cross", diameter=32, pw=3)
    # Show the fixation screen on the monitor.
    disp.fill(fixscr)
    fix_onset_time = disp.show()
    # Wait for a wee bit.
    timer.pause(1000)
    
    # Draw the stimulus for this trial.
    stimscr = Screen()
    stimscr.draw_text(trial["stimulus"], fontsize=75)
    # Show the stimulus word / nonword.
    disp.fill(stimscr)
    stim_onset_time = disp.show()
    
    # Get a response.
    pressed_key, press_time = kb.get_key( \
        keylist=["left", "right"], timeout=3000)
    # Compute the response time.
    resp_time = press_time - stim_onset_time
    # See if we need to wait for a bit more.
    if pressed_key is not None:
        timer.pause(3000 - resp_time)
    
    # Check whether the response was correct.
    if trial["type"] == "word":
        if pressed_key == "left":
            correct = 1
        else:
            correct = 0
    elif trial["type"] == "nonword":
        if pressed_key == "right":
            correct = 1
        else:
            correct = 0
    else:
        correct = "WOW NO THIS IS NOT SUPPOSED TO HAPPEN"

    # Add feedback.
    if correct:
        good_sound.play()
    else:
        bad_sound.play()
    
    # Record the response.
    log.write([i, trial["type"], trial["stimulus"], \
        fix_onset_time, stim_onset_time, \
        pressed_key, resp_time, correct])
    
    # Inter-trial interval.
    disp.fill()
    disp.show()
    timer.pause(1500)

# Neatly close the logfile.
log.close()

# Exit the display.
disp.close()
