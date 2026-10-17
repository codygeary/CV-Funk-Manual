MODULES = {
"wonk": {
"tagline": "Six LFOs locked to your clock, with phase-feedback distortion that goes from in sync to wonky without losing the beat.",
"panelMap": """WONK is a six-channel LFO with built-in phase-feedback distortion. It morphs six synchronized oscillators into more chaotic shapes that still stay locked to the clock.

Top:
- CLOCK: syncs the LFOs to an external clock. Without one they run at 30 BPM.
- RESET: resets the oscillators. Also has a button.
- RATE X: multiplies the clock with positive values or divides it with negative values, from -24 to +24. Anything between -1 and 1 runs at 1x. Has an attenuverter and CV.

Shaping (each with an attenuverter and CV):
- WONK: amount of phase feedback. As it rises, the range of NODES narrows and the outputs morph from unison into chaos.
- FDBK POS.: which of the six channels the feedback comes from.
- NODES: phase spacing between the oscillators, -3 to +3.
- MOD DEPTH: output level, 0–5V.

Outputs:
- 1–6: the six LFOs. The display shows each one's current value.
- P: all six as one poly cable.

Context menu:
- Unipolar mode (0-10V): unipolar outputs instead of ±5V.""",
"basicUse": """1. Patch a clock into CLOCK.
2. Set RATE X: 2 for twice the clock, -4 for a quarter.
3. Set NODES to spread the six LFOs out in phase.
4. Raise WONK to bend them away from clean sines. They wander, but stay on the beat.
5. Patch RESET at the start of each bar if you want them to realign.""",
"patching": """• Tempo-locked mod bus: Clock it from your master clock and send the six outputs to filters, pans and VCAs. Everything moves in time.

• Controlled wobble: Push WONK for drift. Reset every bar so it never wanders too far.

• Poly LFO: Patch P into a poly VCA or filter so each voice gets its own related LFO.

• Breathing chaos: Send a slow LFO to WONK so the six channels drift from unison into chaos and back."""
},

"hammer": {
"tagline": "A sample-accurate eight-channel clock. Set ratios with buttons, add swing, and chain it to other HAMMERs and PICUS.",
"panelMap": """HAMMER is a sample-accurate clock with eight channels. Each channel multiplies and divides the master clock to make any beat ratio or polyrhythm. Its CHAIN output carries the clock, on/off and reset to other HAMMER and PICUS modules.

Master clock:
- Display: tempo in BPM.
- RATE: master tempo, up to 480 BPM, with an attenuverter and CV. The CV adds 10 BPM per volt, or tracks V/oct (see the context menu).
- CLOCK input: follow an external clock instead. It also accepts the CHAIN signal from another HAMMER.
- CLK output: the main clock.
- SWING: ±99%. Clock multiples swing along with the master.
- ON/OFF: starts and stops the clock outputs, with a button and gate input.
- RESET: resets the clock dividers, with a button and gate input.

Channels:
- RATIO: each row has − and + buttons on both sides of the display. The left pair sets the multiplier, the right pair the divider. The display shows each ratio; "off" means the channel is silent.
- ROTATE: rotates the ratios across the outputs, with an attenuverter and CV. The ▸ marks where channel 1 is.
- Outputs 1–8: 50% gates at each channel's ratio.

Chaining:
- CHAIN: the internal, unswung master clock plus the ON/OFF and RESET state. Patch it into the CLOCK input of another HAMMER or PICUS. You can have one copy with swing and one without, or one in Phasor Mode.
- POLY: all eight gates in channels 1–8, and their inverted gates in channels 9–16.

Context menu:
- Phasor Mode: outputs 0–10V ramps instead of gates.
- Clock CV as V/oct, or Clock CV is 1V/10BPM.
- Channel Multiply/Divide: sliders for each channel, for typing exact values.""",
"basicUse": """1. Set RATE, or patch a clock into CLOCK.
2. Set each channel's ratio with the − and + buttons. 2:1 is twice the tempo, 1:3 is a third.
3. Patch the outputs to drums and envelopes.
4. Add SWING to taste.
5. Use ROTATE to move the ratios around the outputs.""",
"patching": """• Polyrhythm grid: Set a different ratio on each channel and patch them to percussion for interlocking rhythms.

• Swing and straight: Chain a second HAMMER from the first. Swing one and leave the other straight, both perfectly in time.

• Ramps: Turn on Phasor Mode and use the outputs as eight tempo-locked ramps for filters, panning or wavefolding.

• Drum patterns: Chain into PICUS so its DON and KA patterns follow HAMMER's clock."""
},

"hub": {
"tagline": "Two channels of poly CV processing with a big hands-on knob, a voltmeter and a corn cob display.",
"panelMap": """HUB is a macro controller and CV processing hub. Each of the two channels has gain, offset and a VCA, for poly signals. The display reads out the output voltage, and the big animated knob follows the input; grab it to take over and set the CV by hand. The corn cob display shows the voltage of every poly channel.

Each channel (I and II):
- Input jack, with two small knobs: gain (-2x to +2x, so you can invert or boost) and offset (±10V).
- Big knob: shows the input after gain and offset. Turn it yourself to override the input and set the CV by hand.
- Display: the voltage of the first output channel.
- VCA knob, attenuverter and CV: the output range, 0–10V. Patch CV here to use it as a VCA.
- Output: the result, polyphonic.
- Corn cob: one kernel per poly channel. Large yellow kernels are positive voltages, small white ones negative.""",
"basicUse": """1. Patch CV into a channel's input.
2. Set gain and offset to fit the range you need.
3. Read the result on the display, or watch the corn cob for poly signals.
4. Grab the big knob any time to take over by hand.
5. Patch an envelope into the VCA CV to fade the channel in and out.""",
"patching": """• Range adapter: Turn a 0–10V envelope into ±5V with gain 1 and offset -5V.

• Performance controls: Put HUB at the front of a patch with its outputs on the most important parameters. Let modulation run, and grab the knobs when you want to steer.

• Poly VCA: Patch a poly modulation source in and a single envelope into the VCA CV to fade all voices together.

• Voltmeter: Patch anything in to read its voltage and see its poly channels."""
},

"rat": {
"tagline": "A polyphonic ratio generator for FM. The knob spends most of its travel near the ratios that sound good.",
"panelMap": """RAT is a polyphonic ratio generator for exploring FM. Patch in the pitch of one oscillator and RAT outputs the pitch of a second at a set ratio. The RATIO knob isn't linear: it gives you the most precision around useful, slightly detuned ratios.

Jacks and controls:
- OSC I V/OCT: polyphonic pitch input for the first oscillator. It sets the module's polyphony.
- Display: the current ratio. Normally it shows three decimal places, so you can see the detune. With LOCK on, it shows the ratio as a fraction.
- LOCK: snaps to whole fractional ratios.
- RATIO: ±16. Values above 1 multiply, below -1 divide, and the region from -1 to 1 is 1:1. Has an attenuverter and CV.
- OSC II V/OCT: polyphonic pitch output, scaled by the ratio.

Context menu:
- Ratio Non-Linearity: how strongly the knob favors ratios near whole numbers. LOCK overrides it and outputs the nearest fixed ratio.""",
"basicUse": """1. Patch your carrier's pitch into OSC I V/OCT, and OSC II V/OCT into your modulator.
2. Turn RATIO to choose the relationship. Small moves near a whole number give gentle detuning and slow beating.
3. Press LOCK for exact ratios like 3:2 or 7:4.""",
"patching": """• FM ratio: Run two oscillators from RAT and FM one with the other. Sweep RATIO for classic DX-style timbres.

• Beating pairs: Set RATIO just off 2.000 and mix the two oscillators for slow phasing.

• Poly FM: Patch a poly V/oct in. Every voice gets its modulator at the same ratio.

• Several operators: Chain more RATs from the same input for a stack of ratios."""
},

"count": {
"tagline": "A counter with a big display. Counts up, down, in loops or forever, and outputs gates and a stepped phase.",
"panelMap": """COUNT is a counting module with a large display. Loop, stop at the ends, or count forever. It outputs a gate at the boundaries and a stepped phase voltage.

Display: the current number. The font shrinks to fit as the number grows.

Counting:
- UP, DOWN, RESET: add one, subtract one, or reset. Each has a button and an input.
- LOOP / ∞ / STOP switch: Loop wraps around within MAX VAL. Unbounded (∞) keeps counting without limit, up to a 64-bit integer. Stop holds at the ends of the range.
- RESET POINT switch: reset to zero, the midpoint, or the end.
- MAX VAL: type in any positive number up to 14 digits.

Outputs:
- GATE: goes high at the loop point (Loop) or at the ends (Stop).
- PHASE: 0–10V stepped voltage showing where the count sits relative to MAX VAL. In Unbounded mode it cycles.

Context menu:
- Zero-based counting (start at 0): counts 0–9 instead of 1–10 for a MAX VAL of 10. Useful for linking several counters into a bigger display.""",
"basicUse": """1. Type a MAX VAL.
2. Patch a clock into UP.
3. Pick Loop, Unbounded or Stop.
4. Take GATE as a trigger every MAX VAL counts, and PHASE as a stepped ramp.""",
"patching": """• Clock divider: MAX VAL 16 in Loop mode. GATE fires once every 16 clocks.

• Sequencer address: Patch PHASE into a switch or a sequencer's CV input to step through positions in order.

• Up and down: Patch two different clocks into UP and DOWN. The count drifts in whichever direction is faster.

• Bigger counters: Turn on zero-based counting and patch one COUNT's GATE into the next one's UP to count into the millions.

• Countdown: Set the reset point to End, Stop mode, and clock DOWN. GATE fires when it reaches zero."""
},

"clpy": {
"tagline": "A stereo polyphonic waveshaper that folds small signals and clips big ones toward a voltage you choose.",
"panelMap": """CLPY folds your waves and clips them toward a target voltage. Quiet parts of a signal go through a smooth sine fold. As the level rises past about 4.6V, the output crossfades toward the CLIP voltage instead of a hard rail. Because CLIP is under CV, you can clip to a moving voltage, or even to another audio signal.

Controls:
- IN L / R: stereo input, polyphonic.
- GAIN: input gain, 0–10x, with attenuverter and CV. More gain means more folding and more clipping.
- CLIP: the target voltage, ±5V, with attenuverter.
- CLIP L / R inputs: CV or audio for the clip target on each side. If only one is patched, it's used for both.
- OUT L / R.

Context menu:
- Clipping Mode: Convergent (default) sends both halves of the wave toward CLIP. Symmetric sends the positive half to +CLIP and the negative half to -CLIP, like a classic clipper.
- Supersampling: oversampled processing for less aliasing. The CLIP input is smoothed too, so fast CV and audio into CLIP stay clean.
- Bandlimit Filter: a 6-pole low-pass after the shaper, with a Filter Cutoff slider.""",
"basicUse": """1. Patch audio into IN and take OUT.
2. Raise GAIN until the signal starts folding and clipping.
3. Set CLIP to choose where the clipped parts land. At 0V in Convergent mode, loud parts fold back toward silence.
4. Try Symmetric mode for a more familiar clipper sound.
5. Turn on Supersampling for clean high-gain results.""",
"patching": """• Clip to an envelope: Patch an envelope into CLIP L. Loud parts of the signal follow the envelope shape.

• Clip to audio: Patch a second oscillator into CLIP. The loud parts of the first take on the second, for ring-mod-like timbres.

• Stereo width: Send different LFOs into CLIP L and CLIP R.

• Gentle warmth: GAIN just above 1 and CLIP near 0V adds soft harmonics without obvious clipping."""
},

"cvfunk-blank": {
"tagline": "An 8HP CV funk blank panel.",
"panelMap": "An 8HP blank panel with the CV funk look. It has no controls.",
"basicUse": "Use it to space out your rack.",
"patching": ""
},

"cvfunk-blank4-hp": {
"tagline": "A 4HP CV funk blank panel.",
"panelMap": "A 4HP blank panel with the CV funk look. It has no controls.",
"basicUse": "Use it to space out your rack.",
"patching": ""
},
}
