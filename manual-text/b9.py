MODULES = {
"twang": {
"tagline": "A polyphonic string you can bow, pluck, or both. With palm mute, tension twang, and a body that runs from a whistle to a cello.",
"panelMap": """TWANG is a physical model of a single string, played with a bow, a pick, or both at once. The string is a waveguide running from nut to bridge, with a stick-slip bow at one point and a pluck at another. At the bridge it's loaded by a modelled body, so string and body work together like a real instrument instead of a string run through a filter. Up to 16 voices; the voice count follows the widest of the PITCH, PLUCK and BOW inputs, so a poly bow cable alone can play chords.

The display shows the first voice's string from nut (left) to bridge (right). The blue line with the bow is where the bow touches; the white line with the pick is where the pluck lands. The trace warms toward amber as you bow harder and add DRIVE.

Left column (knob, trim and CV)
- BOW: bow speed, -1 to +1. Zero lifts the bow; negative bows backwards. The bow takes a moment to get going and coasts to a stop. The CV is polyphonic, so each string can be bowed on its own; a mono cable bows them all.
- MUTE: palm mute. The knob (green light) sets a partial mute; the button (red light) mutes everything fully. Muting darkens the string and shortens its ring together, like a palm on the strings. The CV is polyphonic.
- TWANG: tension bend. A real string goes sharp when it's plucked hard and settles back as it rings. TWANG sets how much of that you hear.

Second column
- PITCH: knob (±2V around C4) and V/oct input, polyphonic. Notes above +2V fold down an octave to keep the bow stable.
- VOL: volume, with CV.
- FM: trim and input. The depth in semitones is set in the context menu.
- PLUCK: a trimmer for maximum pluck velocity (0–10V), a button that plucks every voice, and a trigger input. The trigger's voltage is the velocity, and harder plucks are brighter as well as louder.

Bow row (top sliders, each with trim and CV)
- BOW (blue): how much of the bow's energy reaches the string.
- BOW POS (blue): where the bow touches. Mid-string is round; near the bridge is bright and edgy.
- PRESS (blue): bow pressure. Light is airy and easy to lose; heavy is grippy and crunches at the top. The default sits at a violin-like setting.
- SLIP (blue): how fast the bow lets go once the string slips. Low is a lazy, buzzy scrape; high is crisp and articulate.
- MAT (yellow): body material, wood to metal to glass. Wood thuds, glass sings.
- TONE (red): brightness at the bridge, about 1 kHz to 18 kHz.

Pluck row (bottom sliders, each with trim and CV)
- PICK (white): pluck strength.
- PICK POS (white): where the pluck lands. Near the end is thin and twangy; mid-string is round. Polyphonic CV sets it per voice.
- DECAY (white): how long the open string rings, 0.5 s to 60 s, the same at every pitch.
- HARD (white): finger to pick. Polyphonic CV sets it per voice.
- SIZE (yellow): body size. Up is bigger: from a tiny metallic box (lowest mode around 1.2 kHz), through a guitar (131 Hz, the default), to something so big it's just thud and room (30 Hz).
- DRIVE (red): saturation after the strings, before the body, 1x to 8x.

OUT L / R (top right): stereo. The body is mono, with a subtle stereo width added around it, so it sounds like one instrument and still sums to mono cleanly.

Context menu
- Pluck: String Impedance (how hard the string resists the bow), Material Brightness Tilt (how much MAT brightens the body), Pluck Tilt.
- Body: Bridge Coupling (how much the body loads the string; 0 is a dead bridge).
- Twang: Max Bend (0–24 semitones, default 3), Twang Bounce (how far the pitch rebounds), Bounce Rate. Past 12 semitones the rebound speeds up and rings through several aftershocks.
- Pitch: FM Depth (semitones).
- Output: Poly Out (each voice on its own channel, with its own body, instead of the stereo mix), Stereo Width.
- Pickup Output: OUT L and R both carry one dry pickup on the strings, with no body, drive or stereo widening. It's what a guitar sends down the cable, ready for a fuzz or amp sim such as FUZZY.
- Pickup Position: Neck, Middle or Bridge (the default, and wound a little hotter, like a real guitar).
- Panic: Clear All Energy.""",
"basicUse": """1. Pluck it:
   - Patch a V/oct sequence into PITCH and triggers into PLUCK.
   - Gates are all 10V, so every hit is a full-strength pluck. Turn the velocity trimmer down for a gentler range, or send velocity as the trigger voltage.
   - Shape the attack with PICK POS and HARD, and the ring with DECAY.

2. Bow it:
   - Turn up BOW, or patch an envelope into the BOW CV with the trim open. The bow eases in and coasts out.
   - PRESS and SLIP set the bow's grip; BOW POS sets where it touches. If the note sputters, add pressure or speed. If it crunches, ease off.
   - A pluck lifts the bow for a moment, so you can bow and pluck the same string.

3. Choose the body:
   - SIZE for small and bright up to big and boomy, MAT for how long it rings.
   - TONE darkens the bridge; DRIVE adds grit.

4. Add expression:
   - TWANG makes hard plucks bend sharp and settle. Raise Max Bend for rubbery bends.
   - MUTE for palm-muted chugs.

5. Play chords:
   - A poly PITCH and PLUCK play one string per channel. Turn on Poly Out to pan or process each string.

TWANG sleeps when nothing is bowing or plucking and the strings have rung out.""",
"patching": """• Guitar: Poly PITCH and PLUCK from a chord sequencer, SIZE at its default, MAT low, HARD around 0.5, DECAY around 0.6, a touch of TWANG.

• Palm-muted chug: A gate pattern into MUTE CV and fast triggers into PLUCK. DRIVE up for rock.

• Cello: SIZE high, MAT low, BOW POS around 0.7, and a slow envelope on the BOW CV. Keep TONE fairly dark.

• Strum: Press PLUCK, or send one trigger on a mono cable, to pluck every voice of a held chord.

• Guitar with STRINGS: STRINGS' leftmost V/OCT into PITCH, its leftmost MUTE into the MUTE CV (trim fully up), and its TRIG into PLUCK. You get real guitar fingerings, with the strings each chord leaves out palm-muted.

• Bowed pads: A poly envelope into the BOW CV so each string swells on its own.

• Pluck over bow: Bow a quiet drone and pluck the same string on top.

• Rubber-band bass: Low notes, TWANG at full, Max Bend 12 or more, Twang Bounce around 1.

• Zither: MAT high, SIZE low, HARD high, PICK POS near the end, long DECAY.

• Spatial strings: Turn on Poly Out and patch OUT L into HOTPOT to place each string in the room.

• Fuzz guitar: Turn on Pickup Output, keep the Bridge pickup, and patch OUT L into FUZZY. TWANG is the guitar, FUZZY is the pedal."""
},

"mala": {
"tagline": "A spicy stereo complex oscillator. Grafts harmonics and noise onto the crests of a sine, with a built-in LFO that moves left and right in opposite directions.",
"panelMap": """MALA is a polyphonic stereo complex oscillator named after mala, the numbing-spicy Sichuan flavour. Oscillator A is a shaped sine. Oscillator B is an additive voice with 8 partials and an optional noise layer. HEAT drives A into a waveshaper, and wherever A's crests cross the threshold, B is grafted in. Near A's zero crossings nothing changes. So the crests take on B's harmonics while the fundamental stays solid, even at heavy settings.

The built-in LFO is the MALA bus. MA is its rate and LA its depth. It's applied in opposite directions to the left and right channels, so anything it touches moves across the stereo field.

Displays
- A (top left): the shaped sine, with the graft zones shaded.
- B (bottom left): B's waveform and its ratio to A. A band shows how much noise is in it.
- Scope (right): one cycle of the output, left and right overlaid, with the grafted parts in the heat colour.

HEAT (big knob, trim and CV): graft amount, 0–10. At zero you hear A alone.

Sliders (each with a MAP button above, trim and CV below)
- SHAPE (yellow): A's shape. Centre is a sine; left thins the crests to a point; right saturates toward a rounded square.
- RATIO (blue): B's frequency against A, 1/8x to 16x.
- MORPH (red): B's spectrum, through 20 stops: Sine, Octave, Triangle, Hollow, Square, Reed, Saw (default), Pulse 1/4, Pulse 1/8, Bright, Nasal, Vowel oo, Vowel ah, Vowel ee, Bell, Glass, Comb, Clang, Haze, Noise. The last few add noise.
- SPREAD (green): stretches B's partials from harmonic toward bell-like.
- DETUNE (white): pulls the left and right pitches apart, up to 30 cents (240 with Wide detune). It glides, and glides back into exact unison.
- PHASE (blue): moves B against A, a full cycle across the slider. Changes where B's features land on the crests.

MAP buttons: the seven buttons above HEAT and the sliders send the MALA bus to that control (lit when on). Switching fades, so it never clicks.

Mode buttons
- QUANT: snaps RATIO to 32 simple ratios between 1/8 and 16. Non-integer ratios put formants between harmonics when SYNC is on.
- SYNC (on by default): B restarts with every cycle of A, so RATIO acts like a formant.
- SYM: off grafts B onto both crests the same way (brighter, even harmonics). On makes the graft follow A's sign (hollower, odd symmetry).
SYM waits for A's next zero crossing before it switches, so it never clicks.

MALA bus
- MA: LFO rate, 0.02–50 Hz, with trim and CV.
- LA: LFO depth, with trim and polyphonic CV.

Pitch (left column)
- FM: through-zero linear FM, with a polyphonic input. At full index, 1V moves the pitch by its own frequency, and deep FM can run the oscillators backwards.
- PITCH: knob (±5V around C4) and V/oct input, polyphonic.

Outputs
- MALA, A, B: the LFO and the two raw oscillators, one channel per voice.
- VOL CV (0–10V VCA, polyphonic) and VOL knob.
- OUTS: L and R.

Context menu
- Supersampling: 2x, 4x, 8x, or Auto (default). Auto picks the lowest setting that keeps the current pitch and HEAT clean.
- Polyphonic outputs (default on): L and R carry one channel per voice. Off mixes them down.
- Wide detune (240 cents).
- B brightness: a gentle rolloff on B's partials, 800 Hz to 20 kHz (default 3.5 kHz).
- Texture seed (0–31): changes the noise's waveform, not its spectrum or level.
- Mala wave: Sine (default), Triangle or Slow random.
- Ma CV overrides Mala (depth by La): while the MA CV jack is patched, your CV replaces the internal LFO, scaled by LA.
- Mala voice phase: Spread (default), where each voice's LFO is offset so chords shimmer, or Unison.""",
"basicUse": """1. Start with A:
   - Patch V/oct into PITCH. With HEAT at zero you hear the shaped sine. Move SHAPE to thin or round it.

2. Graft B:
   - Turn up HEAT slowly. B's harmonics bloom on the crests while the fundamental holds.
   - Choose B's spectrum with MORPH and its ratio with RATIO. With SYNC on, sweeping RATIO moves a formant.
   - Press QUANT to lock RATIO to clean intervals. Toggle SYM to hear bright against hollow.

3. Widen it:
   - DETUNE for a chorused split, PHASE to move B on the crests, SPREAD for metal.

4. Animate it:
   - Light one or more MAP buttons and raise LA. MA sets the speed. Even one destination moves in stereo.

5. Play it:
   - The outputs are polyphonic by default, so patch them into a poly VCA or mixer, or use the VOL CV as a built-in VCA.""",
"patching": """• Spicy bass: Low notes, SHAPE a little right, MORPH on Saw, RATIO 2x with QUANT, HEAT around 4. An envelope on HEAT gives a filter-like bite that keeps the fundamental.

• Talking lead: MORPH on the vowels with SYNC on. Sweep MORPH and RATIO for vowel and formant movement.

• Stereo shimmer pad: A poly chord into PITCH, DETUNE up, MAP on PHASE and SPREAD, MA slow, LA moderate.

• Bells and gongs: SPREAD high, MORPH on Bell or Glass, SYNC off, a non-integer RATIO, and a percussive envelope on VOL CV.

• Breathy tone: MORPH toward Haze or Noise with HEAT low. The noise only appears on the crests, so it sounds like breath riding the note.

• Through-zero FM: Patch another oscillator into FM. HEAT adds its harmonics on top of the FM sidebands.

• External bus: Turn on Ma CV overrides Mala and patch a sequencer or envelope into MA. The MAP buttons and the stereo movement now follow your modulation."""
},

"hotpot": {
"tagline": "A spatial mixer for up to 96 sources. Place and move them around the listener, in a shared room, through a tube-warmed bus.",
"panelMap": """HOTPOT is a three-track polyphonic spatial mixer, with controls named after a hot pot dinner. Every input channel is a source placed around a virtual listener. Each source gets real distance and direction cues: level, timing between the ears, head shadow, air absorption, front and back colouring, and Doppler when it moves. All sources share one diffuse room, and the mix runs through a saturating stereo bus. Each track has two poly inputs, so a track holds up to 32 sources and the whole pot up to 96.

The tracks
- STIR (cyan): a ring around the listener, 4 m away at 1x. Position is the angle, ±180°.
- SHABU (chili): a stage 6 m in front, ±12 m left to right.
- FAN (yellow): two tracks, one each side, running from narrow behind you to wide in front. IN A goes to the left track and IN B to the right (if only A is patched, its channels alternate sides). Position runs back to front.

The pot (top centre) is a map seen from above, front at the top. Each source is a dot in its track's colour, sized by its level. SKIM sits in the middle, where the listener is: press it and every source glides home, the light stays on while they settle, and motion starts again from the beginning.

Track strips (one per track)
- ↔ button: motion mode, Parallel (the default) or Mirrored, lit in the track colour when mirrored.
  - Stir: parallel turns everything together; mirrored turns the two halves opposite ways.
  - Shabu: parallel swishes the group side to side; mirrored opens and closes the two halves.
  - Fan: parallel moves both tracks front and back together; mirrored rocks them against each other.
- M button: mute, with a fade. The room tail rings out naturally.
- ANGLE (Stir) or POS slider: home position. Polyphonic CV positions each source.
- SPREAD slider: how far apart the sources sit.
- LEVEL slider: track level, unity at three-quarters. The CV is a 0–10V VCA, normalled to 10V; polyphonic CV sets each source.
- RATE knob: motion speed, 0.01 Hz up to 7 Hz, off at the bottom. The top of the range is fast enough for rotating-speaker effects.
- IN A and IN B (polyphonic).
Moving sources keep their order and spacing, and close up near the end of a track instead of folding back.

Room and scene (knob, trim and CV)
- BROTH: room send, 25% by default.
- MSG: room decay.
- STEAM: diffusion first, then slow modulation of the room above about 20%.
- LID: the room's damping, 1 kHz to 20 kHz.
- POT: scene size, 0.25x to 10x. Scales every distance and the room together.
- SPICE: cue strength, 0–300%. 100% is natural. Above that the cues get more vivid: far sources wetter, near ones drier, ears further apart. The CV covers the full range over 10V.

Main
- M button: main mute.
- SIMMER slider, trim and CV: the lower half is volume; the upper half drives a tube stage (up to +20 dB) for warm, even-harmonic saturation.
- OUTS: L and R.

Headroom is automatic. Each track shares out the level of its active channels, a gentle leveler keeps a full pot under control, and a soft clip catches rare peaks below 10.5V. On load the output fades in over about two seconds. Bypassed, the A inputs go left and the B inputs right.

Context menu
- Motion shape: Sine, Triangle or Stepped (8 steps per cycle with short glides), for each track.
- Haas far-ear delay: how far the far ear lags. Natural (default), Wide, Wider or Widest (60 ms) for an exaggerated stereo spread.
- Doppler: pitch shift from moving sources, kept to a few cents. On by default.
- Full-bandwidth room (more CPU): runs the room at the full sample rate instead of half.""",
"basicUse": """1. Fill the pot:
   - Patch poly voices into a track's IN A. Each channel is a source and appears as a dot.
   - STIR for sounds all around, SHABU for a band in front, FAN for sounds coming from behind.

2. Place them:
   - ANGLE / POS sets where the group sits; SPREAD sets how far apart.
   - LEVEL sets the track level. Patch envelopes into the LEVEL CV for a VCA on each source.

3. Set the room:
   - BROTH sets how much goes into the room; MSG how long it rings.
   - LID darkens it; STEAM thickens it and, higher up, sets it gently moving.
   - POT scales the whole scene from a small room to a hall.

4. Make it move:
   - Turn up RATE on a track. Try both settings of the ↔ button.
   - Pick Sine, Triangle or Stepped motion in the context menu.
   - Press SKIM to bring everything home.

5. Season to taste:
   - SPICE above 100% for a more vivid space, below for something closer to a plain panner.
   - SIMMER past halfway warms the whole mix.

HOTPOT is made for headphones and stereo speakers. Directional cues come across best on headphones.""",
"patching": """• Surround chord: A poly chord into STIR IN A, SPREAD full, RATE slow, ↔ on Mirrored. The notes orbit you, half one way and half the other.

• Band on a stage: Drums into SHABU IN A, bass and keys into SHABU IN B, SPREAD around 0.5, BROTH 20–30%.

• Fly-by: One source on FAN with Triangle motion and RATE moderate. It sweeps from behind to in front, with Doppler and air absorption.

• Notes in their own places: Poly random or sequence CV into STIR's ANGLE CV puts every note of a chord at its own angle.

• Spatial VCA: Poly envelopes into LEVEL CV. Each source is gated on its own while sharing the room.

• Rotating speaker: An organ or pad alone on STIR, SPREAD at zero, RATE near the top (6–7 Hz). It spins around your head like a fast Leslie, with Doppler and head shadow doing the work.

• Hopping sources: Stepped motion on SHABU with RATE low. The sources jump between eight places with short glides.

• Vivid space: SPICE at 200%, POT large, BROTH 40%. Distant sources sink into the room while near ones stay close and dry.

• Warm bus: SIMMER three-quarters up, with a slow LFO on its CV for breathing saturation.

• Spatial strings: TWANG with Poly Out on, into STIR IN A, so each string has its own place."""
},
}
