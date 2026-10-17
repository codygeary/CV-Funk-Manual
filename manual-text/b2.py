MODULES = {
"impulse-controller": {
"tagline": "Fire an impulse into a 24-node network and watch it ripple out. Every node is an envelope output.",
"panelMap": """IMPULSE CONTROLLER sends a pulse through a branching network of 24 nodes. Each node rings with its own decay envelope when the pulse reaches it, then wakes the nodes after it. You get 24 related envelopes that fire in rhythm with your input, spread out in time like a wave moving through a medium.

Controls (each with an attenuverter and CV input):
- LAG: how long a pulse takes to travel from one node to the next.
- SPREAD: how the nodes line up in time. Turn left to pull them into unison, right to spread them apart.
- DECAY: how long each node rings once it's hit.

[[fig:network]]

Jacks:
- IN: a gate or trigger here fires the first node. The button above does the same.
- IMPULSES: 24 envelope outputs. The light next to each one shows its level, and the red trail shows the pulse moving through the network.""",
"basicUse": """1. Set the shape of the wave:
   - LAG sets the travel time between nodes, DECAY sets how long each node rings.

2. Fire it:
   - Patch a clock or gate into IN, or press the button.

3. Adjust SPREAD:
   - A node can only pass the pulse on once it has decayed below a threshold, and SPREAD sets that threshold. At the far left, nodes fire in unison.
   - SPREAD also scales the timing down the network. Negative SPREAD makes each later node fire sooner; positive SPREAD stretches each step to 1–2x longer.

[[fig:threshold]]

[[fig:spread]]

4. Patch the outputs:
   - Treat the 24 outputs as a bank of related envelopes. Send them to VCAs, filters, panners or other modules' CV inputs.""",
"patching": """• Moving sound: Send groups of outputs to the pan or level CVs of a mixer. Each pulse sweeps across the stereo field as it travels through the network.

• Related modulation: Patch different nodes to different parameters. Everything moves together but never quite in sync.

• Self-patched networks: Patch node outputs back into IN, or into LAG, SPREAD and DECAY. Press the button to start it, then watch the pulse circulate. Patching several IMPULSE CONTROLLERs into each other builds bigger rhythmic networks.""",
"figures": [
  {"id": "network", "src": "/figures/impulse-controller/network.png", "caption": "How the 24 nodes connect. The pulse enters at node 1 and branches outward.", "section": "panelMap"},
  {"id": "threshold", "src": "/figures/impulse-controller/threshold.png", "caption": "A node passes the pulse on once its envelope decays below the threshold set by SPREAD.", "section": "basicUse"},
  {"id": "spread", "src": "/figures/impulse-controller/spread.png", "caption": "SPREAD also scales node timing, shortening or stretching the gap at each step down the network.", "section": "basicUse"}
]
},

"signals": {
"tagline": "A six-channel scope that fits in your signal path. Good for tuning envelopes and LFOs.",
"panelMap": """SIGNALS shows six signals at once in a narrow module, and passes each one straight through so you can leave it in the patch. It's handy for dialing in envelope and LFO shapes.

Controls:
- RANGE knob: time window, up to 1 second.
- SLOW switch: stretches the window to 10 seconds.
- RETRIG button: with the light on, each trace restarts on a rising edge through 1V, so envelopes stand still on the screen. Turn it off for free-running signals.

Jacks:
- Inputs (left): six signals. A polyphonic cable fills the channels below it until the next patched input.
- PASS outputs (right): each input passes through unchanged.""",
"basicUse": """1. Patch up to six signals into the inputs.
2. Use the PASS outputs to carry on to wherever the signals were going.
3. Set the time window with RANGE. Flip SLOW for LFOs and long envelopes.
4. Leave RETRIG on to freeze repeating envelopes in place. Turn it off to watch signals roll past.""",
"patching": """• Envelope tuning: Put SIGNALS between an envelope and its VCA. With RETRIG on, the shape holds still while you turn the knobs.

• Compare a family: Patch all six outputs of ENVELOPE ARRAY or HEX MOD in at once to see how they relate.

• Setting up audio-rate tricks: Use a short RANGE to check wavelengths, for example when setting FIRST WIDTH for the ENVELOPE ARRAY sub-harmonics patch."""
},

"ranges": {
"tagline": "Evenly spaced voltages between TOP and BOTTOM. Scales, crossfades, panning and gate scanning.",
"panelMap": """RANGES fills in the voltages between TOP and BOTTOM in equal steps. DIVS sets how many steps, and one more output lights up for each. Because everything is under CV, the same module works as an interval generator, a multi-way crossfader, a panning spreader or a gate scanner.

Controls (each with an attenuverter and CV input):
- TOP: voltage of the top output, ±10V. Adds to its CV.
- BOTTOM: voltage of the bottom active output, ±10V. Adds to its CV.
- DIVS: number of divisions, 0–12. Each volt of CV adds about 2.4 divisions.

Jacks:
- OUTS: up to 13 outputs, from TOP down to BOTTOM. The lights show which are active. Inactive outputs sit at 0V.
- TOP and BOTTOM are polyphonic: patch poly cables in and every output becomes a poly cable.""",
"basicUse": """1. Set TOP and BOTTOM.
2. Set DIVS. The outputs in between are evenly spaced.
3. Patch the outputs anywhere you need a set of related voltages.""",
"patching": """• Chromatic scale: TOP 0V, BOTTOM 1V, DIVS 12. Each output is one semitone higher than the last.

• Perfect fourths: TOP 0V, BOTTOM 5V, DIVS 12. Each step is 5/12V, a perfect fourth.

• Crossfader: Patch two signals into the TOP and BOTTOM inputs with both attenuverters at 1 and both knobs at 0. The outputs are blends of the two, from all TOP to all BOTTOM. Change DIVS for more or fewer blends.

• Group panning: Set TOP and BOTTOM to 0 with attenuverters at 1. Patch -5V and +5V into a crossfader (VCV FADE works) and its outputs into TOP and BOTTOM. Set DIVS to your number of mixer channels and patch the outputs to the pan CVs. Moving the fader pans every channel at once.

• Gate scanner: TOP 5V, BOTTOM 5V, DIVS 0. Patch outputs 3 and up to gate inputs. A rising voltage into DIVS turns them on one by one."""
},

"hex-mod": {
"tagline": "Six phase-related LFOs. NODES rearranges their phases from evenly spread to unison and back.",
"panelMap": """HEX MOD is six sine LFOs running at one rate. NODES sets how their phases are arranged around the cycle: evenly spread in a hexagon, all together, or grouped in twos and threes. A trigger on any channel pulls its phase back to zero, and it eases back into place afterwards.

Controls:
- RATE: speed of all six LFOs, up to 20 Hz. The button beside it switches to slow mode, where the knob covers 1/20 of the range. RATE has an attenuverter and CV input.
- NODES: phase arrangement. 0 = hexagonal (evenly spaced), 1 = unison, 2 = two groups, 3 = three groups. In between, it morphs. Attenuverter and CV.
- RANGE: output level, ±10V. The CV input lets RANGE act as a bipolar VCA.
- SYNC: locks the LFOs to an external clock or oscillator. By default, patching SYNC takes over from the RATE knob.

Jacks:
- PHASE RESET (top row): one per LFO. A trigger resets that output to zero phase. An envelope eases the phase back to its NODES position, and a gate holds the phase while it's high. Each input is normalled to the next, in a loop.
- Outputs: six LFOs, at the corners of the hexagon.

Lights: each output has 10 lights. Red lights are +1V each, blue lights are -1V each.

Context menu:
- Enable Lights: turns the lights off if you'd rather not have them blinking.
- Rate multiplies the Sync Input: RATE multiplies the synced clock instead of being ignored. RATE 1 follows the clock, RATE 2 doubles it.
- Sync locks both Clock and Phase: on by default, so each clock pulse also realigns the phases. Turn it off to let the phases run free and reset them with the PHASE RESET inputs.
- Rate input take v/oct (for audio rate): RATE CV tracks V/oct for audio-rate use. The RATE knob and attenuverter are disabled.
- Enable Polyphonic Output to Channel 1: output 1 carries all six LFOs.""",
"basicUse": """1. Set the speed with RATE, and the phase arrangement with NODES.
2. Patch the six outputs to six destinations.
3. Patch triggers or envelopes into the PHASE RESET inputs to pull channels into line and let them drift back. One trigger into the first input resets all six, because they're normalled.
4. Patch a clock into SYNC to lock to tempo.
5. Use RANGE to set the output level, or patch CV into it to use it as a VCA.""",
"patching": """• Panning in a circle: Send the six outputs to the pan CVs of six mixer channels. With NODES at 0 the sounds sit evenly around the stereo field and rotate. A trigger into a PHASE RESET input groups them together in space, and then they slowly spread out again. Try other NODES settings to group them differently.

• Self-modulation: Patch one output into RATE and another into NODES, with a little attenuation on each. The six LFOs start bending each other's shapes.

• Audio-rate timbres: Turn on v/oct mode in the context menu. Patch output 2 into NODES with the attenuverter at 0.1 and listen to output 4. Turn NODES for timbre. Every output sounds different, so try them all."""
},

"collatz": {
"tagline": "Rhythms from the Collatz conjecture. Pick a number and listen to it fall to 1.",
"panelMap": """COLLATZ turns Collatz sequences into rhythm. Pick a starting number. If it's even, halve it. If it's odd, triple it and add one. Repeat. The Collatz conjecture says you always end up at 1, and when the module gets there it stops and sends an END gate.

Each number in the sequence becomes a burst of gates within one clock interval. MODULUS caps the bursts: the remainder (number mod MODULUS) sets how many pulses go to OUT, and the quotient sets the accents on ACC. The display shows the current number, the modulus, and the beats-to-accents split.

Controls (each with an attenuverter and CV input):
- NUMBER: starting number, 2–1000.
- MODULUS: maximum pulses per clock interval, 1–100.

Jacks:
- CLOCK: required. The time between clock pulses sets the length of each burst.
- RESET: stops the sequence and turns the outputs off. Also has a button.
- START: arms a new run using the current NUMBER. It starts on the next clock pulse. Also has a button.
- OUT: the main gate bursts, 50% pulse width.
- ACC: accent gates.
- END: goes high when the sequence reaches 1. Patch END into START to loop.""",
"basicUse": """1. Patch a clock into CLOCK. Without a clock the module stays silent.
2. Set NUMBER and MODULUS. For drum patterns keep MODULUS low. Higher settings can run up to audio rate.
3. Press START or send it a trigger. The sequence begins on the next clock.
4. Patch OUT and ACC to drums.
5. Patch END into START to repeat the sequence forever.""",
"patching": """• Drums: The gates are short and snappy, which suits snares and percussion. Clock it from your main clock or a division, and patch END into START so it cycles.

• Simple patterns: Powers of two give plain, predictable runs, like rotating clock divisions:
  32→16→8→4→2→1
  8→4→2→1

• Nested patterns: Many sequences contain each other, so you can pick the length you want:
  12→6→3→10→5→16→8→4→2→1
  5→16→8→4→2→1

• Long walks: Small odd numbers can wander for a long time before landing. 9 takes 19 steps:
  9→28→14→7→22→11→34→17→52→26→13→40→20→10→5→16→8→4→2→1
  Every number always gives the same sequence, so you can come back to the ones you like. Some run for hundreds of steps, which is what RESET is for.

• Strumming: Use the bursts on OUT to pluck Karplus-Strong strings.

• Pattern variety: Keep NUMBER fixed and change MODULUS. The same sequence gives quite different drum patterns."""
},

"strings": {
"tagline": "Six guitar strings as V/oct outputs. Pick chords from a button grid, with real fingerings, mutes, bends, capo and slash bass.",
"panelMap": """STRINGS outputs six V/oct signals, one per string of a guitar, playing real chord fingerings. Choose chords from the button grid or by CV. The display shows the chord name and fingering. Bends, a whammy bar, a capo and a slash-bass input let you play it like a guitar.

Selecting chords:
- CHORD: chooses the column of the grid, 1–7.
- ROW: chooses the row, 1–4.
- Chord bank I and II: two gate inputs, each with a button. Together they pick one of four banks. Latching a button inverts its gate, so you choose which bank a high gate selects.
- BUTTONS: press any chord in the grid. The lit button shows the current chord's root, and the chord type is printed to the right of each row.

Changing the pitch:
- CAPO: transposes everything in semitones, -12 to +12. The CV input is V/oct: 1/12V per semitone, 1V per octave. Negative values tune the guitar down.
- PITCH BEND (one per string): bends that string up. The input is rectified, and 10V bends 2 semitones, so an envelope makes a natural bend.
- WHAMMY: the same bend applied to all six strings, on top of PITCH BEND.
- SLASH BASS: a V/oct note here becomes the bass note of the chord. STRINGS frets it on the low E or A string within reach of the chord shape and mutes any strings that would sound below it. If it can't be reached, the low string is retuned, like a drop tuning. Unpatched, chords play in root position.

Outputs:
- V/OCT OUT (6): one per string. Muted strings output -10V so you can use them as logic.
- MUTE (6): a gate is high when that string is muted in the current chord. Use it to silence the matching voice.
- TRIG: a trigger whenever the chord or fingering changes: a button press, or a change to CHORD, ROW, bank or CAPO.
- ROOT: the root note of the chord as V/oct, for a bass or another instrument.
Patch only the leftmost V/OCT or MUTE output and it becomes a 6-channel poly cable.

Context menu:
- Classical Chord Set: swaps the suspended chords for diminished ones (see banks below).
- CHORD input in V/oct: send a note into CHORD and STRINGS finds the nearest chord in the current row, adding a semitone of capo when it needs to.
- Invert Mute Gate Outputs: the MUTE outputs go high when a string plays, so they can open a VCA directly.""",
"basicUse": """1. Pick a chord:
   - Press a button, or set CHORD and ROW. The grid is laid out like this:
     Row 1: B E A D G C F
     Row 2: A D G C F Bb Eb
     Row 3: E A D G C Bb7 Abmaj
     Row 4: A D G C F Bb Eb

2. Pick a bank with the I and II gates or buttons:
   - (0,0) Bank 1: dominant 7th, major, minor, sus2. The everyday chords. Relative majors and minors sit next to each other, so moving between them is easy.
   - (1,0) Bank 2: barre chords (dominant 7th, major and minor barre) and 6ths, plus open B and E major in the top row. The minor row adds Bb7 and Abmaj.
   - (0,1) Bank 3: sus4, major 7th, minor 7th, 7sus4. Major and minor 7ths add tension. Row 3 adds an Ab7.
   - (1,1) Bank 4: add9, augmented, minor 6th, minor 9th. The colorful ones.
   With Classical Chord Set on: Bank 1 swaps sus2 for diminished, Bank 2 swaps 6th for diminished 7th, Bank 3 is 2nd, major 7th, minor 7th, 9th, and Bank 4 is 6th, 7+5, minor 6th, augmented.

3. Handle the mutes:
   - Many fingerings skip strings. Those strings output -10V, and their MUTE gate goes high. Use the gates to silence the matching voices.

4. Bend and slide:
   - Send envelopes to PITCH BEND for single-string bends, or to WHAMMY to bend them all.
   - Use CAPO to move up and down the neck. VCV OCT makes a nice front end for it.

5. Strum:
   - TRIG fires on every chord change. Use it to start a strum, for example through IMPULSE CONTROLLER.

6. Add a bass note:
   - Patch a V/oct note into SLASH BASS for chords like C/G or D/F#.""",
"patching": """• Guitar with TWANG: Patch the leftmost V/OCT output (a 6-channel poly cable) into TWANG's PITCH, and the leftmost MUTE output into TWANG's MUTE CV with its trim fully up. TWANG plays six strings, and every string STRINGS mutes in the fingering is palm-muted on the matching TWANG string. Patch TRIG into TWANG's PLUCK to strum the whole chord on every change.

• Bends: Patch TRIG into ENVELOPE ARRAY and send one envelope to the 5th string's PITCH BEND.

• Neck slide: Patch a decay envelope into CAPO. The capo moves in whole semitones, so it sounds like sliding down the frets.

• Glass slide: Patch a sine LFO at about 6 Hz, unipolar, into WHAMMY. Reset the LFO from TRIG so the vibrato starts with each chord.

• Play from a keyboard: Turn on CHORD input in V/oct, set the CHORD knob all the way down, and patch a keyboard or sequencer into CHORD. Use ROW and the bank gates to choose the chord type. For any root you send, STRINGS finds the nearest guitar fingering and adds capo if it needs to.

• Bass lines under chords: Hold a chord and sequence SLASH BASS to walk the bass note underneath it."""
},
}
