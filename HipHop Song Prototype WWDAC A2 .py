# 60 second hip-hop prototype
# Beginner-friendly version with detailed comments explaining each step
from earsketch import *

# --- SETUP ---
init()  # Initializes the EarSketch session. Must always call this first.
setTempo(90)  # Sets the BPM (beats per minute) of the track. 90 BPM is a classic hip-hop tempo.

# SOUND DEFINITIONS 
# Sounds = "clips" or "samples" 
# different intruments - (*synth = synthenizer, electronic sound)
# Each variable stores the name of a sound to use later in fitMedia()
kick = Y60_KICKS_1                # Low-end kick drum for the beat
snare = HIPHOP_DUSTYGROOVE_005    # Snare drum for the backbeat
hihat = HIPHOP_DUSTYGROOVE_006    # Hi-hat for rhythm and groove
bass = HIPHOP_SYNTHBASS_001       # Bassline to support harmony
piano = HIPHOP_DUSTYPIANOLEAD_001 # Piano for chords/melody (foundation of song)
synth = AK_UNDOG_PAD_2             # Pad sound for atmosphere

# Vocals
voc_jayz  = ENTREP_VOX_JAYZ_VRS_1  # Main chorus vocal
voc_pharrell = ENTREP_VOX_JAYZ_VRS_1  # Additional supporting vocal layer
voc_switch = ENTREP_VOX_JAYZ_VRS_2  # Used only in Section 2 for a different vocal/mood

# STRUCTURE TIMING (IN MEASURES)
# Defining number of measures for each section
intro_measures  = 1        
verse1_measures = 4         
chorus_measures = 3          
verse2_measures = 2           
outro_measures  = 1           
end_measure     = 12  # end of first section

# INTRO (Measures 1-4) 
# Gradual intro to build anticipation
# Piano enters first to establish harmony

fitMedia(piano, 1, 1, 7)  # fitMedia(sound, track, startMeasure, endMeasure)
# (*fitMedia = how you fit a sound clip into a specific spot in the timeline)
# Track 1 is where piano will be placed
# It plays from measure 1 through 7 (intro + verse 1)

# setEffect(track, effectType, param, startValue, startMeasure, endValue, endMeasure)
# Applying volume changes to fade the sound in gradually
# (*setEffect = telling a sound how it should change over time, e.g., louder, softer etc.)
setEffect(1, VOLUME, GAIN, -20, 1, 0, 4)  # fade-in piano from -20dB to 0dB over intro
setEffect(1, VOLUME, GAIN, 0, 4, 0, 7)    # maintain full volume into verse 1

# Hi-hat enters slightly later for rhythm
fitMedia(hihat, 2, 2, 7)  # Hi-hat enters at measure 2, continues under verse
setEffect(2, VOLUME, GAIN, -15, 2, 0, 4)  # fade-in hi-hat over intro
setEffect(2, VOLUME, GAIN, 0, 4, 0, 7)    # maintain hi-hat volume under verse

# Light vocal texture enters last for subtle color
fitMedia(voc_jayz, 9, 3, 7)  # measure 3 through 7
setEffect(9, VOLUME, GAIN, -25, 3, -5, 4)  # fade-in soft vocal
setEffect(9, VOLUME, GAIN, -5, 4, -5, 7)   # maintain soft vocal

# Optional tiny pad for atmosphere (pad = a soft subtle background sound)
fitMedia(synth, 6, 4, 7)  # pad enters measure 4
setEffect(6, VOLUME, GAIN, -30, 4, -10, 5)  # gentle fade-in
setEffect(6, VOLUME, GAIN, -10, 5, -10, 7)  # maintain under verse

# SECTION 1: VERSE 1 (Measures 3-6)
# Core rhythm: kick, snare, hi-hat, bass, piano, vocals
fitMedia(kick, 3, 3, 7)       
fitMedia(snare, 4, 3, 7)      
fitMedia(hihat, 2, 3, 7)      
fitMedia(bass, 5, 3, 7)       
fitMedia(piano, 1, 3, 7)      
fitMedia(voc_pharrell, 9, 3, 7)  # additional vocal layer

# Small variation in hi-hat to make rhythm less repetitive
fitMedia(hihat, 2, 5, 6)

# CHORUS: Measures 7-14 
fitMedia(kick, 3, 7, 14)
fitMedia(snare, 4, 7, 14)
fitMedia(hihat, 2, 7, 14)
fitMedia(bass, 5, 7, 14)
fitMedia(piano, 1, 7, 14)
fitMedia(synth, 6, 7, 14)

# Chorus vocal layers
fitMedia(voc_jayz, 10, 7, 14)      # main hook
fitMedia(voc_pharrell, 12, 7, 14)  # extra layer
fitMedia(AK_UNDOG_VOCAL_BKUP_1, 11, 7, 15) # backing vocal for width
fitMedia(AK_UNDOG_VOCAL_BKUP_4, 11, 7, 15) # another backing vocal

fitMedia(COMMON_LOVE_DRUMBEAT_1, 13, 7, 12) # extra drum texture

# VERSE 2: Measures 10-11
fitMedia(kick, 3, 10, 12)
fitMedia(snare, 4, 10, 12)
fitMedia(hihat, 2, 10, 12)
fitMedia(bass, 5, 10, 12)
fitMedia(piano, 1, 10, 12)
fitMedia(synth, 6, 11, 12)

# OUTRO / FADE: Measures 12-14 
fitMedia(piano, 1, 12, 14)   # piano tail
fitMedia(hihat, 2, 12, 14)   # hi-hat tail

# Fade-out volume gradually
setEffect(1, VOLUME, GAIN, 0, 12, -20, 14)
setEffect(2, VOLUME, GAIN, 0, 12, -22, 14)
setEffect(1, REVERB, REVERB_TIME, 1.2)  # subtle echo/reverb (reverb = echoes)

# SECTION 2 (SWITCH-UP)
# Introduce new instruments and vocal texture

switch_kick = Y60_KICKS_1
switch_snare = HIPHOP_DUSTYGROOVE_005
switch_hihat = HIPHOP_DUSTYGROOVE_006
switch_bass = IRCA_SALSA_2_BASS_2
switch_piano = YG_NEW_FUNK_ELECTRIC_PIANO_1
switch_pad = YG_NEW_FUNK_ELECTRIC_PIANO_3
voc_switch = ENTREP_VOX_JAYZ_VRS_2

# Fade out old vocals/synth to avoid overlap
setEffect(10, VOLUME, GAIN, 0, 12, -35, 13)
setEffect(12, VOLUME, GAIN, 0, 12, -35, 13)
setEffect(6, VOLUME, GAIN, 0, 12, -25, 13)

# Stop chorus instruments at measure 13 for clean transition
fitMedia(piano, 1, 7, 13)
fitMedia(bass, 5, 7, 13)
fitMedia(kick, 3, 7, 13)
fitMedia(snare, 4, 7, 13)
fitMedia(hihat, 2, 7, 13)

# Transition cue: riser + hi-hat fill
fitMedia(RD_TRAP_SFX_WASHRISE_1, 8, 13, 14)
fitMedia(HIPHOP_DUSTYGROOVE_006, 2, 13, 14)
setEffect(8, VOLUME, GAIN, -15, 13, 0, 14)
setEffect(8, REVERB, REVERB_TIME, 1.2)

# Section 2 groove
fitMedia(switch_kick, 3, 13, 16)
fitMedia(switch_snare, 4, 13, 16)
fitMedia(switch_hihat, 2, 13, 16)
fitMedia(switch_bass, 5, 13, 16)
fitMedia(switch_piano, 1, 13, 16)
fitMedia(switch_pad, 6, 13, 24) # ambient texture continues

fitMedia(IRCA_SALSA_2_BASS_2, 5, 14, 24)
fitMedia(voc_switch, 9, 13, 24)

# Boundary cues (= a small sound/element that signals a change in the track, anticipates a transition)
fitMedia(hihat, 3, 21, 22)
fitMedia(kick, 3, 22, 23)

# Fade all content toward end
setEffect(1, VOLUME, GAIN, 0, 21, -8, 24)
setEffect(2, VOLUME, GAIN, 0, 21, -8, 24)
setEffect(3, VOLUME, GAIN, 0, 21, -8, 24)
setEffect(4, VOLUME, GAIN, 0, 21, -8, 24)
setEffect(6, VOLUME, GAIN, 0, 21, -8, 24)

# Final hits before silence
fitMedia(hihat, 2, 23, 24)
fitMedia(kick, 3, 23, 24)

# OUTRO: Measures 24-29 
fitMedia(switch_pad, 6, 24, 29)
fitMedia(switch_piano, 1, 24, 28)
fitMedia(switch_bass, 5, 24, 27)
fitMedia(switch_hihat, 2, 24, 26)
fitMedia(voc_switch, 9, 24, 26)

# Vocal fade first
setEffect(9, VOLUME, GAIN, 0, 24, -40, 26)

# Instrumental fade
setEffect(1, VOLUME, GAIN, 0, 26, -40, 29)
setEffect(5, VOLUME, GAIN, 0, 26, -40, 28)
setEffect(2, VOLUME, GAIN, 0, 26, -40, 27)
setEffect(6, VOLUME, GAIN, 0, 26, -40, 29)

# Add reverb for smooth closure
setEffect(1, REVERB, REVERB_TIME, 1.8)
setEffect(6, REVERB, REVERB_TIME, 2.0)

# Optional ambient pad tail
fitMedia(DUBSTEP_PAD_002, 7, 28, 29)
setEffect(7, VOLUME, GAIN, -10, 28, -60, 29)

# End marker
finishMeasure = 29
finish()
