MODULES = {
"steps": {
"tagline": "A comparator and a stepper in one. Walks a voltage up and down inside a window you set.",
"panelMap": """STEPS pairs a window comparator with a stepper. The stepper adds a fixed STEP to its output every time it's triggered, and the comparator watches whether that voltage has left the window set by BIAS and RANGE. Use it to build fixed-interval scales of any width, count steps, or make rhythms out of the window crossings.

The top half is the comparator. The bottom half is the stepper. With nothing patched into the comparator IN, the two halves are wired together: the stepper's output feeds the comparator, and the comparator's gates push the stepper back into the window when it walks out.

[[fig:normals]]

Comparator:
- IN: the signal to compare. Patching it breaks the normal to the stepper, so the two halves work independently.
- BIAS knob: center of the window, ±5V.
- RANGE knob: size of the window, 0–10V.
- OUT + / OUT −: 10V gates that go high when IN is above or below the window.
- IN, BIAS and RANGE each have a CV jack with an attenuator knob above it.

Stepper:
- STEP: step size, ±1V. Each mark on the knob is 2 semitones. The IN jack below adds to the knob through its attenuator, scaled so ±5V sweeps the whole knob range.
- TRIG.: takes one step. The button above it does the same.
- RESET: jumps back to BIAS (or to 0V when the comparator normal is broken). Also has a button.
- INVERT STEP: a gate here flips the sign of STEP + IN, so the stepper walks the other way.
- OUT (bottom right): the stepper voltage.

Lights: the column shows where the stepper sits in the window, in 10% steps. The larger light flashes on each step or reset.

How the normal works: when the stepper walks out of the window, the comparator gates add ±RANGE back into the next step. The correction lands one step late, which is where a lot of the module's variation comes from.

Context menu:
- Poly Channel Count: Auto follows the widest input, or lock it to 1–16 channels.
- Quantization: snaps the stepper OUT to a grid. Octaves, 12-EDO semitones, 24-EDO quarter-tones, or 9, 17, 19, 22, 31, 41 and 53-EDO.
- Invert Input Mode: Momentary (default) inverts while the INVERT STEP gate is high. Latch flips direction on each gate.""",
"basicUse": """1. Set the window:
   - BIAS places the center, RANGE sets the width.

2. Set the step:
   - Turn STEP to the interval you want. At 1/12V per step you're walking semitones; turn on 12-EDO quantization to keep them exact.

3. Step it:
   - Patch a clock to TRIG. Patch a slower clock to RESET to start the walk over.

4. Read the outputs:
   - The bottom OUT is your stepped CV.
   - The OUT + and OUT − gates fire when the walk crosses the window, which makes them handy clock dividers.

5. Split it in two:
   - Patch something into the comparator IN to use the comparator and stepper as two separate tools.""",
"patching": """• Counting: The ratio of RANGE to STEP sets how many steps fit in the window. With RANGE at 4V and STEP at 1V, a comparator gate fires once every four steps.

• Shifting rhythms: Modulate STEP with an LFO and take the OUT + and OUT − gates as clock divisions. As the step size drifts, the divisions change.

• Melodic walks: Patch the stepper OUT to an oscillator's V/oct. Turn on quantization for in-tune intervals.

• Sequence the phrase, not the notes: Drive BIAS, RANGE and STEP from a slow sequencer. Each stage sets up a new walk, so you're sequencing contour and phrasing instead of single notes.

• Up and down: Patch OUT + into INVERT STEP with Invert Input Mode set to Latch. The stepper climbs to the top of the window and turns around.""",
"figures": [
  {"id": "normals", "src": "/figures/steps/normals.png", "caption": "With the comparator IN unpatched, the stepper and comparator are normalled together: STEP and IN feed the stepper, and the comparator outputs feed back into it.", "section": "panelMap"},
  {"id": "comparator", "src": "/figures/steps/comparator.png", "caption": "The comparator +OUT gate as the stepper crosses the top of the window.", "section": "basicUse"},
  {"id": "walk", "src": "/figures/steps/walk.png", "caption": "STEPPER OUT climbing by STEP on each trigger. When it leaves the window (BIAS ± RANGE), the normalled comparator knocks it back by RANGE one step later.", "section": "basicUse"}
]
},

"envelope-array": {
"tagline": "Six related envelopes from one set of controls. Set the first and last, and the four in between fill in.",
"panelMap": """ENVELOPE ARRAY generates six envelopes that belong together. You set the width of the first and last, and the four in between take evenly spaced widths. SLANT and CURVE shape all six at once. Each channel has its own trigger input and an end-of-cycle gate, so the module is easy to self-patch into LFOs, chains and loops.

Controls:
- FIRST WIDTH: cycle time of channel 1. CV can push it beyond the knob's range.
- LAST WIDTH: cycle time of channel 6. Channels 2–5 sit between FIRST and LAST.
- RANGE buttons: one each for FIRST and LAST. Choose fast, seconds or minutes. The in-between channels bridge the two even if they're set to different ranges.
- SLANT: tilts every envelope between a fast rise and a fast fall.
- CURVE: log to linear to exponential, and beyond to the extremes.
- BUTTON: triggers channel 1 by hand.
SLANT and CURVE also nudge the width a little.

[[fig:shapes]]

Jacks:
- TRIGGER/GATE INPUTS 1–6: trigger inputs. Each is normalled to the one on its right, so a single trigger into 1 fires all six.
- ENVELOPES 1–6: the envelope outputs.
- GATES 1–6: go high while their envelope is at 0V. Use them to chain, loop and reset.
- SLANT, CURVE, FIRST and LAST each have a CV input with an attenuverter.

Context menu:
- Enable Retriggering: by default a channel won't retrigger until it has fallen back to 0V. With this on, it retriggers anywhere in the fall (but still not during the rise).
- Enable Polyphonic Output to Channel 1: ENVELOPES 1 and GATES 1 carry all six channels as one poly cable.""",
"basicUse": """1. Set the widths:
   - Pick a RANGE for each end, then set FIRST and LAST. The middle four fill in between.

2. Shape them:
   - SLANT and CURVE shape all six together. Try the corners of the two knobs first. The figure above shows what's possible.

3. Trigger:
   - One trigger into input 1 fires all six, because the inputs are normalled to the right. Patch separate triggers to break the chain.

4. Use the gates:
   - The GATE outputs mark the end of each envelope. Patch them into other inputs to chain, loop or reset things.

5. Modulate:
   - Every shape and width control has a CV input with an attenuverter.""",
"patching": """• Related modulation: Send the six envelopes to six filter cutoffs or VCAs. They move together but not in lockstep, which keeps a patch alive without sounding random.

• Six LFOs: Patch each channel's GATE back into its own input. Each envelope retriggers itself as it finishes, so you get six free-running LFOs that drift in and out of phase.

[[fig:six-lfos]]

• Chained envelopes: Patch GATE 1 into input 2, GATE 2 into input 3, and so on. Each envelope starts the next. Patch GATE 6 back into input 1 to loop the whole chain. Use the envelope outputs to modulate the module's own controls for patterns that keep changing.

[[fig:chain]]

• Rhythms: Patch the GATE outputs into sequencer resets, and let the envelope widths set the pattern.

• Sub-harmonics: Set both ranges to audio rate. Patch an oscillator into input 1 and set FIRST a little shorter than its wavelength (SIGNALS helps here). Mix all six envelopes and offset the mix by -5V (VCV RSCL works). Each channel can only retrigger at the end of its own cycle, so they lock to the oscillator in overlapping ways and produce rich sub-harmonics.

[[fig:subharmonics]]""",
"figures": [
  {"id": "shapes", "src": "/figures/envelope-array/shapes.png", "caption": "SLANT and CURVE together cover a wide range of envelope shapes.", "section": "panelMap"},
  {"id": "six-lfos", "src": "/figures/envelope-array/six-lfos.png", "caption": "Six LFOs: each GATE patched back into its own input.", "section": "patching"},
  {"id": "chain", "src": "/figures/envelope-array/chain.png", "caption": "Chained envelopes: each GATE triggers the next channel, and GATE 6 loops back to input 1.", "section": "patching"},
  {"id": "subharmonics", "src": "/figures/envelope-array/subharmonics.png", "caption": "Sub-harmonics: an oscillator triggers the array at audio rate, and the six envelopes are mixed and offset.", "section": "patching"}
]
},

"penta-sequencer": {
"tagline": "Five steps, five outputs at once. Each trigger rotates which knob goes to which output, with slew that follows your tempo.",
"panelMap": """PENTA SEQUENCER plays all five of its steps at the same time. Each output A–E carries one of the knobs I–V, and every trigger rotates which knob goes where. Two paths decide the rotation, Circle and Star, and you can run either one clockwise or counterclockwise. SLEW is computed from your trigger timing, so glides stay in time when the tempo changes.

Controls:
- KNOBS I–V: the five step voltages, ±5V.
- SLEW: off at the left. Turned up, each output glides to its next value, timed from the last trigger interval and the size of the jump. CV into the center jack overrides the knob: -5V to +5V, with 0V giving 50% slew.

Inputs:
- TRIG: advances the rotation one step. The button does the same.
- RESET: back to the start (A plays I). Also has a button.
- CIRCLE / STAR: Circle by default (I→II→III→IV→V→I). Hold a gate above 1V for Star (I→III→V→II→IV→I).
- CW / CCW: clockwise by default. Hold a gate above 1V to run counterclockwise. Changing direction swaps the left and right outputs.
- SHIFT: transposes all five steps.

Outputs:
- The five round jacks around the pentagon are outputs A–E. The lights around each one show which knob it's playing, and a light by the knobs marks the one feeding the bottom-most active output.

Context menu:
- Enable Polyphonic Output to Channel A: output A carries all five outputs as one poly cable.""",
"basicUse": """1. Set the steps:
   - Dial in five voltages on I–V.

2. Clock it:
   - Patch a clock into TRIG. Each trigger rotates the knob-to-output mapping, and all five outputs change at once.

3. Change the path:
   - A gate into CIRCLE / STAR switches to Star while it's held.
   - A gate into CW / CCW runs the rotation backwards while it's held.

4. Add slew:
   - Turn up SLEW to glide between steps. Bigger jumps glide faster, so the outputs always arrive by the next trigger.""",
"patching": """• Slewed octaves: Set the knobs to -2, -1, 0, 1, 2 and SLEW to 0.25. Send each output to a wavetable VCO with a slightly different timbre. For melody, run a second PENTA SEQUENCER with slew at 0, quantize it, and patch it into the first one's SHIFT. The octave lanes glide while the notes stay in tune.

• Five LFOs: Clock slowly and set SLEW to 1.0. The slew uses the time between the last two triggers to build its ramps, so you get five slow, related LFOs.

[[fig:slew]]

• Fixed root: Reset so the bottom output plays the step you want as your root. Switch between Circle, Star, CW and CCW as much as you like; the bottom output stays put.

• Five-channel fader: Set knob I to +5V and the rest to 0V. Patch each output to a mixer channel's level and set SLEW to 1. Each slow trigger crossfades to the next channel. Good for moving between soundscapes.

[[fig:fader]]""",
"figures": [
  {"id": "slew", "src": "/figures/penta-sequencer/slew.png", "caption": "SLEW morphs continuously from stepped to sloped CV. Knobs set to I=0V, II=1.25V, III=2.5V, IV=3.75V, V=5V.", "section": "patching"},
  {"id": "fader", "src": "/figures/penta-sequencer/fader.png", "caption": "Five-channel fader: one knob at 5V rotates across the outputs, and SLEW turns each step into a crossfade.", "section": "patching"}
]
},
}
