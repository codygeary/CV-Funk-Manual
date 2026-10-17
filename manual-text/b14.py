MODULES = {
"fuzzy": {
"tagline": "Eight classic fuzz and overdrive pedals simulated from their schematics, with a guitar volume knob for clean-up and a battery that drains until the circuit sputters out.",
"panelMap": """FUZZY is a fuzz pedal with eight circuits inside, each one simulated from the original schematic, transistor by transistor. The input is leveled so whatever you patch in arrives like a hot single-coil pickup, so synths, drums and samples all hit the circuit the way a guitar would.

Display
- The model's name and its circuit: how many transistors, germanium or silicon, and the topology.
- A glyph for each transistor and diode, which glows with the current through it and changes color when it saturates.
- A level meter on the left and a battery icon on the right.

Models
- ROUNDHOUSE: after the Arbiter Fuzz Face (UK, 1966). Two germanium PNP transistors with shunt feedback.
- RASP: after the Sola Sound Tone Bender MK1 (UK, 1965). Three germanium PNPs: a follower and two gain stages.
- SUSTAINER: after the Tone Bender MK2 (UK, 1966). Three germanium PNPs: a boost into a feedback pair.
- SPLUTTER: after the Vox/JEN Tone Bender (Italy, 1966). Two germanium PNPs, with Q2 biased near cutoff.
- BUZZSAW: after the Maestro FZ-1 Fuzz-Tone (US, 1962). Three germanium PNPs on a 3V cell.
- KAIJU: after the Univox Super-Fuzz (Japan, 1968), the scooped octave fuzz. Five silicon NPNs and two germanium diodes.
- HORNET: after the Ibanez Standard Fuzz (Japan, 1970s), a flatter octave fuzz. A JFET, three silicon transistors and a germanium diode.
- KALEIDO: after the Colorsound Power Boost (UK, 1970). Three silicon NPNs, an 18V feedback pair and EQ.
Each model is level-matched, so switching between them changes the character, not the loudness.

Controls
- BATT: the battery's charge, 0–100%. Turn it down and the supply sags and the junctions warm up, until the circuit sputters and dies. With trim and CV.
- FUZZ: each circuit's gain or bias pot, mapped over its sweet spot. With trim and CV.
- GUITAR: the guitar's volume knob, in front of the circuit. Rolling it back cleans up the fuzz the way it does on a real guitar, and the taper spreads the clean-up across the whole knob. With trim and CV.
- MODEL: picks the circuit. The CV is 1V per model and wraps around. Changes crossfade and are rate-limited, so CV can't switch models at audio rate.
- VOL: output volume. The CV covers the full range at 10V.
- SWITCH: the footswitch. The button or a trigger at the jack toggles the pedal, and the red light shows it's on. It fades between the circuit and the clean, leveled input.
- IN and OUT: mono. The output has a DC blocker and a soft limiter.

Context menu
- Oversampling: Off (1x), 2x, 4x (the default) or 8x.""",
"basicUse": """1. Patch a sound into IN and take OUT to your mixer.
2. Pick a MODEL. ROUNDHOUSE is a good place to start.
3. Set FUZZ for the amount of grind.
4. Roll GUITAR back to clean it up, and back up for the full fuzz.
5. Turn BATT down for a dying-battery sputter.""",
"patching": """• Guitar rig: TWANG with Pickup Output on (Bridge pickup) into IN. TWANG is the guitar and FUZZY is the pedal.

• Swell into fuzz: An envelope or a slow LFO into GUITAR's CV, so notes bloom from clean into fuzz like a player riding the volume knob.

• Gated sputter: A random LFO on BATT's CV. The pedal chokes and recovers on its own.

• Pedal-board switching: A sequencer's gates into SWITCH to kick the fuzz in on certain bars.

• Model sequencing: A stepped sequence into MODEL CV changes circuits each bar, with crossfades between them.

• Octave fuzz on synths: KAIJU or HORNET on a simple saw or square bass for the octave-up ring."""
},

"vega": {
"tagline": "Bass pedals after a classic 1976 analog bass-pedal synthesizer: two saws into a transistor ladder, with the original presets and a programmable VARIABLE console.",
"panelMap": """VEGA is a bass-pedal synth after a classic 1976 design, simulated from the schematic and service bulletin: two sawtooth oscillators into a transistor ladder filter, contour generators for the filter and the VCA, and the pitch hold that keeps the note sounding after you lift your foot. It's polyphonic up to 16 voices, and each voice gets its own part tolerances.

Top row
- PITCH and GATE inputs: V/oct and gate, mono or poly. A patched GATE plays whatever PITCH holds.
- GRIT: how hard the circuit is driven, 1/4x to 4x around noon, with makeup gain. With trim and CV.
- SNARL: in the bottom half, osc B's saw swings the cutoff (±4 octaves at half travel). From 0.4 up it crossfades in a sub-octave that also frequency-modulates osc A, and the note growls an octave down. With trim and CV.
- GATE and PITCH outputs: the gate and the held pitch for each voice, so the pedals can play other modules too.

Left column
- TUNE: ±1.5 semitones, both oscillators.
- BEAT: detunes osc B, ±34 cents.
- GLIDE: glide time, 5 ms to 1 s, when the GLIDE switch is on.
Each has a CV jack. TUNE and BEAT CVs add a fifth of the knob's range per volt.

VARIABLE PRESET SETTING
This is the programmable preset, played when VAR is selected. The sliders light up while any voice is on VARIABLE. Each slider has a CV input, worth 10% of its travel per volt.
- OCT: the Variable preset's octave, Lo, Med or Hi.
- B–A: the oscillator mix, all B at the bottom and all A at the top.
- OSC B: osc B's interval, −1 to +13 semitones.
- VOLUME ATTACK, SUS and DECAY: the volume contour.
- CUTOFF: 0–4 octaves above the base cutoff.
- EMPH: emphasis (resonance), 0–10. It self-oscillates from about 8.
- AMT: how much the filter contour moves the cutoff.
- FILTER ATTACK and DECAY: the filter contour.

Presets and switches
- MODE: preset CV, 1V per preset, wrapping every 4V. A poly CV gives each voice its own preset.
- VAR, VEGA, TUBA, BASS: the presets. VEGA, TUBA and BASS use the values from the original preset switches. VEGA is the default.
- GLIDE: on uses the GLIDE knob's time; off, notes change almost instantly.
- DECAY: on by default. Off gives a fast release.
- OCTAVE: low or high. Switching glides between them.

Bottom
- VOLUME: the volume foot pedal, with trim and CV.
- FILTER: the filter foot pedal, 42.9 Hz to 3 kHz, with trim and CV. The cutoff also tracks the keyboard.
- AUX: an external input into the mixer, ahead of the filter. The button above it chooses Mix (alongside the oscillators) or Filter only, where the oscillators drop out and the VCA stays open, following the VOLUME pedal.
- Pedals: 13 clickable pedals, C to C. Drag across them to slide legato. The mouse plays voice 0.
- OUT: audio.

In release, the held pitch droops 12 cents per second, as on the original.

Context menu
- Oversampling: Off, 2x (the default) or 4x.
- OUT: Polyphonic, a channel per voice (the default), or Summed to mono.
- Voice variation: each voice gets its own part tolerances. On by default.
- V/Oct range: Folded onto the pedals, C1 to C2 (the default), so any pitch lands on the 13 pedals, or Full range.""",
"basicUse": """1. Click the pedals to play. Drag across them for legato.
2. Try the VEGA, TUBA and BASS presets.
3. Pick VAR and shape your own sound with the sliders.
4. Ride the FILTER and VOLUME pedals.
5. For a sequence, patch V/oct into PITCH and gates into GATE.""",
"patching": """• Bass from a sequencer: Patch a sequence into PITCH and GATE. With V/Oct range folded, every note lands on the pedals, an octave from C1 to C2.

• Wah pedal: An envelope or slow LFO into FILTER's CV.

• Poly drones: A poly chord into PITCH and GATE with OUT left polyphonic, then into HOTPOT to spread the voices around the room.

• Preset sequencing: A stepped CV into MODE changes preset each step. With poly CV, each voice can play a different preset.

• Filter an outside sound: Set AUX to Filter only and patch a drum loop or pad into AUX. VEGA becomes a ladder filter, played with the FILTER and VOLUME pedals.

• Growl: SNARL past 0.4 with GRIT up for the sub-octave snarl.

• Pedals as a controller: The GATE and PITCH outputs carry what you play, so the pedals can drive another voice in unison."""
},
}
