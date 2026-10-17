MODULES = {
"tatami": {
"tagline": "A stereo polyphonic wavefolder that weaves waveforms into new shapes instead of creasing them.",
"panelMap": """TATAMI is a stereo, polyphonic wavefolder. SHAPE morphs smoothly between folding curves, and antiderivative anti-aliasing keeps the folds smooth, weaving waveforms into new shapes rather than creasing them. Separate DENSITY controls for left and right make stereo images out of a mono source.

Controls (each with an attenuator and CV input):
- SHAPE: the folding curve, 0–3. A saturating tanh at 0, a sine at 1, an exponential sine at 2, and back to tanh at 3.
- COMPRESS: squeezes the input before folding and expands it by the same amount afterwards, so dynamic signals fold evenly.
- SYMMETRY: adds a DC offset to the input before folding, ±5V. Shifts which harmonics come out.
- DENSITY L and R: how many times the signal folds, 1–20, set separately for each side, each with its own CV.

Jacks:
- IN L / R: stereo input, up to 16-channel polyphony.
- OUT L / R.

The display shows the folded output over the input.

Context menu:
- Apply DC Blocking Filter.
- Enable 8x Supersampling: less aliasing at high DENSITY, at more CPU.""",
"basicUse": """1. Patch audio into IN and take OUT L and R.
2. Raise DENSITY for more folds. Set left and right a little apart for width.
3. Sweep SHAPE to choose the folding character.
4. Use SYMMETRY to bring in even harmonics.
5. Add COMPRESS if your input changes level a lot, such as a plucked or enveloped sound.""",
"patching": """• Moving timbre: A slow LFO on SHAPE gives a constantly changing tone.

• Stereo from mono: Patch a mono source into IN L and modulate DENSITY L and R from two different LFOs.

• Folded FM: Fold a sine before using it as an FM modulator, for brighter, more controllable sidebands.

• Envelope-driven folds: Send an envelope to DENSITY so each note starts bright and settles."""
},

"cartesia": {
"tagline": "A 4×4×4 sequencer you can move through in three dimensions, with knob ranges under CV.",
"panelMap": """CARTESIA is a 4×4×4 sequencer: four layers (Z) of 4×4 grids (X and Y). The display shows exactly where you are in the cube, and the 16 knobs and buttons always edit the layer you're looking at. CV over the knobs' range adds a twist: the same pattern can be stretched, squashed or shifted live.

Display and slice panel:
- 3D display: the cube, with the current step lit. The four buttons above select which Z layer the knobs show.
- 16 knobs: the step values for the shown layer. The color shows the layer. Each knob's display shows its note or voltage.
- Buttons by each knob: turn that step's gate on or off.

Moving through the cube (each row has a CV input, a reverse trigger and a forward trigger with button):
- X, Y, Z: step along each axis, or set the position directly with CV.
- SCAN: walks through the current layer in X–Y order.

Ranges:
- MIN and RANGE: the lowest knob value, ±10V, and the span of the knobs, 1–20V. Both have an attenuverter and CV, and the knob displays update as they move.
- QUANTIZE: switches between semitone notes and plain voltages.
- OFFSET: CV added to the final output.

Buttons and inputs:
- ON/OFF: stops and starts the sequencer.
- RESET: back to the first step.
- RANDOM: jumps to a random X, Y, Z position.

Outputs:
- RESET: a trigger whenever the sequencer resets.
- TRIG.: a trigger on every step.
- POLY: 1–4. Sets how many layers come out at once. OUTPUT, GATE and INV become poly cables carrying the selected layer and the ones after it.
- GATE / INV.: the gate and inverted gate for the current step's button.
- OUTPUT: the sequencer value.

Context menu:
- Copy Layer, Paste Layer, Paste to All Layers.
- Sample and Hold Active Step: on by default. OUTPUT only updates on steps whose gate is on, and holds through the steps that are off.
- Enable Triggers from Gate Outputs: GATE and INV send short triggers instead of full-length gates.""",
"basicUse": """1. Pick a layer with the buttons above the knobs, and set the 16 values.
2. Turn on the steps you want with the buttons.
3. Clock X FWD to walk across the layer. Clock Y and Z from slower divisions to move to the next row and layer.
4. Or clock SCAN FWD to step through a layer in order.
5. Set MIN and RANGE, and turn on QUANTIZE for melodies.
6. Turn up POLY to play several layers in parallel.""",
"patching": """• Song sections: Write a different phrase on each layer. Clock X and Y for the melody and advance Z each section.

• Four-voice harmony: Set POLY to 4 and send OUTPUT to a poly oscillator. Each layer is one voice.

• Stretchable patterns: Modulate RANGE slowly. The melody keeps its shape but its intervals grow and shrink.

• Controlled wandering: Trigger RANDOM occasionally between regular clocks to jump to somewhere new in the cube."""
},

"junk-dna": {
"tagline": "A gate sequencer that writes and reads DNA. Type a pattern, and it grows into a 2056-letter gene with variations.",
"panelMap": """JUNK DNA is a gate sequencer that generates and reads DNA. Type a repeat pattern in letter code, and it's copied out to fill a 2056-letter gene. Letters can be fixed bases or wildcards that are filled in at random on every repeat, so you can write anything from short repetitive motifs to whole genes. Each position then fires the gates for the base it holds.

[[fig:codes]]

REPEAT PATTERN: the text box. Use the IUPAC nucleotide codes:
- A, T, C, G: the four bases.
- R (A or G), Y (C or T), S (C or G), W (A or T), K (G or T), M (A or C): a random choice of two.
- B (not A), D (not C), H (not G), V (not T): a random choice of three.
- N: any base.
- X: a strand break. No base, so every gate is off at that position. Use it for rests.
An R has a 50% chance of being A or G. A D has a 33% chance each of being A, G or T.

Moving:
- FWD and REV: step forwards or backwards through the gene, with buttons. It wraps around at the ends.
- RESET: back to position 0. As long as the pattern doesn't change, the gene replays exactly.

Outputs, laid out on the Venn diagram:
- A, T, C, G: high while the current base is that letter.
- R, Y, S, W: high while the current base is either of their two letters.
- B, D, H, V: high while the current base is not their letter.
- N (center): a trigger at every position.
- DNA: a voltage for the current base. A = 0V, T = 1V, C = 2V, G = 3V by default.
- P (bottom right): all twelve gates in one poly cable, in the order A, T, C, G, R, Y, S, W, D, H, V, B.

Gates stay high through repeats, so AAA gives one long gate on A. The same goes for the pattern outputs: CGCGCG keeps S high the whole time.

Context menu:
- Output Pulses instead of Gates: every position sends a short trigger instead of holding the gate.
- The DNA output voltage for each base can be set to your own values.""",
"basicUse": """1. Type a pattern into REPEAT PATTERN, for example CGNNNRX or ATTAGCC.
2. Clock FWD.
3. Patch A, T, C and G to four drum sounds, or use the R, Y, S, W and B, D, H, V outputs for broader patterns.
4. Patch RESET to replay the same gene from the start.""",
"patching": """• Four-piece kit: A to kick, T to snare, C to closed hat, G to open hat. Use fixed letters for the backbone and wildcards to vary the fills.

• Long and short gates: Patterns with runs (AAAA) make long gates; alternating patterns (ATATAT) keep W high. Use the pattern outputs for accents and structure.

• Melodies: Send DNA into a quantizer and set the base voltages to the notes you want.

• Poly gates: Patch P into a poly envelope or poly drum module to get all twelve gates in one cable.""",
"figures": [
  {"id": "codes", "src": "/figures/junk-dna/codes.png", "caption": "The IUPAC nucleotide codes JUNK DNA understands, as listed in its context menu.", "section": "panelMap"}
]
},

"picus": {
"tagline": "A two-voice drum pattern generator. Seven stages of clock ratios with a ten-step DON/KA pattern on top.",
"panelMap": """PICUS is a two-channel trigger burst generator. Program up to seven stages, each with its own clock ratio. A variable-length beat pattern sits over the beats and decides which go to DON (the big drum) and which go to KA (the rim), so a simple interface gives complex rhythms.

Pattern (top row):
- Ten pattern buttons. Each press cycles DON (large white), KA (medium blue) and off (small red). Each beat in a stage plays the next step of the pattern.
- PATTERN LEN.: pattern length, 1–10 steps, with attenuverter and CV.

Stages (seven rows):
- SELECT: jumps to that stage when the current one ends.
- BEATS (− / +): beats to play in the stage. 0 mutes the stage.
- CYCLES (− / +): length of the stage in clock cycles. 0 turns the stage off, so it's skipped.
- The display shows each stage as BEATS:CYCLES. 2:1 plays two beats in one clock cycle; 3:4 plays three beats spread over four cycles.

Transport:
- Mode switch: O (off), I (on), or 1 (one-shot, which switches itself off at the end of the cycle).
- CLOCK: the master clock. It also accepts the CHAIN signal from HAMMER.
- RESET: back to the first stage and the start of the pattern. Also has a button.

Outputs:
- DON and KA: trigger outputs, as programmed by the pattern.
- END: a pulse at the end of each stage, or at the end of the loop (see the context menu).

Context menu:
- END outputs pulse at: each stage end, or the loop end.
- Pattern resets: at each stage end, or only on RESET.""",
"basicUse": """1. Patch a clock into CLOCK, or the CHAIN output of a HAMMER.
2. Set BEATS and CYCLES for each stage you want. Set CYCLES to 0 to skip a stage.
3. Click the pattern buttons to choose DON, KA or off for each step, and set PATTERN LEN.
4. Switch to I to play.
5. Patch DON and KA to two drum sounds.""",
"patching": """• Taiko: DON to a low drum, KA to a rim click. Mix stages like 1:1, 2:1 and 3:2 for rolling rhythms.

• Fills: Make the last stage fast (4:1 or 6:1) for a fill at the end of each loop.

• One-shot phrases: Set the switch to 1 and trigger RESET to play the sequence once.

• Linked to HAMMER: Patch HAMMER's CHAIN into PICUS for sample-accurate timing with your other clocks."""
},

"node": {
"tagline": "A small two-channel stereo mixer and crossfader with clickless mutes and up to 10x gain.",
"panelMap": """NODE is a compact two-channel stereo mixer and crossfader. Each channel has a VCA with up to 10x gain to lift weak signals, gentle tanh saturation at high gain, and clickless mutes.

Channels I and II (each):
- Inputs L and R. Mono and poly inputs are mixed down to one stereo channel.
- GAIN: 0–10x. At high gain the signal saturates gently, with antiderivative anti-aliasing.
- CV: a VCA input for the gain.
- MUTE: clickless mute. Bright red means muted.

Center:
- XFADE: blends between channel I and channel II. The CV input takes -5V to +5V and moves the slider so you can see the mix.
- VOL.: output volume.
- OUT L / R.

Context menu:
- Output poly instead of mix: keeps poly inputs as poly cables at the output.
- Sum poly channels (instead of average).
- Mute Fade Time: 1 ms to 4 seconds, 10 ms by default.""",
"basicUse": """1. Patch two stereo sources into channels I and II.
2. Set GAIN for each. Push it high for warmth.
3. Use XFADE to blend between them, by hand or with CV.
4. Use the MUTE buttons to bring them in and out. Lengthen the fade time in the context menu for slow swells.""",
"patching": """• Crossfade between scenes: Patch two textures in and move XFADE slowly with an LFO.

• CV booster: Turn GAIN up to lift a small modulation signal to full range.

• Dry and driven: Send the same signal into both channels, one with low GAIN and one with high, and use XFADE as a drive control.

• Long fades: Set the mute fade time to a few seconds and use the MUTE buttons as fade-ins and fade-outs."""
},

"weave": {
"tagline": "A six-voice chord quantizer with guitar-like voicings. Weave the voices into new orders as you play.",
"panelMap": """WEAVE is a chord quantizer with voicings that feel like guitar chords. It's built for strumming the six output voices like strings, or spreading them out in space. Each trigger weaves the six voices into a new order, so the same chord keeps moving.

Chord:
- NOTE: root note, as V/oct. The keyboard display shows it, and its − and + buttons move it down or up an octave.
- CHORD: chord type: Oct, M, m, 7, M7, m7, 6, m6, 9, M9, m9, Add9, sus2, sus4, 5, aug, dim. The CV input advances one type per semitone and wraps around (CV skips Oct). The display shows the chord name.
- SHIFT: adds directly to every output to transpose the voicing. Has a CV input.

Weaving:
- WEAVE: picks one of 21 orderings for how the voices move. Has an attenuverter and CV, 1V per pattern.
- TRIG.: moves to the next arrangement. Also has a button.
- RESET: back to the default order. Also has a button.
- Display: the notes on the six outputs. Each line shows the next arrangement that will come with a trigger.

Outputs:
- 1–6: the six voices.
- ROOT: the root note.
- TRIG: a trigger whenever a note changes.
- POLY: all six voices as one poly cable.

Context menu:
- Quantize Shift to semitones.
- Allow input to track multiple octaves: NOTE follows the octave of its input, instead of folding to one octave.""",
"basicUse": """1. Patch a root note into NOTE, or play the keyboard.
2. Choose a chord type with CHORD.
3. Patch outputs 1–6 to six voices, or POLY to one poly voice.
4. Send triggers to TRIG. to weave the voices into new orders. Choose how they move with WEAVE.
5. Use SHIFT to transpose the voicing.""",
"patching": """• Strummed guitar: Send outputs 1–6 to six plucked voices and trigger them one after another, for example from IMPULSE CONTROLLER.

• Moving in space: Pan each output to a different place. Each trigger moves the notes between positions.

• Chord progressions: Sequence NOTE and CHORD from a sequencer, and use TRIG on every beat to keep the voicing alive.

• Chords for MIRAGE: Patch POLY into MIRAGE's chord input to give it a live chord to quantize a melody against."""
},
}
