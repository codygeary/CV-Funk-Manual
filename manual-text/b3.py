MODULES = {
"magnets": {
"tagline": "A magnetic spin lattice you can play with. 24 outputs read the average spin of each zone.",
"panelMap": """MAGNETS, how do they work? This module runs a small magnetic spin-lattice simulation. Every light is one spin, flipping between up and down. Each spin is pulled toward the way its neighbours point and shaken up by temperature. The 24 outputs report the average spin in each zone of the grid, so you get 24 related, slowly shifting CVs.

Controls (each with an attenuverter and CV input):
- TEMP: temperature. Cold and the lattice freezes into big stable regions. Hot and the spins flip constantly.
- POLARITY: pushes all the spins toward up or down, making them more likely to line up that way as they update.
- RATE: time between simulation updates, 0.15–2 ms. Faster updates use more CPU.
- INTERACT: how strongly each spin follows its neighbours. Low lets the lattice flow; high can trap it in a state.

Jacks:
- TAPE HEAD: sets the spins of the central square, and adds to POLARITY across the whole lattice. Write a signal into the middle and watch it spread.
- RESET: randomizes every spin, weighted by POLARITY. Also has a button.
- Outputs: 24 zones, one jack per zone of the grid.

Context menu:
- Voltage Range ±5V: switches the outputs from ±10V to ±5V.""",
"basicUse": """1. Set RATE. Start in the middle and only push it faster if you need to.
2. Set TEMP. Low freezes the lattice, high fills it with noise. Interesting things happen near the point where it starts to freeze.
3. Set INTERACT. Higher values make larger regions that move together, and can cause sudden phase changes.
4. Use POLARITY to lean the whole lattice one way.
5. Press RESET to scramble it and start again.
6. Patch any of the 24 outputs as CV. Neighbouring outputs move together.""",
"patching": """• Connected motion: Send neighbouring outputs to related parameters, like a filter's cutoff and resonance, or the pans of two voices. They move in a way that feels physically linked.

• Swells: Patch a slow LFO into POLARITY. The whole lattice tips toward positive, then negative, taking all 24 outputs with it.

• Slow drift: Low TEMP, moderate INTERACT and a slow RATE give slow, organic movement.

• New state every bar: Patch a clock division into RESET to snap the lattice into a fresh state on the downbeat.

• Writing into the lattice: Patch an LFO or a sequence into TAPE HEAD. It flips the centre spins, and the change ripples outward through the zones."""
},

"ouros": {
"tagline": "A stereo phase-feedback oscillator, shown on a circular display. Like the ouroboros, it feeds on its own tail.",
"panelMap": """OUROS is a stereo oscillator named after the ouroboros, the snake that eats its own tail. Two oscillators circle each other on a polar display. A second phase oscillator, fed back into the first, bends its waveform. NODE moves the phase relationship between unison, two groups, three groups and back. FEEDBACK sets how hard the snake bites.

Pitch:
- V/OCT knob and input: frequency, across 8 octaves. A polyphonic V/OCT turns on polyphony for the module and every CV input.
- FM: exponential FM, added to V/OCT, with an attenuverter.
- SYNC: hard-syncs the oscillator. The button resets it by hand.

Shape (each with an attenuverter and CV input):
- FEEDBACK: amount of phase feedback. At zero you get a clean sine, and POS, NODE and MULTIPLY do nothing.
- MULTIPLY: frequency of the feedback oscillator, 1–10x. Like an FM operator ratio, it sounds best at whole numbers, so the knob is mapped to spend most of its travel near them.
- POS: where in the cycle the feedback lands, ±360°.
- NODE: number of repeating nodes in the feedback phase, 0–5.

Stereo (each with an attenuverter and CV input):
- PHASE: turns both outputs around the phase circle together, ±360°.
- SPREAD: phase difference between left and right, ±360°.

Outputs:
- OUTS: left (orange on the display) and right (blue).

Context menu:
- Presets: factory presets in three groups. See below.""",
"basicUse": """1. Set the pitch with V/OCT. Everything starts as a sine.

2. Add FEEDBACK. The waveform bends and picks up harmonics as you turn it up.

3. Shape it:
   - MULTIPLY picks the harmonic the feedback works on. Stay near whole numbers for in-tune, metallic tones.
   - NODE and POS change where and how often the feedback lands in each cycle.

4. Widen it:
   - SPREAD separates the left and right phases for stereo width and movement. PHASE turns both together.
   - The display draws the two outputs in polar form, so you can see what each change does.

5. Load a preset:
   - Right-click › Presets for classic waveforms, instruments and shapes. Use SYNC or its button to realign the phases after loading.""",
"patching": """• Classic waveforms: The default is a sine. The presets also give rounded saw, square and triangle. They're built additively, so they lack the very top harmonics, but they sound nice unfiltered.

• Instruments: Presets approximate piano, electric piano, violin, saxophone, flute, marimba and glass harp. Whole-number MULTIPLY values keep them harmonic.

• Shapes: The shape presets (Aardvark, Bunny, Butterfly, Rubber Ducky and more) all use whole-number MULTIPLY with SPREAD at zero. Nudge them slightly off for animated timbres and stereo movement.

[[fig:presets]]

• Stereo animation: Modulate SPREAD slowly and run the output through a chorus or delay.

• Metallic tones: Whole-number MULTIPLY with moderate FEEDBACK gives bright, bell-like partials.

• Controlled chaos: Patch an LFO into NODE or POS, and keep FEEDBACK below where it runs away.""",
"technical": True,
"extra": """Technical notes

How does phase-feedback distortion work? The oscillator's phase isn't fixed. A portion of another oscillator's output is fed back to push its phase around. Like the ouroboros, it feeds on itself. Each cycle the phase is shifted a little off its ideal position, so the waveform bends and skews. The result is a sine-like signal whose harmonics and shape depend on the feedback depth: the more feedback, the more distortion.

[[fig:feedback]]

Why the MULTIPLY knob feels sticky: MULTIPLY scales the phase oscillator against the main one, much like an FM operator ratio, and it sounds best at whole-number ratios. The knob is mapped through a set of steep 5th-order curves, so it still covers the whole range but spends most of its travel close to whole numbers.

[[fig:multiply]]""",
"figures": [
  {"id": "presets", "src": "/figures/ouros/presets.png", "caption": "The factory presets: classic waveforms, instruments and shapes.", "section": "patching"},
  {"id": "feedback", "src": "/figures/ouros/feedback.png", "caption": "Phase-feedback distortion with MULTIPLY = 2. Left: the feedback oscillator, the distorted oscillator and a reference sine. Right: the distorted outputs overlaid on the sine.", "section": "panelMap"},
  {"id": "multiply", "src": "/figures/ouros/multiply.png", "caption": "The MULTIPLY knob's mapping. Each step is a steep curve, so most of the knob's travel sits close to a whole number.", "section": "panelMap"}
]
},

"pressed-duck": {
"tagline": "A crunchy six-channel stereo mixer with sidechain ducking, compression and saturation.",
"panelMap": """PRESSED DUCK compresses and ducks your sound into a deliciously crunchy mix. Six stereo channels are compressed together, and a stereo sidechain channel can duck all of them, which is great for pumping bass lines. Everything is under CV, and the saturation uses antiderivative anti-aliasing for a cleaner mix at low CPU.

Channels:
- SIDE: stereo sidechain input. It ducks the six main channels and sits in the centre of the mix. It isn't compressed.
- STEREO INPUTS: six stereo channels. A poly cable in channel 1 spreads across the six channels.
- LEVELS: sliders for input level, 0 to 2x. The middle mark is unity.
- VCA INPUTS: linear VCA CV, multiplied with the slider.
- PAN: one knob and CV per channel. SIDE doesn't pan.
- MUTES: clickless mute buttons with a smooth 5 ms fade. Shift-click a button to solo that channel.

Master (each with an attenuverter and CV):
- DUCK: how far the SIDE signal ducks the main mix.
- PRESS: compression of the main mix. The lights show how much is being applied.
- FEED: extra gain after the compressor, up to 11x, for pushing the saturation into distortion. The lights show how much clipping is happening.
- LEVEL: master level, up to 2x. At 1x the mix saturates at 5V; at 2x, at 10V.
- L / R: stereo outputs.

Context menu:
- Apply Filters: a 30 Hz high-pass on every input removes DC, which keeps the saturation cleaner. On by default.
- Muted Sidechain still Ducks: mute SIDE and it keeps ducking, so you can use a signal you don't want to hear (a kick, say) as the trigger.
- Enable Supersampling: oversamples the output saturation for less aliasing, at more CPU.
- Mute CVs function as Toggle: on by default, so each trigger into a mute input flips the mute. Turn it off and the CV holds the mute while it's high, overriding the button.""",
"basicUse": """1. Patch up to six stereo sources, and a sidechain source into SIDE.
2. Set levels with the sliders. Use PAN to place each channel.
3. Turn up DUCK to make room for the sidechain. You can duck from the SIDE signal itself, or patch an envelope into the DUCK CV.
4. Add PRESS to glue the mix together. Fully compressed, the mix fills the whole range set by LEVEL, with tanh saturation.
5. Add FEED for drive and crunch. At extreme settings it will alias audibly; supersampling helps.
6. Set LEVEL for the output.""",
"patching": """• Plain mixer: Leave PRESS and FEED at zero.

• Sidechain pump: Kick into SIDE, bass and pads into the main channels. Set DUCK to taste. Turn on Muted Sidechain still Ducks and mute SIDE if you want the pump without hearing the kick.

• Chained ducking: Patch one PRESSED DUCK's output into the SIDE of the next. Duck the kick into the snare in the first, then the drum mix into the music in the second. Balance the DUCK levels carefully.

• Performance mutes: Bring channels in and out with the clickless mutes. The compressor keeps the overall level steady as channels come and go.

• Drive bus: Push FEED for tanh saturation across the whole mix."""
},

"flower-patch": {
"tagline": "Turns audio into flowers. A 12-tone polar display with FFT, plus pitch and amplitude outputs for the strongest peaks.",
"panelMap": """FLOWER PATCH draws your audio as a field of flowers. Each column of the display is one note of the 12-tone scale (C to B), and each row is an octave. The signal is drawn in polar form around each flower, with the period set by that flower's note, so each one shows how your audio lines up with that pitch. An FFT measures how much of each note is in the signal, and FLOWER PATCH also sends the strongest peaks out as V/oct.

Controls (each with an attenuverter and CV input):
- HUE: colour of the display. Left gives monotone, desaturated colours; the middle gives white with the FFT peaks in colour; right gives a coloured background with the peaks highlighted.
- FILL: how much the shapes are filled in.
- FLOWER: morphs the shapes from rings into flowers.
- POWER: scales the shapes by the FFT result, positively or negatively, so loud notes grow (or shrink).

Jacks:
- IN: audio input. Left and right are averaged.
- OUT f: V/oct of the six strongest peaks, as a 6-channel poly cable.
- OUT A: the amplitude of each of those peaks, matching channel for channel.

Context menu:
- Flower Mode, Waterfall Mode, Scope Mode: three ways to draw the display.""",
"basicUse": """1. Patch audio into IN.
2. Turn up FLOWER to grow petals, and FILL to fill them in.
3. Use POWER to make the notes in your signal stand out.
4. Pick colours with HUE.
5. Try the Waterfall and Scope views in the context menu.""",
"patching": """• Note watcher: Put FLOWER PATCH on a chord bus to see which notes are sounding.

• Pitch follower: Patch OUT f into a quantizer or oscillator to track the loudest pitches in a sound. Use OUT A as matching VCA levels to resynthesize the strongest partials.

• Light show: Patch slow LFOs into HUE, FILL and FLOWER and let the display move with the music."""
},

"syncro": {
"tagline": "Eight clocks from one, at any ratio. Rotate the ratios, add fills, and bend time with swing.",
"panelMap": """SYNCRO is an eight-channel clock multiplier and divider. Each channel runs at its own fraction of the master clock. ROTATE moves the ratios between channels, FILL adds extra beats, and SWING bends the master clock itself, so every channel stays in step with it. FILL and ROTATE are made for self-patching new rhythms.

Master clock:
- Display: BPM to 0.1 BPM, and swing in %.
- CLOCK: master tempo, up to 480 BPM. The CV input adds 10 BPM per volt at full attenuverter (or tracks V/oct, see the context menu).
- EXT CLOCK: patch a clock here and SYNCRO follows it instead. The tempo comes from the time between the last two pulses.
- ON/OFF: starts and stops the clocks. A gate into the jack flips the button's state.
- RESET: restarts and resyncs every channel. Also has a button.

Shaping (each with an attenuverter and CV input):
- SWING: ±99%. Swing runs over two master clock beats and speeds the clock up and slows it down along a cosine. At 50% the clock swings between 1.5x and 0.5x speed. It's more like rubato than a classic shuffle; for a traditional feel, run the master clock at half tempo and use a x2 channel.
- ROTATE: rotates the ratios across the outputs. The triangle on the display marks where row 1 is.
- WIDTH: gate width, 50% by default. Each output compares a ramp against WIDTH, so with swing on, the gates come out uneven.

Channels (8 rows):
- X: multiply, 0–128. Set it to 0 to silence a row.
- 1/Y: divide, 1–256. The display shows each row's ratio.
- FILL: buttons and gate inputs, one per row. The FILL knob (0–8 beats, shown by the lights, with CV) sets how many beats are added to that row's multiplier at the start of a cycle.
- OUT and INV: a gate and an inverted gate for each row. The top pair is the master clock, which doesn't rotate.

Context menu:
- Phasor Mode: each row outputs a pair of 0–10V ramps instead of gates. WIDTH then sets the phase between the pair (50% by default).
- Clock CV as V/oct: the CLOCK input reads V/oct, with 0V = 120 BPM. The CLOCK knob and attenuverter are disabled, and the display shows a ▸ to tell you.

[[fig:swing]]""",
"basicUse": """1. Set the tempo with CLOCK, or patch a clock into EXT CLOCK.
2. Set a ratio for each row with X and 1/Y.
3. Patch the OUT and INV jacks to drums, sequencers and envelopes.
4. Add FILL to a row with its button or gate input for extra beats.
5. Turn ROTATE to move the ratios between outputs. The X and 1/Y knobs follow the rotation; the FILL inputs stay with their row.
6. Add SWING for a pushed-and-pulled feel.""",
"patching": """• Tap tempo: Patch VCV Push into EXT CLOCK. The button becomes a tap tempo.

• Fills: Set one of the bottom rows to a long division and patch its INV output into a drum row's FILL input. Patch another long division into the FILL CV so the fill size changes too.

• Synth pad: Turn on Clock CV as V/oct and patch a pitch into the CLOCK input. Set the rows to harmonic ratios like 1:1, 2:1, 3:1, 4:1, 6:1, 8:1. Mix the outputs in a mixer that can handle DC, like PRESSED DUCK, and shape the levels with ENVELOPE ARRAY.

• Muting rows by rotation: Set X to 0 on some rows. As ROTATE moves, different rows drop out.

• Swing and phasors: In Phasor Mode, patch the outputs into SIGNALS to watch swing bend the ramps.

[[fig:phasors]]""",
"figures": [
  {"id": "swing", "src": "/figures/syncro/swing.png", "caption": "Swing at 50%. Over two clock beats the clock speeds up to 1.5x and slows to 0.5x along a cosine.", "section": "panelMap"},
  {"id": "phasors", "src": "/figures/syncro/phasors.png", "caption": "Phasor Mode outputs on SIGNALS.", "section": "patching"},
  {"id": "swing-width", "src": "/figures/syncro/swing-width.png", "caption": "With swing on, the ramps bend, so the same WIDTH gives uneven gates.", "section": "patching"}
]
},

"nona": {
"tagline": "Nine channels of gain, offset and mixing for CV. Outputs normal down the module.",
"panelMap": """NONA is a CV utility for scaling, offsetting and mixing signals. Use it to match voltage ranges between modules, make DC voltages, or mix CV.

Each of the nine rows has:
- IN: the signal to process.
- GAIN: -2x to +2x. Negative values invert, and gains over 1 boost weak signals.
- OFFSET: -10V to +10V. With nothing patched into IN, it's a plain DC voltage.
- OUT: the result. Each output also feeds the row below, so unpatched outputs mix down the module. Patching an OUT breaks the chain at that point.

Context menu:
- Row 1 as Master VCA: row 1 becomes a VCA for the other eight. Their outputs are multiplied by row 1's OUT, and a curved line appears on the panel to show it.

[[fig:master-vca]]""",
"basicUse": """1. Patch CV into any input.
2. Use GAIN to scale it (negative inverts) and OFFSET to shift it.
3. Take the output from that row, or leave it unpatched to mix it into the rows below.
4. With nothing patched in, use OFFSET as a DC voltage source.""",
"patching": """• Range matching: Turn a ±10V LFO into 0–5V with GAIN 0.25 and OFFSET 2.5V.

• Mixing: Patch several modulators into rows 1–8 and take the mix from OUT 9.

• Submixes: Patch OUT 3 and OUT 9 to get two separate mixes, rows 1–3 and rows 4–9.

• One knob for everything: Turn on Row 1 as Master VCA and patch an envelope into row 1. All eight other rows follow it.""",
"figures": [
  {"id": "master-vca", "src": "/figures/nona/master-vca.png", "caption": "With Row 1 as Master VCA on, a curved line marks row 1 as the VCA for the rows below.", "section": "panelMap"}
]
},
}
# Ouros technical notes go at the end of the panel map.
_o = MODULES["ouros"]
_o["panelMap"] = _o["panelMap"] + "\n\n" + _o.pop("extra")
_o.pop("technical")
