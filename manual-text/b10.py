MODULES = {
"syzygy": {
"tagline": "Two stereo phase-feedback oscillators that cross over: ring mod, AM, cross-FM, folding and noise. From glass bells to metallic chaos.",
"panelMap": """SYZYGY is a complex oscillator made of two stereo phase-feedback oscillators that can ring-modulate, amplitude-modulate and cross-FM each other. It's inspired by chromosomal crossover: the two oscillators recombine, and on the display their product bridges the two centres like a pair of chromosomes. It covers everything from bell and glass-like ring modulation to the metallic clang of linear through-zero cross-FM.

Oscillators I and II (each)
- V/OCT knob and input. A polyphonic V/OCT turns on polyphony for the whole module and every CV input.
- FM knob and input: linear FM, added to V/OCT. The FM inputs are normalled so each oscillator modulates the other; patching a cable breaks the normal. Exponential FM and depth options are in the context menu.
- LOCK: hard-syncs this oscillator to the other one.
- SYNC input: hard-syncs on a rising zero crossing.
- LFO button (oscillator II): LFO mode, where 0V is 1 Hz.

Harmonic palette (sliders for each oscillator, each with an attenuverter and CV)
- FEEDBACK: amount of phase feedback. At zero you get a sine, and POS, NODE and RATIO do nothing.
- POS: where in the cycle the feedback lands, ±360°.
- NODE: number of nodes in the feedback phase. Oscillator I runs 0–5. Oscillator II runs -3.5 to 3.5 with a symmetric pattern, which gives it a different but related sound to OUROS.
- PHASE: the oscillator's base phase, ±360°. After ALIGN, use it to set the two oscillators against each other.
- SPREAD: offsets left and right from PHASE. Your ears hear the two sides at slightly different times, which gives a spatial effect.
- RATIO: frequency of the feedback, 1–10x. Like an FM operator ratio, it sounds best at whole numbers, and the slider is mapped to spend most of its travel near them.

[[fig:node-i]]

[[fig:node-ii]]

Display
- The left (orange) and right (blue) channels of each oscillator, drawn as one cycle in polar form. The cross-modulation product bridges the two centres.
- CHAN: which poly channel to show. Above the poly count, it shows the last one.
- ALIGN: pulses both SYNC inputs at once, realigning the two oscillators.

Mixer (sliders, each with an attenuverter and CV)
- MOD/MIX: from a plain mix of I and II to the cross-modulated sound.
- XFM: cross-FM amount. Which oscillator it modulates is set in the context menu.
- RING/AM: ring modulation to AM. In AM you hear the carrier; in ring modulation only the sidebands. The difference can be subtle, but it's lovely when the oscillators are tuned to an interval.
- SYM: DC offset before the wavefolder.
- FOLD: wavefolding. At the top it turns into saturation.
- PINK/WHITE: noise colour.
- NOISE/CLEAN: from the clean signal to noise.

Outputs
- I OUT and II OUT: stereo outputs for each oscillator.
- MAIN OUT: the stereo mix.
- VOLUME, with attenuverter and CV: a VCA on the outputs.

Context menu
- FM Range: maximum FM depth.
- FM Mode: Linear TZFM or Exponential V/Oct.
- XFM Mode: cross-modulate oscillator I (the usual complex-oscillator routing, and the default), II, or both.
- 2x Supersampling on Ring/AM Mixer: cleaner cross-modulation at more CPU.
- Mix Down Main Outputs: sums the poly outputs to one channel.
- Volume VCA also controls OscI and OscII outs: on by default. Turn it off for full-level I and II outputs.

Technical notes

How does phase-feedback distortion work? The oscillator's phase isn't fixed. A portion of another oscillator's output is fed back to push it around, like the ouroboros eating its own tail. Each cycle the phase lands a little off its ideal position, so the waveform bends and skews. The more feedback, the more distortion.

[[fig:feedback]]

The RATIO mapping: RATIO scales the phase oscillator against the main one, much like an FM ratio, and whole numbers sound best. The slider is mapped through steep 5th-order curves so it still covers the whole range but spends most of its travel near whole numbers.

[[fig:ratio]]""",
"basicUse": """1. Set the pitch:
   - Patch V/oct into oscillator I, II or both.

2. Choose the relationship:
   - Let the oscillators run free, or press LOCK to sync one to the other. Press ALIGN to snap them back into phase.

3. Build the harmonics:
   - FEEDBACK sets how much phase distortion. NODE, POS and RATIO shape it. SPREAD widens it.

4. Mix:
   - MOD/MIX from a plain mix to cross-modulation, RING/AM between the two, and XFM for cross-FM. The FM inputs already cross-modulate until you patch them.

5. Add texture:
   - FOLD for wavefolding, SYM to make it asymmetric, NOISE/CLEAN for noise.

6. Make it a voice:
   - VOLUME is up by default, so SYZYGY works as an oscillator. Set it to 0 and patch an envelope into VOLUME and it becomes a complete polyphonic synth voice.""",
"patching": """• Plucks from a drone: Set up a drone with moderate FEEDBACK and NODE, then send an envelope to FOLD. Each hit gives a short burst of folded harmonics.

• Bells and glass: Tune the oscillators to an interval and morph RING/AM.

• Cross-FM motion: Leave the FM normals in and sweep XFM.

• Wild drums and effects: Set XFM Mode to Both and push XFM for screaming or bubbling sounds. Great for sculpting percussion.

• Stereo snap: Set SPREAD moderately wide and press ALIGN at the start of each phrase.

• Noise layers: Morph in pink or white noise for landscapes or to give drums some grit.

• Poly voice: Poly V/oct into oscillator I, VOLUME at 0, a poly envelope into VOLUME. Route the envelope to FOLD too, for brighter attacks.""",
"figures": [
  {"id": "node-i", "src": "/figures/syzygy/node-i.png", "caption": "Oscillator I: how NODE 0–5 maps the phase feedback onto the oscillator.", "section": "panelMap"},
  {"id": "node-ii", "src": "/figures/syzygy/node-ii.png", "caption": "Oscillator II: a symmetric node pattern from -3.5 to 3.5.", "section": "panelMap"},
  {"id": "feedback", "src": "/figures/syzygy/feedback.png", "caption": "Phase-feedback distortion with RATIO = 2: the feedback oscillator, the distorted oscillator and a reference sine.", "section": "panelMap"},
  {"id": "ratio", "src": "/figures/syzygy/ratio.png", "caption": "The RATIO mapping. Most of the slider's travel sits close to whole numbers.", "section": "panelMap"}
]
},

"super-wonk": {
"tagline": "Sixteen LFOs locked to your clock. Wonk them out of phase, then ALIGN them back together.",
"panelMap": """SUPER WONK is a 16-channel LFO with phase-feedback distortion. It morphs sixteen synchronized oscillators into more chaotic shapes that still stay locked to the clock. Its ALIGN input pulls all sixteen into line and lets them go again.

Clock
- CLOCK: syncs the LFOs to an external clock. Without one they run at 30 BPM.
- RESET: back to the default phases set by NODES. Also has a button.
- RATE X: multiplies the clock with positive values, divides it with negative values, from -24 to +24. Between -1 and 1 it runs at 1x. Has an attenuverter and CV.

Shaping (each with an attenuverter and CV)
- PHASE: a phase offset for all sixteen. Use it for fine timing, or modulate it for much more complex outputs.
- MOD DEPTH: output level, up to 5V.
- WONK: amount of phase feedback. Any WONK makes the oscillators drift slowly out of phase while staying centred on the beat. As WONK rises, the range of NODES narrows and the outputs morph from unison into chaos.
- FDBK POS: which channel the feedback comes from, 1–16. Each gives the wonk a slightly different feel.
- NODES: phase spacing between the channels, -8 to +8.
  - 0: all in unison.
  - 1: evenly spaced, rotating clockwise. Negative values rotate the other way.
  - 2: the phases go round 720°, so each output appears twice.
  - 8: four full rotations, four of each output, in an even/odd pattern.

ALIGN: a gate here (or the button) makes all sixteen fade into alignment, over 2 seconds by default. When the gate goes low they fade back to their NODES positions.

[[fig:align]]

Outputs
- 1–16: the sixteen LFOs. The display shows each one's value.
- P: all sixteen as one poly cable.

Context menu
- Align fade time: up to 16 seconds.
- Output polyphony: each output can carry a group of channels, wrapping back to 1 after 16.
- Unipolar mode (0-10V): outputs 0–10V instead of ±5V. MOD DEPTH and the display follow.""",
"basicUse": """1. Patch a clock into CLOCK.
2. Set RATE X for the speed against the clock.
3. Set NODES to spread the sixteen channels in phase.
4. Raise WONK to let them drift and bend while staying on the beat.
5. Send a gate into ALIGN to pull them together, and release it to let them spread out again.""",
"patching": """• Sixteen-lane mod bus: Patch neighbouring outputs to related parameters (filter cutoffs, pans, wavefolders) for motion that feels connected.

• Phase collapse: Moderate WONK, and a gate into ALIGN every 4 or 8 bars. Everything sweeps into unison and back.

• Rotating wheel: NODES at 1 and a slow RATE X. The sixteen channels turn like a modulation wheel.

• Poly groups: Set Output polyphony so each jack carries a group of channels for poly voices.""",
"figures": [
  {"id": "align", "src": "/figures/super-wonk/align.png", "caption": "ALIGN: on a rising gate the channels fade into alignment; on a falling gate they fade back to their NODES positions. Shown at three WONK settings.", "section": "panelMap"}
]
},

"envelope-city": {
"tagline": "Sixteen related envelopes. Set the first and last, and fourteen more fill in between.",
"panelMap": """ENVELOPE CITY is ENVELOPE ARRAY grown into a city: sixteen envelopes that belong together. Set the width, slant and curve of the first and the last; the fourteen in between fill in. Each channel has its own trigger, button and end-of-cycle gate, so it's built for self-patching, and it can run itself as an oscillator.

FIRST (left) and LAST (right), each with attenuverter and CV
- WIDTH: cycle time of channel 1 (FIRST) or channel 16 (LAST), in seconds.
- SLANT: from a rising ramp, through a pyramid, to a falling ramp.
- CURVE: from log to linear to exponential.
- RETRIG: one button for channels 1–8 and one for 9–16. On, an envelope can be retriggered while it falls. Off, a trigger waits for the envelope to finish.

INTERPOLATED ENVELOPES (centre slider): skews how the in-between channels are distributed between FIRST and LAST.

[[fig:shapes]]

Channels (16)
- INPUTS: a trigger input for each channel. Each is normalled to the next, so one trigger into input 1 fires them all.
- BUTTONS: trigger each channel by hand.
- ENVELOPES: sixteen outputs.
- GATES: go high while their envelope is at 0V. Use them to chain and loop.
- POLY: poly outputs for the envelopes and for the gates.
The display colours match the colours of the cables you patch.

Context menu
- Output Polyphony Settings: how many channels each envelope output and each gate output carries. The groups wrap back to 1 after 16.
- Trigger Probability: a chance for each channel to fire, set per channel (Channels 1–8 and 9–16 submenus) or for all at once.
- Volcano-shaped Envelopes: by default CURVE flips at the peak, giving shark-fin shapes. Volcano mode applies it the same way on both sides.

[[fig:volcano]]""",
"basicUse": """1. Set FIRST and LAST WIDTH. The fourteen in between take the times between them.
2. Shape FIRST and LAST with SLANT and CURVE. Giving the two ends different shapes makes a fan of related envelopes that peak at different times.
3. Patch one trigger into input 1 to fire them all, or separate triggers for separate timing.
4. Patch the GATES back into the inputs to chain and loop.
5. Use RETRIG and Trigger Probability to control how they respond.""",
"patching": """• Velocity fan: Send the sixteen envelopes to sixteen VCAs for a spread from fast to slow across voices.

• Chains: Patch GATE N into input N+1 to build long chains of envelopes without a clock.

• LFOs: With short widths, patch a GATE back into its own input. The envelope cycles on its own.

• Random fills: Turn on Trigger Probability and set some channels to 60–80% for drum patterns that vary from one trigger.

• Mallets: Turn on Volcano-shaped Envelopes for rounded shapes that feel like plucks or mallets.""",
"figures": [
  {"id": "shapes", "src": "/figures/envelope-city/shapes.png", "caption": "Different CURVE and SLANT settings for FIRST and LAST give families of related envelopes that peak at different times.", "section": "panelMap"},
  {"id": "volcano", "src": "/figures/envelope-city/volcano.png", "caption": "Shark-fin envelopes (default, left) and volcano envelopes (right).", "section": "panelMap"}
]
},

"arrange-xl": {
"tagline": "ARRANGE with sixteen channels, built-in editing buttons, and room for whole compositions.",
"panelMap": """ARRANGE XL is a sixteen-channel step sequencer. Each channel can record its input, quantize to semitones, or fire probability triggers, and the copy, paste and edit buttons are right on the panel.

Transport
- STAGE: selects the stage.
- END: sequence length, up to 128 stages (up to 2048 in the context menu). Changing it resets to the start and rescales STAGE.
- REC: arms recording, with a button and input. The light turns red.
- EDIT: with EDIT off, stages are overwritten as you move through them while recording. With EDIT on, each stage's values are loaded onto the knobs so you can change them.
- BACK / FWD: step backwards or forwards, with buttons and inputs. Clock FWD to play.
- RESET: back to stage 1.

Display: the top shows the stage and length, with a white dot for progress. The column shows each channel's voltage, note or probability.

Channels (16)
- IN: overrides the knob. A poly input spreads downward across the channels.
- MODE button: Voltage (off), semitone quantizer (blue), or probability triggers (yellow). In probability mode -10V is 0% and +10V is 100%.
- Knob and OUT.
- P: poly output.

Editing buttons
- COPY: copies the current stage. COPY ALL copies every stage up to the current one. Their lights show the copy buffer is full.
- PASTE: inserts the buffer after the current stage, adding stages as needed.
- CLONE: copies the first copied stage over every stage.
- CLEAR: resets the current stage.
- ADD / DELETE: inserts or removes a stage, changing the length by one.
- Shift-click a knob while recording to apply its value to every stage.

Context menu
- Individual Output Polyphony: how many channels each output carries, wrapping after 16.
- Set Max Sequence Length: 128, 256, 512, 1024 or 2048.
- Stop Record At End: REC turns off when the sequence loops, so you capture exactly one pass.""",
"basicUse": """1. Set END.
2. Clock FWD.
3. Choose a MODE for each channel.
4. Step through with REC on and set the knobs, or patch CV into IN and record as it plays.
5. Use the editing buttons to build longer arrangements from the stages you've made.""",
"patching": """• A whole track: Set some channels to semitones for melody and bass, others to probability for drums, and use the rest for mixer and effect CVs.

• Live recording: Patch a controller into IN with REC on, and turn on Stop Record At End to catch one loop.

• Arranging: Copy a section, paste it after itself, and edit the copies into variations.

• Changing lengths: Use ADD and DELETE while it plays for unexpected changes of length."""
},
}
