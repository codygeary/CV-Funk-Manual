MODULES = {
"chord-caster": {
"tagline": "A whole composition in one module: chord sequencer, rhythm section, six-voice stereo oscillator, modulation, mixer and delay.",
"panelMap": """CHORD CASTER lets you write and sequence complete pieces in VCV Rack. It has a chord quantizer with 192 hand-programmed guitar-style voicings (each of the 16 chord types has its own voicing for every note of the scale), a six-voice stereo oscillator based on OUROS, a rhythm section, a tempo-synced modulation bus, compression and tanh saturation, and a three-tap delay. Every knob can be recorded per stage, so one module can play a whole song.

The panel is laid out in 16 areas, numbered in the two pictures below.

[[fig:overview-a]]

1. Recorder: RECORD turns recording on and off. NOTES, BEATS and KNOBS choose what gets recorded, and the red light means something is recording. When the STAGE moves on, the recorded settings are written to the stage you're leaving.
   - NOTES (red): the chord, root and each voice's NOTE offset. CV SLEW glides the notes between stages.
   - BEATS (green): the beat ratios, STRUM, RETRIG ENV, CLOCK and BEATS.
   - KNOBS (blue): every knob and attenuverter. KNOB SLEW glides them between stages.
   - EDIT: off by default, so stages are overwritten as you move through them. With EDIT on, moving to a stage loads its settings so you can change them, and moving on saves them.

2. Clock: CLOCK sets the tempo in BPM. BEATS sets how many clock pulses each stage lasts (1–99). When a clock is patched into CLOCK TRIG., the knob follows it.

3. Transport: PLAY starts the sequence (blue). Shift-click PLAY to loop the current stage (yellow), which is handy for auditioning. RESET goes back to stage 1; REV and FWD move one stage. Each has an input.

4. Chord sequencer: STAGE picks the current stage and MAX sets how many there are. The display shows stage/max and the chord. Pick the root on the keyboard (the − and + buttons change octave) and the chord type with the 16 buttons: M, m, 7, M7, m7, 6, m6, 9, M9, m9, +9, sus2, sus4, 5, aug, dim. A mono V/OCT input sets the root. A poly V/OCT input replaces the chord, filling the six voices with its notes (copied as needed).

5. Notes: shows the note on each of the six voices, with a scope of each voice's waveform. NOTE − and + move single voices up or down. Changing the root keeps your changes; choosing a new chord type resets them. With a poly V/OCT patched, the chord buttons are disabled and the NOTE offsets still work.

6. Beat programmer: X and 1/Y set a clock ratio for each voice, like a simple SYNCRO without rotation, swing or width. X at 0 silences that voice. The beats are stored per stage, so the rhythm can change with the sequence.

7. Envelopes: like ENVELOPE ARRAY. WIDTH I sets voice 1's envelope length and WIDTH VI voice 6's, with the rest in between. SLANT and CURVE shape them. The beat programmer's gates trigger them, the display shows each one live, and a LEVEL trimpot per voice sets its depth.

[[fig:overview-b]]

8. Modulation: a six-channel modulation bus related to HEX MOD.
   - RATE x: cycles per stage. 1 is one cycle per stage; -2 is one cycle every two stages, down to -16. Between -1 and 1 it stays at 1, a wide landing pad for resyncing while you play.
   - NODES: how the six channels are spread in phase, -3 to +3. 0 is unison; ±1 spaces them 60° apart (positive turns clockwise, negative counterclockwise); ±2 spaces them 120° apart, two copies of three; ±3 spaces them 180° apart, three copies of two opposed pairs.
   - WONK: self-modulation of RATE and NODES, taken from the channel set by POS.
   - MOD. DEPTH: depth for all six channels.
   The bus restarts whenever a new note comes in, so repeated stages of the same chord play as a tie. With WONK past 0.5 the modulators run free.

9. Oscillator: a six-voice stereo OUROS. SPREAD, OFFSET (with FM), FEEDBACK, PHASE, POS, MULTI and NODE work as on OUROS, each with an attenuverter fed by the modulation bus. The circular display shows the top voice in stereo.

10. Mix: STEREO SPREAD pans the six voices from right-to-left through to left-to-right (it also sets the delay tap pans). PRESS compresses and saturates like PRESSED DUCK, with lights for the compression. GAIN sets the level into the delay; above 1 it drives the feedback harder, and its light shows distortion.

11. Delay FX: a small TRI DELAY with smooth fractional delay lines.
   - DELAY: master delay time, up to 36, 360 or 3600 ms depending on BUFFER SIZE.
   - REVERB: feedback. With the 36 ms buffer, high REVERB gives Karplus-Strong plucks.
   - TAPS I, II, III: offsets from DELAY.
   - CENTER: how the feedback is shared between the taps.
   - DRY/WET and VOLUME.
   The scope shows the dry envelope in orange and the wet in blue. The three dots are the taps: position is time, size is feedback, color is pan.

12. STRUM and RETRIG ENV.: STRUM lets the modulation bus trigger the envelopes instead of the beats, for strum patterns that follow the stages. RETRIG ENV. lets envelopes retrigger before they finish.

13. Copy and paste: COPY, PASTE, CLEAR, ADD and DELETE work on the current stage. Shift-click COPY to copy every stage up to the current one. The COPY light is blue for one stage and yellow for several.

14. Slew: CV SLEW and KNOB SLEW glide notes and knobs between stages while playing (not while recording), up to the length of the stage.

15. Inputs: CLOCK TRIG. (tempo from the last two pulses), V/OCT, CHORD, EXT., FEEDBACK, WONK, MOD. DEPTH, PRESS, DRY/WET and VOLUME. Inputs override the panel. EXT. depends on the context menu.

16. Outputs: NOTES, GATES, ENVS and MODS are six-channel poly outputs from their sections. STAGE sends a trigger on each stage change. AUDIO OUT L and R are the stereo mix.

Shift-click any knob while recording KNOBS to apply it to every stage. This works on STRUM and RETRIG ENV. too.

Context menu
- Set Max Sequence Length: the range of MAX, up to 2048. CHORD CASTER always remembers all 2048 stages, so shortening and lengthening again brings back what was there.
- Stop Record At End: stops recording when the sequence loops, so you don't record over the start.
- External Input Mode: what EXT. does.
  - Maps to VCA: replaces the internal oscillator with an external poly signal (channels 1–6 left, 7–12 right).
  - Triggers Envelopes: a poly gate triggers envelopes 1–6 directly.
  - Maps to Modulation: replaces the modulation bus. Fewer than six channels are copied up to six.
  - Maps to V/Oct Offset: adds to each voice's pitch. A mono signal transposes all six, so another sequencer can transpose the whole piece.
- Stage outputs main clock instead of stage clock.
- Sync modulation bus to main clock instead of stage clock.
- Output dry poly audio: AUDIO OUT carries the six dry oscillator voices, and the mixer and delay are switched off.
- Save CPU: on by default. Turn it off for 8x supersampling and smoother envelopes.""",
"basicUse": """1. Choose a chord: click a root on the keyboard and a chord type.
2. Set a rhythm: give each voice a ratio with X and 1/Y.
3. Shape the sound: envelopes with WIDTH, SLANT and CURVE; the oscillator with FEEDBACK, MULTI and NODE.
4. Record a sequence: turn on RECORD with NOTES (and BEATS or KNOBS if you like). Set each chord, then press FWD to move to the next stage.
5. Press PLAY.
6. Add space with the MIX and DELAY FX sections.""",
"patching": """• Play from a keyboard: Set VCV MIDI-CV to 6-note polyphony and send its V/oct and gate through POLY MAP into V/OCT. Chords you play fill all six voices.

[[fig:unison]]

• Several in unison: Run a few CHORD CASTERs from the same CLOCK TRIG. and RESET (VCV PUSH makes a handy sync button), with different OFFSET or SPREAD for a thick stereo stack.

• Your own oscillator: Set EXT. to Maps to VCA and patch a poly oscillator in. You keep CHORD CASTER's rhythm, envelopes, mixer and delay.

• Transposing by sequence: Set EXT. to Maps to V/Oct Offset and patch in a second sequencer.

• Plucked strings: BUFFER SIZE 36, REVERB high, short DELAY. The delay becomes a Karplus-Strong resonator.

• Strummed chords: Turn on STRUM and set NODES to ±1, so the six envelopes fire one after another every stage.""",
"figures": [
  {"id": "overview-a", "src": "/figures/chord-caster/overview-a.png", "caption": "Areas 1–7: recorder, clock, transport, chord sequencer, notes, beat programmer and envelopes.", "section": "panelMap"},
  {"id": "overview-b", "src": "/figures/chord-caster/overview-b.png", "caption": "Areas 8–16: modulation, oscillator, mix, delay, strum and retrig, copy and paste, slew, inputs and outputs.", "section": "panelMap"},
  {"id": "unison", "src": "/figures/chord-caster/unison.png", "caption": "Several CHORD CASTERs in unison, played from a MIDI keyboard through POLY MAP.", "section": "patching"}
]
},

"poly-map": {
"tagline": "Turns a poly MIDI signal into just the notes you're holding, ready for CHORD CASTER.",
"panelMap": """POLY MAP connects polyphonic MIDI to CHORD CASTER. It reads a poly gate to see which notes are held and outputs only those pitches. The output's channel count changes with the number of notes, and CHORD CASTER spreads them across its six voices.

- POLY V/OCT IN: the poly pitches.
- POLY GATE IN: the matching poly gates.
- MAPPED V/OCT OUT: only the held notes. A single note is doubled, so the output always has at least two channels.""",
"basicUse": """1. Set VCV MIDI-CV to 6-note polyphony.
2. Patch its V/oct into POLY V/OCT IN and its gate into POLY GATE IN.
3. Patch MAPPED V/OCT OUT into CHORD CASTER's V/OCT.
4. Play chords. CHORD CASTER fills its six voices from the notes you hold.""",
"patching": """• Live chords: MIDI keyboard into CHORD CASTER through POLY MAP, as above.

• Tidy poly signals: Use POLY MAP before any module that works better with only the active notes, such as a chord quantizer like MIRAGE."""
},

"chordy": {
"tagline": "CHORD CASTER's chord sequencer on its own, with separate outputs for each note and a ROTATE control.",
"panelMap": """CHORDY is the chord-sequencing brain of CHORD CASTER in a smaller module, with a few extras. Separate outputs for all six notes make it easy to patch, and ROTATE gets more variety out of the same chords.

Sequencer (as on CHORD CASTER)
- STAGE and MAX: the current stage and the number of stages. The display shows both and the current chord.
- Keyboard and chord buttons: the root (with octave − and +) and one of 16 chord types.
- NOTE − and + for each voice: move single notes in the voicing.
- Beats per stage − and +: clock pulses per stage.
- RECORD and EDIT: record chord changes into stages, or load them for editing.
- COPY, COPY ALL, PASTE, CLEAR, ADD, DELETE: edit the sequence.
- On/off, RESET, REV and FWD, with inputs. CLOCK input to advance.

Inputs
- NOTE and CHORD: set the root and chord type by CV.
- External transpose: added to every note.
- ROTATE: see below.

ROTATE: turns the six notes around the outputs, by CV or with the trimpot. The red light shows which output has the first note of the chord.

Outputs
- STAGE: a trigger whenever the stage changes.
- MONO: six separate outputs, one per note.
- POLY: the same six notes as one poly cable.

Context menu
- Set Max Sequence Length.
- Stop Record At End.""",
"basicUse": """1. Pick a root on the keyboard and a chord type.
2. Clock it, and record chord changes into stages with RECORD.
3. Take POLY to a poly voice, or the six MONO outputs to six separate voices.
4. Turn ROTATE, or patch CV into it, to move the notes between outputs.""",
"patching": """• Six-voice orchestra: Send each MONO output to a different instrument, so every chord tone gets its own sound.

• Rotating voicings: Clock ROTATE from STAGE or an LFO so the same chords are passed around the voices.

• Chord tones as modulation: Patch the MONO outputs into filter cutoffs or pans for motion that follows the harmony.

• Driving CHORD CASTER: Patch POLY into CHORD CASTER's V/OCT to use CHORDY as an outboard chord source."""
},
}
