MODULES = {
"dunes": {
"tagline": "Two function generators that rise, fall and wait. With curve shaping, phase gates, and MIN, SUM and MAX of both.",
"panelMap": """DUNES is two function generators, I and II, mirrored on either side of a shared centre. Each one rises, falls, then waits before it can go again, so the rest between shapes is part of the rhythm. The centre combines the two into MIN, SUM and MAX, with a meter to watch them. All inputs are polyphonic.

Each side
- RANGE switch: Slow (0.4 s to 6.8 min), Mid (10 ms to 10 s, the default) or Fast (0.4 ms to 410 ms).
- MODE switch:
  - Slope: a gate starts the cycle and keeps it looping while high. Letting go during the rise cuts straight to the fall.
  - Sustain: a gate rises, holds at the peak while high, and falls when released.
  - Delay: wait first, then rise, then fall. Letting go during the wait cancels it. Holding the gate through the end loops back into the wait.
  A trigger always plays the whole rise, in every mode.
- RISE, FALL, WAIT sliders: the length of each stage, with trim and CV.
- GROW and DECAY sliders: the curve of the rise and the fall, from log through linear to exponential, with trim and CV.
- TRIG: input and button. Fires one full cycle.
- GATE: input and button.
- CYCLE: input and latching button (yellow). Loops continuously.
- Mixer knob (below the meter), with trim and CV: this side's level into OUT, MIN, SUM and MAX.

Centre
- Meter: columns for I, MIN, SUM, MAX and II.

Outputs (bottom row)
- OUT I and OUT II.
- RISE, FALL and WAIT gates for each side, high during that stage.
- MIN, SUM and MAX of the two sides.

Context menu
- Gate Comparator: the threshold for the GATE inputs, in volts.
- Cycle I Jack and Cycle II Jack: Toggle Mode. By default the CYCLE inputs loop only while high; in toggle mode each gate flips looping on or off.""",
"basicUse": """1. Choose a RANGE for each side.
2. Set RISE, FALL and WAIT.
3. Shape the stages with GROW and DECAY.
4. Fire it with TRIG, hold it with GATE, or press CYCLE to loop it.
5. Take OUT, or combine both sides with MIN, SUM and MAX.""",
"patching": """• Envelope: Mode on Sustain, a gate into GATE I, OUT I to a VCA.

• Related pair: Trigger both sides together with different GROW and DECAY. Send MAX to a filter and MIN to a VCA.

• LFOs with rests: CYCLE on, with some WAIT. The pause between shapes becomes part of the rhythm.

• Chains: Patch WAIT I into TRIG II and WAIT II into TRIG I so the two sides take turns.

• Drum triggers: Use the RISE and FALL gates to fire drums or step sequencers in time with the shapes.

• Poly envelopes: A poly gate gives each voice its own cycle."""
},

"crosswinds": {
"tagline": "A sixteen-step gate sequencer where every step can be nudged early or late, or ratcheted.",
"panelMap": """CROSSWINDS is a sixteen-step gate sequencer that works on timing. Each step can be pushed earlier or later than the beat, so the same pattern can swing, drag, rush or fall into polyrhythms. Switch the knobs to ratchet mode and each step can repeat up to nine times instead.

Steps
- 16 knobs in four beats, I to IV: offset each step, from a whole step early to a whole step late. In ratchet mode they set repeats, 1–9.
- 16 step buttons: turn each step on or off.
- KNOB MODE button: switches the knobs between offset and ratchet.
- Display: the displaced gate pattern, with a playback cursor. It dims, but stays editable, while stopped.

Global
- LENGTH slider, with attenuverter and CV: 1–16 steps.
- DEPTH slider, with attenuverter and CV: scales all the offsets together.
- CV MAP: a 16-channel poly input. Channel N controls step N. What it controls is set in the context menu.

Transport
- ON: starts and stops, with a button and input. Each start goes back to the first beat.
- BEAT: the clock input. With nothing patched, the button is a tap tempo. Starts at 120 BPM.
- RESET: back to the first beat, without stopping.

Outputs
- OUT: the displaced gates.
- END: a gate at the end of each loop, or at the end of a one-shot pass.

Context menu
- One-shot mode (vs. loop): plays through once, then stops.
- Gate Width: from a 1 ms trigger up to 99% of a beat.
- MAP CV Destination: Ratchets (default), Offsets or Step Gates.
- Step Gate CV: Toggle mode (vs. Direct Set), for when CV MAP drives the step gates.""",
"basicUse": """1. Patch a clock into BEAT, or tap the button.
2. Turn on the steps you want.
3. Turn the knobs to move steps early or late. Use DEPTH to scale everything at once.
4. Set LENGTH.
5. Press KNOB MODE and turn some knobs up for ratchets.
6. Take OUT to a drum, and END to anything that should happen once per loop.""",
"patching": """• Swing: Leave most offsets at 0 and push the off-beat steps slightly late.

• Displaced rhythm: Move alternate steps in opposite directions for patterns that sit across the beat.

• Ratchet fills: Set CV MAP to Ratchets and send a poly envelope or LFO in, so busy moments ratchet harder.

• Fills on cue: One-shot mode, with a trigger into ON to play the pattern once.

• Song sections: Use END to step a sequencer or trigger a new section every loop.

• Breathing groove: A slow LFO on DEPTH so the displacement drifts in and out."""
},

"drifts": {
"tagline": "Four looping waveforms at clock ratios, mixed into one melodic line. Or run it at audio rate as an oscillator.",
"panelMap": """DRIFTS runs four waveform layers, each looping at its own ratio of the clock, and adds them into one melodic CV. Each layer has its own pitch range, shape and phase, so together they make long, slowly shifting lines that still lock to tempo. It was made as a melody source for MIRAGE. Switch on V/oct mode and it becomes an audio oscillator.

Layers (four rows)
- Button and gate input: turns the layer on or off.
- CYCLES and BEATS: the layer loops CYCLES times every BEATS clock beats. 1:2 is one loop every two beats.
- MIN and MAX: the layer's range, ±48 semitones. The display shows the ratio and range.
- Wave display: the layer's waveform, with a dot for its position.
- WAVE SHAPE slider, with trim and CV: picks one of 16 shapes from the current wave set.
- PHASE slider, with trim and CV: starting offset of the layer.

Global
- WAVE SET knob and CV: morphs between three families of wave shapes, wrapping round.
- SYNC TYPE buttons: RATIO rounds the cycle lengths to whole numbers so the layers stay aligned. OSC. syncs the layers to each other (soft or hard sync, set in the context menu).
- REVERSE: runs the layers backwards, with a button and gate input.
- ON: runs and stops.
- V: V/oct mode. CLOCK then reads pitch instead of tempo.
- RESET: resets every layer.
- OFFSET: shifts the output, ±5V, with CV.
- CV MAP: a poly input that can drive many layer controls at once (see the context menu).
- CLOCK: clock, or pitch in V/oct mode.

Output
- CV RANGE switch: what happens at the edges of the output window. Wrap, Reflect or Clip.
- MIN and MAX: the output window, ±48 semitones.
- MIX OUT: the four layers added together.
- 1–4: each layer on its own.
- POLY: all four as one poly cable.

Context menu
- CV Map: assigns each group of four poly channels (1–4, 5–8, 9–12, 13–16) to a layer control: Phase, Wave Shape, Range Min, Range Max, Ratio Cycles, Ratio Beats or Layer Gate.
- Gate CV Mode: Momentary or Toggle for the layer gates.
- Reverse CV Mode: Momentary or Toggle.
- Oscillator Sync Mode: Soft Sync or Hard Sync.
- Output Modes: what the layer outputs and the poly output carry. Phasor (0–10V), Layer CV (semitone scaled), or Layer CV (bipolar ±5V).
- Oversampling Factor: Off, 2x (default), 4x or 8x, with a Filter Cutoff slider, for audio-rate use.""",
"basicUse": """1. Patch a clock into CLOCK and press ON.
2. Set CYCLES and BEATS for each layer to choose how fast it loops.
3. Set each layer's MIN and MAX range, and the output window.
4. Pick shapes with WAVE SHAPE and the WAVE SET knob.
5. Turn layers on and off to thin or thicken the line.
6. Take MIX OUT into a quantizer, such as MIRAGE.""",
"patching": """• Melody for MIRAGE: MIX OUT into MIRAGE's CV input. Slow ratios give wandering lines that stay in key.

• Four related LFOs: Use the layer outputs on their own, with different ratios.

• Poly modulation: POLY into a poly destination, with Output Modes on Phasor or bipolar.

• Audio oscillator: Turn on V and patch a pitch into CLOCK. Use OSC. sync and different ratios for sync-style timbres, and raise oversampling.

• Play the layers: A gate pattern into the layer gates brings layers in and out in rhythm."""
},

"arcs": {
"tagline": "An 8×8 router that rolls the dice. Each trigger crossfades to a new random set of connections.",
"panelMap": """ARCS routes eight inputs to eight outputs at random. Each trigger picks a new set of connections and crossfades to it. Four sliders set the odds: how many inputs and outputs take part, how much crosstalk there is, and how long the fades last. The display draws every connection as an arc.

Sliders (each with an attenuverter and CV)
- IN: chance that each input takes part. At the top, every patched input plays.
- CROSS: chance of extra arcs between inputs and outputs that aren't paired, for crosstalk.
- FADE: crossfade time, up to 4 seconds. At 0 the routing switches instantly.
- OUT: chance that each output receives a signal.

Jacks
- Inputs 1–8 (left). A poly cable in input 1 spreads across the inputs.
- Outputs 1–8 (right).
- TRIG: input and button. Picks a new routing.
- HOLD: input and button. Freezes the current routing.
- FADE output: an envelope that rises from 0V to 10V across each crossfade.

Context menu
- IN/OUT: guarantee at least 1 active. On by default.
- FADE: Random time in [0, max]. Off by default, so every fade takes the FADE time exactly.
- Hold CV: Latching Toggle. By default HOLD only holds while its gate is high.
- Randomize routing now.
- Reset to identity routing (1→1, 2→2, …).""",
"basicUse": """1. Patch sources into the inputs and destinations from the outputs.
2. Set IN and OUT for how many take part, and CROSS for crosstalk.
3. Set FADE.
4. Send triggers to TRIG for new routings.
5. Hold a routing you like with HOLD.""",
"patching": """• Changing effects sends: Dry sources and effect returns into the inputs; each trigger makes a new mix.

• Slowly morphing textures: Several oscillators or noise voices in, long FADE, occasional triggers.

• Poly spread: A poly source into input 1, scattered across the outputs.

• Events in step: Patch the FADE output into a comparator to fire something when each crossfade finishes.

• Mostly still: Leave HOLD on, and release it now and then for a surprise."""
},

"mirage": {
"tagline": "A chord-aware melody quantizer. Plays the chord tones, then adds passing notes, including just and microtonal ones, as you turn up EXPRESSION.",
"panelMap": """MIRAGE quantizes a melody to the chord that's playing, then expands the chord into a scale. Passing notes are ranked by how well they suit the chord, and EXPRESSION lets them in, most useful first. With the tuning set to Just or Pythagorean, the passing notes can sit between the keys of a piano.

Display
- Keyboard: the chord. Click keys to set it by hand, or patch a chord into CHORD.
- Strip: chord tones (bright) and active passing notes (dimmer), placed on the current tuning grid. The top passing notes are labelled by interval or ratio, like 7/4 or 6/5. They turn grey while GATE is closed.
- Chord name: below the keyboard.

Controls
- ROOT: picks the root. With no chord patched, it picks among the chord tones.
- EXPRESSION: how many passing notes are allowed. At 0 only chord tones.
- MODE: the tuning of the passing notes. 12T (semitones only), JUST (ratios of the harmonic series from the root), PYTH (stacked pure fifths, with wide, tense thirds), 24T (quarter tones).

Inputs
- ROOT: root note as V/oct.
- EXP.: EXPRESSION CV, 0–10V.
- CHORD: poly V/oct chord.
- GATE: high allows passing notes, low allows chord tones only. Unpatched, it's open.
- CV: the melody to quantize.
- TRIG: sample and hold. Each trigger latches every output until the next.
- MODE has CV too, through its jack: 0–2.5V 12-TET, 2.5–5V Just, 5–7.5V Pythagorean, 7.5–10V 24-TET.

Outputs
- LEAD: the quantized melody.
- TENSION: the melody quantized to the full extended scale, ignoring GATE.
- DELTA: TENSION minus LEAD. It reads how hard the scale is holding the melody back.
- BEND: how far LEAD sits from 12-TET, up to a quarter tone. Send LEAD to a normal oscillator and BEND to its fine tune to keep the microtones.
- VEL.: 10V for chord tones, 1–9V for passing notes by rank.
- TRIG: fires whenever a new note is quantized.

The quantizer leans the way the melody is moving, so a rising line snaps up and a falling line snaps down. A sine LFO into CV runs cleanly up and down the scale.

Context menu
- Adaptive tuning: off by default, so microtonal notes are added alongside the chord as flavour notes. Turn it on and they replace the tempered chord tones, so the chord itself retunes toward just intonation as EXPRESSION rises.
- Delta as modulation (x20): scales DELTA up to about ±5V for filters and VCAs. Leave it off when DELTA goes to a pitch input.""",
"basicUse": """1. Set a chord on the keyboard, or patch a poly chord into CHORD.
2. Patch your melody into CV and take LEAD to an oscillator.
3. Start with EXPRESSION at 0 to hear chord tones only, then turn it up to let in passing notes.
4. Choose a MODE. Try JUST and PYTH for notes between the keys, and patch BEND to the oscillator's fine tune.
5. Use a gate to switch passing notes on for some phrases and off for others.""",
"patching": """• Lead over chord changes: WEAVE's POLY or CHORD CASTER's NOTES into CHORD. Sweep EXPRESSION with an envelope to add colour only at the peaks of phrases.

• DRIFTS into MIRAGE: DRIFTS' MIX OUT into CV for wandering lines that always fit the chord.

• Natural phrasing: VEL. into an envelope's level. Chord tones land hard, passing notes are softer.

• A second voice: TENSION into another oscillator for a line that always uses the full scale.

• Tension as modulation: Turn on Delta as modulation and send DELTA to a filter. It opens when the melody pushes against the scale.

• Just chords: MODE on JUST with Adaptive tuning on. As EXPRESSION rises, the chord itself settles into pure intervals."""
},
}
