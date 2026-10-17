MODULES = {
"decima": {
"tagline": "A ten-step gate sequencer you program with buttons. Per-step probability, reversible, with a gate for every step.",
"panelMap": """DECIMA is a ten-step gate sequencer. Click the buttons to set your pattern, click the step lights to jump anywhere, and give each step its own probability. Each step also has its own gate output, which makes it easy to self-patch shorter sequences.

Inputs:
- CLOCK: advances one step. The time between the last two clocks sets the length of the 50% gates.
- DIR: a positive voltage runs the sequence backwards.
- RESET: back to step 1.

Steps (10 rows):
- Button (left): turns the step on or off.
- STEP light: shows the active step. Click it to jump there.
- PROB: probability that an active step fires, 0–100%.
- GATE: 10V for the whole time this step is active, whether or not it fired.

Outputs:
- OUT: a 50% gate for each step that fires.
- INV: a 50% gate for each step that doesn't.

Context menu:
- Active step outputs to Gate output: the step GATE outputs follow OUT for their own step, instead of staying high for the whole step.""",
"basicUse": """1. Click the buttons to choose which steps play.
2. Patch a clock into CLOCK and take OUT to a drum or envelope.
3. Turn down PROB on any step to make it fire only some of the time.
4. Patch INV to a second voice for the off-beats.
5. For a shorter loop, patch a step's GATE output into RESET. Patching step 7 into RESET gives a six-step loop.""",
"patching": """• Hi-hats with life: Turn every step on and set PROB between 50% and 80%. The pattern stays busy but never repeats exactly.

• Call and response: OUT to one drum, INV to another. Every clock goes to exactly one of them.

• Odd lengths: Patch different step GATEs into RESET for 3, 5 or 7-step loops. Switch the RESET cable during a performance to change the meter.

• Ping-pong: Patch the GATE from step 10 into a flip-flop and drive DIR with it, so the sequence turns around at each end."""
},

"morta": {
"tagline": "One knob, sixteen outputs. Every common range, forwards and backwards, plus a voltmeter.",
"panelMap": """MORTA turns one knob into sixteen outputs, each scaled to a different range. Patch a CV into the input and MORTA turns the knob for you, and the display shows the voltage. It's useful for driving many parameters with one gesture, for measuring and rescaling signals, and with its reversed outputs, as a crossfade controller.

Top:
- Big knob: the master control, ±10V.
- Input jack: patch a CV to take over the knob. The knob then animates to follow it. The two small knobs beside it set input gain (±2x) and offset (±10V).
- Display: the current voltage.
- Pass-through output: the knob or input voltage, unchanged.
- POLYPHONY: a poly input switches the whole module to poly. The display shows the first channel.

RANGE knob, attenuverter and CV: sets R, the range of the fourth column, from 0 to 10V.

Outputs, in a 4 × 4 grid. Columns are 1V, 5V, 10V and R. Rows are:
- Unipolar: 0→1, 0→5, 0→10, 0→R
- Bipolar: -1→1, -5→5, -10→10, -R→R
- Reverse bipolar: 1→-1, 5→-5, 10→-10, R→-R
- Reverse unipolar: 1→0, 5→0, 10→0, R→0""",
"basicUse": """1. Turn the big knob, or patch a CV into the input.
2. Patch outputs from whichever rows and columns your destinations need.
3. Set RANGE for the fourth column, or modulate it.
4. Use the reversed rows where one thing should go down while another goes up.""",
"patching": """• Scene control: Map one MORTA across a mix: filters open, reverb rises, a sound fades out, all from one knob.

• Crossfader: Patch a unipolar output and its reversed partner into two VCAs. Turning the knob fades from one to the other.

• Rescaler: Patch a ±5V LFO into the input to get 0–10V, 0–1V or ±R copies of it at once.

• Voltmeter: Patch anything into the input to read its voltage on the display.

• Poly macro: Patch a poly modulation source into the input. Every output becomes a poly cable in its range."""
},

"step-wave": {
"tagline": "An eight-step sequencer that draws a waveform. You shape each step, and move the boundaries between them.",
"panelMap": """STEP WAVE is an eight-step sequencer that outputs a continuous waveform rather than plain steps. Each stage has a VALUE, a SHAPE and a number of BEATS, and you can push the boundaries between stages back and forth with CV. SLEW smooths over any jumps in the result.

The display shows the output in blue. With SLEW at 0, a gray line shows the waveform before slew. Along the bottom is the GATE output with its BEATS.

Timing:
- CLOCK: each clock sets the length of one stage (one grid line on the display). With no clock it runs at 120 BPM. The clock sets the timing only, it doesn't advance the stages, so use RESET to line up with your master clock.
- ON/OFF: starts and stops the sequencer. A gate into the jack pauses it while high. The button inverts what the gate does.
- RESET: back to the start of stage 1. Also has a button.

Stages (8 columns):
- VALUE slider: the stage's level, ±5V. A CV patched into the jack below takes over the slider, and the slider moves to show it.
- RHYTHMIC DISPLACEMENT knobs and jacks: between each pair of stages. They move the boundary earlier or later by up to half a stage (±5).
- SHAPE: morphs through 12 shapes for the stage's curve.
- BEATS: 1–10 gate subdivisions in the stage.
- STAGE buttons and outputs: click to jump to a stage (this also works while stopped). Each output carries a 10V gate for as long as its stage plays.

Global:
- LINK: with LINK on, the SHAPE repeats once per beat across the stage.
- TRACK: with TRACK on, each stage follows its VALUE CV continuously, even at audio rate. With it off, a stage samples its VALUE when it starts.
- SLEW: smooths the output. It's scaled to the stage length.
- CV OUT: the waveform.
- GATE OUT: gates for the BEATS, as drawn at the bottom of the display.

Context menu:
- Stage Value CV Modulates Shape: the VALUE inputs modulate each stage's SHAPE instead of its level.
- Quantize CV Out: rounds CV OUT to semitones.

[[fig:shapes]]""",
"basicUse": """1. Patch a clock into CLOCK, and the same clock (divided) into RESET to keep the sequence lined up.
2. Set a VALUE for each stage.
3. Pick a SHAPE for each stage to decide how it moves from one value to the next.
4. Set BEATS for the rhythm on GATE OUT. Turn on LINK to repeat the shape on every beat.
5. Turn the RHYTHMIC DISPLACEMENT knobs to stretch some stages and squeeze others.
6. Add SLEW to smooth the result.""",
"patching": """• Melody with groove: CV OUT into a V/oct input with Quantize CV Out on, and GATE OUT into an envelope. Displacement swings the notes.

• Wobbly bass: Short CLOCK, LINK on, BEATS of 2 or 4 on some stages. CV OUT into a filter cutoff.

• Drifting groove: Patch slow LFOs into the RHYTHMIC DISPLACEMENT inputs so the boundaries breathe.

• Audio-rate waveform: Clock it fast with TRACK on and patch audio-rate signals into the VALUE inputs. STEP WAVE becomes a drawable oscillator.

• Animated shapes: Turn on Stage Value CV Modulates Shape and patch LFOs into the VALUE inputs to morph the shapes over time."""
,
"figures": [
  {"id": "shapes", "src": "/figures/step-wave/shapes.png", "caption": "SHAPE morphs continuously through 12 shapes. The numbers show the knob positions in between.", "section": "panelMap"}
]
},

"preeeeeeeeeeessed-duck": {
"tagline": "PRESSED DUCK, with sixteen channels. For when six just isn't enough.",
"panelMap": """PREEEEEEEEEEESSED DUCK will satisfy your hunger and craving for more channels. It's PRESSED DUCK with sixteen stereo channels plus the sidechain: 34 audio inputs in 17 channels. Patch a fully loaded 16-voice polyphonic signal into the leftmost channel and duck into it with a SIDE signal.

Everything works the same as PRESSED DUCK:
- SIDE: stereo sidechain that ducks the main mix, with its own level slider and VCA input.
- STEREO INPUTS: 16 stereo channels, compressed together by PRESS. A poly cable in channel 1 spreads across all 16.
- VCA INPUTS / LEVELS: a slider (0 to 2x) and VCA input per channel.
- PAN: per channel.
- MUTES: clickless, with shift-click to solo.
- DUCK, PRESS, FEED and LEVEL, each with an attenuverter and CV.
- L / R outputs.

Context menu: Apply Filters, Muted Sidechain still Ducks, Enable Supersampling, and Mute CVs function as Toggle. See PRESSED DUCK for what each one does.""",
"basicUse": """1. Patch a polyphonic stereo source into channel 1, or up to 16 separate stereo sources.
2. Patch a kick or drum bus into SIDE.
3. Set DUCK for how much the mix gets out of the way, PRESS to glue it, FEED for crunch, and LEVEL for the output.
4. Use the clickless mutes to bring voices in and out.

See PRESSED DUCK for the details.""",
"patching": """• Big poly bus: Patch a 16-voice poly synth into channel 1 and pan each voice with the PAN knobs.

• Master bus: Use it as the main mixer for a whole rack, with the kick on SIDE.

• Staged ducking: Feed a PRESSED DUCK drum mix into SIDE, so the drums duck everything else."""
},

"arrange": {
"tagline": "A seven-channel sequencer you can play into. Record CV, quantize it, or turn it into probability triggers.",
"panelMap": """ARRANGE is a seven-channel step sequencer with up to 128 stages. Each channel can record its input, hold a knob setting, quantize to semitones, or fire probability triggers. Switch between record and playback as you go.

Transport:
- STAGE: selects the stage. Its range follows END.
- END: length of the sequence, up to 16 stages by default (up to 128 in the context menu). Changing it resets to stage 1.
- REC: arms recording, with a button and gate input. The light turns red.
- BACK / FWD: step backwards or forwards, with buttons and inputs.
- RESET: back to stage 1.

Display: the top shows the current stage and the sequence length, with a white dot for progress. The column below shows each channel's output as a voltage, a note, or a probability.

Channels (7 rows):
- IN: overrides the knob. A poly cable into IN spreads downward across the channels.
- MODE button: Voltage (off), V/oct semitones (blue), or Probability triggers (yellow).
- Knob: the stage value, ±10V.
- OUT: the current stage value. In Probability mode, -10V means 0% and +10V means 100%, and the output fires a trigger with that chance each time the stage is reached.

When REC is off, turning a knob changes the output but doesn't write to the sequence. When REC is on, the knob is ignored and the input is recorded into the active stage. Shift-click a knob while recording to apply its value to every stage.

Context menu:
- Set Max Sequence Length: up to 128, 256, 512, 1024 or 2048 stages, handy for quantizing long compositions to 16th notes.
- Stop Record At End: REC turns off when the sequence wraps, so you can record exactly one loop.
- Edit Mode: when on, moving to a stage while recording loads its stored values onto the knobs for editing. When off, the knobs stay where they are, which suits live recording.
- Set Polyphony for Channel 1: OUT 1 carries the channels as one poly cable.
- Copy Stage, Copy All Stages (up to current), Paste (insert after current), Clone Stage to All, Clear Stage, Add Stage (after current), Delete Stage: edit the sequence directly.
- Rotate Sequence to Start Here: the current stage becomes stage 1, and the stages before it wrap around to the end.""",
"basicUse": """1. Set END for the number of stages.
2. Clock FWD to play.
3. Set each channel's MODE: plain voltage, semitones, or probability.
4. To program by hand, step through with FWD and set the knobs with REC on.
5. To record, patch CV into IN, turn on REC and let it play through. Turn on Stop Record At End to capture one loop.""",
"patching": """• Automation lanes: Record slow knob gestures from MORTA or a MIDI controller and loop them.

• Live sampling: Punch REC in and out on a rhythm to catch snapshots of changing modulation.

• Probability drums: Set some channels to Probability mode and patch them to drums. Program a chance for each stage.

• Song structure: Set a long max length, clock FWD with a bar clock, and use the channels to change sections: transposition, mutes, effect sends."""
},

"tri-delay": {
"tagline": "A stereo delay with three taps and a display that shows you what each tap is doing.",
"panelMap": """TRI DELAY is a stereo delay with three taps. Each tap has its own time, feedback and pan, set as offsets from the master knobs. The display shows envelope followers for the dry input (orange) and wet output (blue), plus a dot for each tap: its position is the delay time, its size is the feedback, and its color is the pan (red left, blue right). Gentle tanh saturation with anti-aliasing, and 8x oversampled outputs, keep the feedback from turning harsh.

Master controls (each with an attenuverter and CV):
- DELAY: master delay time, in ms.
- PAN: master pan. There are two delay lines, one per output, and each tap feeds both.
- FEEDBACK: master feedback, 0–100%.
- WET/DRY: mix, 50% by default.

Taps I, II and III: a trimpot for each of DELAY, PAN and FEEDBACK adds to or subtracts from the master. By default the taps are panned left, center and right.

Buffer:
- BUFFER SIZE switch: 36 ms, 360 ms or 3600 ms. Delays up to 3.6 seconds. The same choice is in the context menu under Delay Time.
- CLEAR: empties the buffer, with a button and gate input.
- HOLD: loops what's in the buffer while the button or gate is held.

Jacks:
- IN L / R: a mono signal in L goes to both channels.
- OUT L / R.""",
"basicUse": """1. Patch audio into IN and take OUT L and R.
2. Set DELAY and FEEDBACK with the master knobs.
3. Use the tap trimpots to spread the three taps apart in time, feedback and stereo position.
4. Set WET/DRY.
5. Press HOLD to loop the current buffer, and CLEAR to empty it.""",
"patching": """• Rhythmic echoes: Set the three taps to simple fractions of a beat, like 1/4, 3/8 and 1/2.

• Stereo shimmer: Short buffer, taps panned wide, and a slow LFO on DELAY.

• Freeze: Hold the buffer and modulate PAN and FEEDBACK for an evolving pad from a single phrase.

• Comb tones: The 36 ms buffer with high feedback turns the taps into pitched resonances."""
},
}
