#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.00), February 06, 2015, at 12:48
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Rosvold CPT'  # from the Builder filename that created this script
expInfo = {u'Gender': u'female', u'Handedness': u'Right', u'participant': u'100'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "first_slide"
first_slideClock = core.Clock()
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text='A fixation will be placed onscreen during your preliminary scans/set up.\n\nPress Space Bar to continue when your participant is ready for the experiment.\n\nPress Space Bar to go to the fixation screen now.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "init_fix"
init_fixClock = core.Clock()
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Welcome = visual.TextStim(win=win, ori=0, name='Welcome',
    text='Welcome to the CTE Study\n\nPress any button when ready to continue',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
'''
Total time to record MRI sequence:
    Seconds: ~329.9789
    Minutes: 5.4996483333333333333333333333333
Expected time:
    Seconds: 330
    Minutes: 5.5
'''

################################
############## NS Initialization
# >>> import and initialization >>> 
import egi.threaded as egi
ms_localtime = egi.ms_localtime     
ns = egi.Netstation()
ns.initialize('10.10.10.52', 55513)
ns.BeginSession()
ns.sync()
############## NS Initialization
################################

correctButton = '1'

'''
#pick random number from 1-100 for determining if this is an nBack round or not
bias = randint(1, 100)
print 'Bias:'
print bias
currentLetter = nBackLets[randint(0,25)]
print currentLetter
#check that enough rounds have passed to display an nBack
if position-nBack >= 0:
    #determine if next letter will be new or a nBack match, currently 50/50 odds
    if bias < 50:
        currentLetter = oldLets[position-nBack]
        print "nbacked"
        print currentLetter
        corAns = '1'
    else:
        corAns = 'None'
'''

# Initialize components for Routine "AreYouSure_"
AreYouSure_Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text="After this point we won't stop the experiment, unless there is a problem.\n\nAre you sure you are ready? If so, press any key.",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "MRI_sync"
MRI_syncClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='Waiting for trigger pulse...',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "nBack"
nBackClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='N-back Instructions.jpg', mask=None,
    ori=0, pos=[0, 0], size=[1.125, 1.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "trials_3"
trials_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='default text',    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
corAns = ''
nBackLetter = 'A'
currentLetter = 'A'
oldLets = []
nBackLets = []
position=0
correctAns=0
nBack = 2
print nBack
#array of letters to sample from
nBackLets = map(chr, range(65, 91))

# Initialize components for Routine "interrupt_overTR"
interrupt_overTRClock = core.Clock()
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text='Experimenter: if the functional scan is still running, wait for it to finish/cancel, then press SPACEBAR for next sync screen.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "end"
endClock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='Thank you, the study is complete. Please wait patiently for the technician to assist you out of the MRI.',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "first_slide"-------
t = 0
first_slideClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_18 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_18.status = NOT_STARTED
# keep track of which components have finished
first_slideComponents = []
first_slideComponents.append(text_15)
first_slideComponents.append(key_resp_18)
for thisComponent in first_slideComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "first_slide"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = first_slideClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if t >= 0.0 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t  # underestimates by a little under one frame
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)
    
    # *key_resp_18* updates
    if t >= 0.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t  # underestimates by a little under one frame
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        key_resp_18.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_18.keys = theseKeys[-1]  # just the last key pressed
            key_resp_18.rt = key_resp_18.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in first_slideComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "first_slide"-------
for thisComponent in first_slideComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
   key_resp_18.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.nextEntry()

#------Prepare to start Routine "init_fix"-------
t = 0
init_fixClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_17 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_17.status = NOT_STARTED
# keep track of which components have finished
init_fixComponents = []
init_fixComponents.append(text_14)
init_fixComponents.append(key_resp_17)
for thisComponent in init_fixComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "init_fix"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = init_fixClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t  # underestimates by a little under one frame
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *key_resp_17* updates
    if t >= 0.0 and key_resp_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_17.tStart = t  # underestimates by a little under one frame
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        key_resp_17.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_17.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_17.keys = theseKeys[-1]  # just the last key pressed
            key_resp_17.rt = key_resp_17.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in init_fixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "init_fix"-------
for thisComponent in init_fixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
   key_resp_17.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.nextEntry()

#------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
trialComponents = []
trialComponents.append(Welcome)
trialComponents.append(key_resp_2)
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "trial"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if t >= 0.0 and Welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome.tStart = t  # underestimates by a little under one frame
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()


#------Prepare to start Routine "AreYouSure_"-------
t = 0
AreYouSure_Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
AreYouSure_Components = []
AreYouSure_Components.append(text_6)
AreYouSure_Components.append(key_resp_7)
for thisComponent in AreYouSure_Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "AreYouSure_"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = AreYouSure_Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AreYouSure_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "AreYouSure_"-------
for thisComponent in AreYouSure_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
   key_resp_7.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()

#------Prepare to start Routine "MRI_sync"-------
t = 0
MRI_syncClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
ns.StartRecording()
# keep track of which components have finished
MRI_syncComponents = []
MRI_syncComponents.append(text_2)
MRI_syncComponents.append(key_resp_4)
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "MRI_sync"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = MRI_syncClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['num_multiply', '8'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MRI_syncComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "MRI_sync"-------
for thisComponent in MRI_syncComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()


#------Prepare to start Routine "nBack"-------
t = 0
nBackClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_9.status = NOT_STARTED
ns.sync()
ns.send_event( 'inst', label="Begin Instructions", timestamp=egi.ms_localtime(), table = {'time' : egi.ms_localtime()} ) 

# keep track of which components have finished
nBackComponents = []
nBackComponents.append(key_resp_9)
nBackComponents.append(image)
for thisComponent in nBackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "nBack"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = nBackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_9* updates
    if frameN >= 0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # underestimates by a little under one frame
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        key_resp_9.clock.reset()  # now t=0
    elif key_resp_9.status == STARTED and frameN >= 1800:
        key_resp_9.status = STOPPED
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['*'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys.extend(theseKeys)  # storing all keys
            key_resp_9.rt.append(key_resp_9.clock.getTime())
    
    # *image* updates
    if frameN >= 0 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t  # underestimates by a little under one frame
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    elif image.status == STARTED and frameN >= 1800:
        image.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nBackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "nBack"-------
for thisComponent in nBackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
   key_resp_9.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()


# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7.keys():
        exec(paramName + '= thisTrial_7.' + paramName)

for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7.keys():
            exec(paramName + '= thisTrial_7.' + paramName)
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ns.sync()
    
    #pick random number from 1-100 for determining if this is an nBack round or not
    bias = randint(1, 100)
    print 'Bias:'
    print bias
    currentLetter = nBackLets[randint(0,25)]
    print currentLetter
    #check that enough rounds have passed to display an nBack
    if position-nBack >= 0:
        #determine if next letter will be new or a nBack match, currently 50/50 odds
        if bias < 50:
            currentLetter = oldLets[position-nBack]
            print "nbacked"
            print currentLetter
            corAns = '1'
        else:
            corAns = 'None'
    
    key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_11.status = NOT_STARTED
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(text_7)
    fixationComponents.append(key_resp_11)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if frameN >= 0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        elif text_7.status == STARTED and frameN >= 120:
            text_7.setAutoDraw(False)
        
        
        # *key_resp_11* updates
        if frameN >= 59 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t  # underestimates by a little under one frame
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            key_resp_11.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif key_resp_11.status == STARTED and frameN >= 120:
            key_resp_11.status = STOPPED
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_multiply', '8'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                key_resp_11.rt = key_resp_11.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
       key_resp_11.keys=None
    # store data for trials_7 (TrialHandler)
    trials_7.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials_7.addData('key_resp_11.rt', key_resp_11.rt)
    
    #------Prepare to start Routine "trials_3"-------
    t = 0
    trials_3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    text_8.setText(currentLetter)
    key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_10.status = NOT_STARTED
    oldLets.append(currentLetter)
    nBackYesNo = 'N/A'
    if position-nBack >= 0:
        if currentLetter == oldLets[position-nBack]:
            corAns = '1'
            nBackYesNo = 'Yes'
        else:
            corAns = 'None'
            nBackYesNo = 'No'
    
    ns.send_event( 'lttr', label="Letter Presented", timestamp=egi.ms_localtime(), table = {'ltr-' : currentLetter, 'nbk?' : nBackYesNo, 'time' : egi.ms_localtime()} ) 
    
    key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_12.status = NOT_STARTED
    # keep track of which components have finished
    trials_3Components = []
    trials_3Components.append(text_8)
    trials_3Components.append(key_resp_10)
    trials_3Components.append(key_resp_12)
    for thisComponent in trials_3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trials_3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trials_3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if frameN >= 0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        elif text_8.status == STARTED and frameN >= 60:
            text_8.setAutoDraw(False)
        
        # *key_resp_10* updates
        if frameN >= 0 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # underestimates by a little under one frame
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # AllowedKeys looks like a variable named `correctButton`
            if not 'correctButton' in locals():
                logging.error('AllowedKeys variable `correctButton` is not defined.')
                core.quit()
            if not type(correctButton) in [list, tuple, np.ndarray]:
                if not isinstance(correctButton, basestring):
                    logging.error('AllowedKeys variable `correctButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in correctButton: correctButton = (correctButton,)
                else:  correctButton = eval(correctButton)
            # keyboard checking is just starting
            key_resp_10.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif key_resp_10.status == STARTED and frameN >= 60:
            key_resp_10.status = STOPPED
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=list(correctButton))
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # was this 'correct'?
                if (key_resp_10.keys == str(corAns)) or (key_resp_10.keys == corAns):
                    key_resp_10.corr = 1
                else:
                    key_resp_10.corr = 0
        
        
        # *key_resp_12* updates
        if frameN >= 0 and key_resp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_12.tStart = t  # underestimates by a little under one frame
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            key_resp_12.clock.reset()  # now t=0
        elif key_resp_12.status == STARTED and frameN >= 60:
            key_resp_12.status = STOPPED
        if key_resp_12.status == STARTED:
            theseKeys = event.getKeys(keyList=['num_multiply'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_12.keys.extend(theseKeys)  # storing all keys
                key_resp_12.rt.append(key_resp_12.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trials_3"-------
    for thisComponent in trials_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
       key_resp_10.keys=None
       # was no response the correct answer?!
       if str(corAns).lower() == 'none': key_resp_10.corr = 1  # correct non-response
       else: key_resp_10.corr = 0  # failed to respond (incorrectly)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('key_resp_10.keys',key_resp_10.keys)
    trials_7.addData('key_resp_10.corr', key_resp_10.corr)
    if key_resp_10.keys != None:  # we had a response
        trials_7.addData('key_resp_10.rt', key_resp_10.rt)
    trials_7.addData("nBack_Letter", currentLetter, trials_7.thisN)
    
    if currentLetter == oldLets[position-nBack]:
        correctButton = '1'
    else:
        correctButton = None
    
    if (key_resp_10.keys == correctButton):
        evaluation = 'correct'
        keyResp = key_resp_10.keys
    else:
        evaluation = 'incorrect'
        keyResp = 'None'
    
    ns.send_event( 'rsp-', label="Subject Response", timestamp=egi.ms_localtime(), table = {'resp': keyResp, 'eval': evaluation, 'time' : egi.ms_localtime()} ) 
    
    '''
    oldLets.append(currentLetter)
    print oldLets
    if position-nBack >= 0:
        print oldLets[position-nBack]
        print position-nBack
        if currentLetter == oldLets[position-nBack]:
            print 'Current letter is a match'
            print key_resp_10.keys
            if (key_resp_10.keys == correctButton):
                key_resp_10.corr = 1
                correctAns = correctAns + 1
                print 'good'
                print correctAns
            else:
                key_resp_10.corr = 0
                print 'bad'
        if currentLetter != oldLets[position-nBack]:
            print 'Current letter is not a match'
            print key_resp_10.keys
            if (key_resp_10.keys == 'None'):
                key_resp_10.corr = 1
                correctAns = correctAns + 1
                print 'good'
                print correctAns
            else:
                key_resp_10.corr = 0
                print 'bad'
    '''
    position = position + 1
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
       key_resp_12.keys=None
    # store data for trials_7 (TrialHandler)
    trials_7.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        trials_7.addData('key_resp_12.rt', key_resp_12.rt)
    thisExp.nextEntry()
    
# completed 100 repeats of 'trials_7'

# get names of stimulus parameters
if trials_7.trialList in ([], [None], None):  params = []
else:  params = trials_7.trialList[0].keys()
# save data for this loop
trials_7.saveAsExcel(filename + '.xlsx', sheetName='trials_7',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_7.saveAsText(filename + 'trials_7.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "interrupt_overTR"-------
t = 0
interrupt_overTRClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_14.status = NOT_STARTED
# keep track of which components have finished
interrupt_overTRComponents = []
interrupt_overTRComponents.append(text_12)
interrupt_overTRComponents.append(key_resp_14)
for thisComponent in interrupt_overTRComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "interrupt_overTR"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = interrupt_overTRClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # underestimates by a little under one frame
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t  # underestimates by a little under one frame
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        key_resp_14.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_14.keys = theseKeys[-1]  # just the last key pressed
            key_resp_14.rt = key_resp_14.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in interrupt_overTRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "interrupt_overTR"-------
for thisComponent in interrupt_overTRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
   key_resp_14.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()

#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
routineTimer.add(20.000000)
# update component parameters for each repeat
ns.StopRecording()
# keep track of which components have finished
endComponents = []
endComponents.append(text_9)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # underestimates by a little under one frame
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)
    elif text_9.status == STARTED and t >= (0.0 + (20-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_9.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)







win.close()
core.quit()
