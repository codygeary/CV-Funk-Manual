MODULES = {
"tuner": {
"tagline": "Two tuners side by side, each with a waveform display and a V/oct output.",
"panelMap": """TUNER is two independent pitch detectors, each with its own display. Each display shows the note name with its offset in cents, the frequency in Hz, and the waveform, held steady across a set number of cycles.

Each channel:
- IN: audio to measure.
- OFFSET: moves the waveform up or down on the display, ±5V.
- GAIN: scales the waveform on the display, 0–5x.
- WIDTH: how many cycles to show, 1–6.
- V/OCT: the detected pitch as V/oct.
GAIN, OFFSET and WIDTH only change the display, not the measurement.

Context menu:
- Analysis speed: trade response time for CPU.
- Large Hz display (disable waveform): replaces the waveform with a big frequency readout.""",
"basicUse": """1. Patch an oscillator into IN.
2. Read the note and cents offset at the top of the display.
3. Use GAIN, OFFSET and WIDTH to get a clear view of the waveform.
4. Take V/OCT to use the detected pitch elsewhere.""",
"patching": """• Tuning oscillators: Patch an oscillator in and tune it until the cents read zero. Use both channels to tune two oscillators against each other.

• Checking V/oct tracking: Play octaves into an oscillator and watch whether the note stays on pitch.

• Pitch follower: Patch V/OCT into a quantizer or another oscillator to follow the pitch of any sound."""
},

"alloy": {
"tagline": "Strike a ring of tuned delay lines for bells, cymbals and metal. Polyphonic and stereo.",
"panelMap": """ALLOY is a metallic voice built from a ring of Karplus-Strong delay lines. A strike sends a short noise burst into the ring. Each node is tuned slightly differently and panned across the stereo field, and their outputs run through ADAA saturation. The result ranges from tuned bells and plates to cymbals and clangs. Patch audio into IN and the ring becomes a resonator for other sounds.

Pitch:
- PITCH knob and V/oct input: ±4V around C4. A poly V/oct gives each voice its own ring.

Tone (each with an attenuverter and CV):
- SHAPE: how the nodes are tuned. Negative scatters them into a chaotic, cymbal-like cluster; positive spreads them evenly for a clearer metallic shimmer.
- TEMPER: coupling between neighboring nodes. More coupling gives a more blended, sympathetic ring.
- RESONANCE: feedback in the ring, which sets how long it rings.
- OVERDRIVE: saturation after the nodes.

Strike section:
- STRIKE button and input: fires the noise burst.
- IMPULSE: length of the burst.
- NOISE: a little noise fed in continuously while the ring sounds, for sizzle.

Jacks:
- IN: audio into the ring.
- VOLUME, and OUT L / R.

Context menu:
- Set Node Count: 4, 8, 12 (default) or 16 nodes.
- Delay effect mode: drops the pitch range by 4 octaves so the ring becomes long delay lines, for using ALLOY as an effect.""",
"basicUse": """1. Press STRIKE or patch a trigger into it.
2. Set the pitch with PITCH, or play it from a V/oct source.
3. Turn SHAPE to move between cymbal-like chaos and clear metal.
4. Set the ring time with RESONANCE.
5. Add TEMPER for a richer, more blended tone, and OVERDRIVE for grit.""",
"patching": """• Metal percussion: Trigger it from a gate sequencer. SHAPE positive and moderate RESONANCE for bells, SHAPE negative for cymbals and hats.

• Resonator: Patch drums or a plucked sound into IN and tune PITCH to the key of your track.

• Poly bells: Patch poly V/oct and poly gates in for a resonator per note.

• Dense swells: SHAPE fully negative, TEMPER high, RESONANCE moderate, with a little NOISE.

• Metallic delay: Turn on Delay effect mode and feed audio into IN."""
},

"onion": {
"tagline": "Eighteen sliders, eighteen outputs, and a LAYERS knob that turns each output into a poly stack.",
"panelMap": """ONION is a bank of 18 sliders, each with its own output. The LAYERS knob makes every output polyphonic: each one carries its own slider plus the next ones in line, so a single cable can carry a whole stack of values. That's the onion, in layers.

Controls:
- −/+ and + switch: bipolar (−DEPTH to +DEPTH) or unipolar (0 to DEPTH). Switching moves the sliders so the voltages stay the same.
- LAYERS: 1–16 channels on each output. Output N carries sliders N, N+1, N+2 and so on, wrapping around after 18.
- DEPTH knob and CV: the full-scale voltage of the sliders, up to 10V.
- 18 sliders in three rows of six, each with its output in the bar below.""",
"basicUse": """1. Choose bipolar or unipolar, and set DEPTH.
2. Set the sliders.
3. With LAYERS at 1, use the outputs as 18 separate CV sources.
4. Turn LAYERS up to get poly stacks from each output.""",
"patching": """• Chord shapes: Set LAYERS to 4 and use the sliders as pitches. Each output is a different four-note chord made of neighboring sliders.

• Poly voice settings: Set LAYERS to the number of voices in a poly patch and use the sliders as per-voice settings like detune or pan.

• Macro fade: Patch an envelope into DEPTH to scale all 18 outputs together."""
},

"strata": {
"tagline": "A layered pitch sequencer with a drum-pattern heart. Rhythm, pitch, semitone and octave rows that each move at their own pace.",
"panelMap": """STRATA is a step sequencer built in layers. A rhythm generator in the style of PICUS decides when notes happen. A row of eight pitch knobs decides what they are. A semitone row and an octave row add variation on top, each stepping at its own rate. Four complete layers can be stored and switched.

Transport:
- PATTERN LEN.: length of the beat pattern, 1–24, with CV.
- CLOCK and RESET (with a button).
- PLAY MODE: 0 (off), I (on), or 1 (one-shot).

Rhythm (top):
- Pattern lights: up to 24 steps, each DON, KA or off. Click to change them.
- Eight stages, each with − / + button pairs for BEATS and CYCLES, shown as two numbers. A stage plays BEATS beats over CYCLES clocks. 0 cycles skips the stage; 0 beats mutes it.

Pitch:
- STEP / STAGE switch (STAGE, HYBRID, STEP): how the pattern and pitches move. In STAGE mode the pattern advances once per stage; in HYBRID it advances on every beat; in STEP mode every beat also steps the pitch, with DON beats moving through the left four knobs and KA beats through the right four.
- Eight pitch knobs, ±2V, in a left half and a right half, each with an on/off light.

Semitone row:
- Seven knobs, ±12 semitones, each with an on/off light, and its own BEATS and CYCLES.
- FWD / REV switch: forward, ping-pong or reverse.

Octave row:
- Four knobs, ±3 octaves, each with an on/off light, and its own BEATS and CYCLES.
- LT / RT switch: apply the octave to the left half, both halves, or the right half.

Layers:
- Four LAYER buttons, a next-layer button, and a LAYER CV input. Each layer stores its own knobs, beats and switches.
- OFFSET knob and CV: transposes everything, ±2V.

Outputs:
- Display: the note being played.
- INV, GATE and OUT.

Context menu:
- Copy Layer, Paste Layer, Paste to All Layers, and Paste Mode (Knobs + Beats, Knobs Only, Beats Only).
- Layer Advance by CV (1V/layer).""",
"basicUse": """1. Patch a clock into CLOCK and set PLAY MODE to I.
2. Set the beat pattern with the lights along the top, and PATTERN LEN.
3. Set the pitch knobs and switch on the ones you want.
4. Add the semitone and octave rows for variation, and set how often each steps.
5. Patch OUT to a V/oct input and GATE to an envelope.
6. Copy the layer to the other three and vary them. Switch layers by hand or with CV.""",
"patching": """• Evolving melody: Give each layer a different beat ratio and switch layers with LAYER CV at the start of each bar.

• Chromatic runs: Leave the main stages on long notes and run the semitone row faster for passing notes.

• Octave scenes: Run the octave row slowly to move the whole sequence up and down every few bars.

• One-shot phrases: Set PLAY MODE to 1 and trigger RESET to play the sequence once.

• Live variation: Click pattern steps between DON, KA and off while it plays."""
},

"triton": {
"tagline": "A stereo three-band splitter with resonant crossovers, envelope followers and stereo width on any parameter.",
"panelMap": """TRITON splits a stereo signal into low, mid and high bands. Each band has its own level, envelope follower and stereo outputs, and the bands also sum back together. A row of sliders sets the crossovers, and a WIDTH slider can push left and right apart on any of them for wide, moving stereo.

The display shows the filter response for left and right, the crossover points, and each band's envelope.

Inputs:
- IN L / R: audio. A mono signal in L goes to both sides.
- V/OCT: moves the crossovers to follow pitch.

Sliders (each with a trim and CV input below):
- CENTER: where the crossovers sit, tracked by V/OCT.
- SPREAD: distance between the two crossover points.
- GAP: negative overlaps the bands; positive leaves a gap of silence between them.
- SHARP: filter steepness, from 1 to 8 stages.
- RES.: a resonant peak at each crossover.
- DRIVE: tanh saturation before the split.
- WIDTH: offsets left against right on every slider whose button is lit.
The buttons above the first six sliders choose which ones WIDTH affects. Several can be on at once.

Band rows (LOW, MID, HIGH, MIX), each with:
- Level knob, with trim and CV.
- ENVELOPE output, with a light.
- L and R outputs. The MIX row's L and R carry all three bands summed.

Context menu:
- Internal Feedback: adds a feedback loop to the resonance for a stronger, wilder peak. Off by default.
- Scaled Envelopes: on by default, so each envelope output follows its band's level knob.""",
"basicUse": """1. Patch audio into IN L (and IN R for stereo).
2. Set CENTER and SPREAD to place the crossovers. Watch the display.
3. Take the bands from the LOW, MID and HIGH outputs, or the whole mix from MIX.
4. Use the level knobs to rebalance the bands.
5. Light a button and raise WIDTH to spread that parameter across left and right.""",
"patching": """• Multiband effects: Send each band to its own effect and mix them back together.

• Envelope followers: Use the ENVELOPE outputs to drive VCAs, filters or reverb sends elsewhere. The low band makes a good kick follower.

• Wide stereo: Light CENTER and raise WIDTH. Left and right crossovers move apart. Modulate WIDTH for movement.

• Moving notches: Set GAP high and SHARP steep for two deep notches, and sweep CENTER with an LFO.

• Resonant bass: Low CENTER, narrow SPREAD, RES. up, to pull a pitched sub out of a sound. Track it with V/OCT."""
},
}
