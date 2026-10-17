MODULES = {
"sirocco": {
"tagline": "A desert in a module. Grass grows, locusts swarm, the wind blows and it rains, and every part of it is a CV output.",
"panelMap": """SIROCCO simulates a small desert ecosystem. Grass grows and spreads its seeds on the wind. Locusts find the grass and multiply, eat it faster than it can recover, and crash. The grass grows back and it starts again. This is the classic predator-prey (Lotka-Volterra) cycle, but it plays out along a strip of 64 patches of ground, so different places are at different stages at the same time. Swarms form, move, strip an area bare and dissolve somewhere else. The outputs never quite repeat.

The display shows the strip: grass in gold, moisture in blue, seeds, and the locust swarm in green, under the night sky.

Weather (knob, attenuverter and CV)
- WIND: how much energy the weather has. Sets how far seeds blow and how strong storms get.
- SQUALL: how changeable the wind is: how often it changes direction, and how often dust storms come.

Ecology (sliders, each with CV)
- BLOOM: how fast grass grows back.
- WILT: drought. Grass dies off on its own, without locusts. This unsettles the cycle and makes it less regular.
- CYCLE (center, ⟳): the master tempo of the whole predator-prey cycle.
- EAT: how fast locusts turn grass into more locusts.
- GROW: how long locusts survive without food.

Events (button and trigger input)
- STORM: a dust storm. A surge of wind that scatters the seeds.
- RAIN: a rainfall. Grass blooms across the strip.
- WADI: switches the strip between a loop (the ends join) and a valley with walls at each end.
- RESET: back to a sparse desert.

Outputs
- GRASS: total grass, 0–10V.
- SEED: a 1 ms trigger each time grass seeds itself.
- POLY: grass density along the strip, in 16 channels, 0–10V.
- WIND: wind speed and direction, ±5V.
- RAIN: rain and storm intensity, 0–10V.
- POP.: locust population, 0–10V.
- SWARM: where the swarm is along the strip, 0–10V.

Context menu
- Seed Timing: Seed maturation rate, and the Re-seed die-back threshold.
- RAIN Output Mode: Intensity (default), Rain gate, or Dust storm gate.""",
"basicUse": """1. Let it run. At the default settings the ecosystem organizes itself. Watch the grass grow, the swarms bloom and the rain fall.
2. Change the weather with WIND and SQUALL, or press RAIN and STORM.
3. Change the life cycle: BLOOM for how quickly grass recovers, EAT and GROW for how locusts boom and bust, WILT for drought, CYCLE for the overall speed.
4. Press WADI to switch between a looped strip and a walled valley.
5. Patch the outputs. GRASS and POP. move in opposite directions, SWARM moves along the strip, and WIND swings both ways.""",
"patching": """• Paired slow LFOs: GRASS to a filter cutoff and POP. to a reverb mix. As one rises the other falls.

• Moving sound: SWARM into a panner. The sound follows the locusts across the stereo field.

• Weather events: Set RAIN to Rain gate and use it to open a reverb or sweep a filter. Use SEED to pluck strings or fire percussion.

• Drift: WIND, attenuated, into a pitch or delay time for slow, organic movement.

• Sixteen lanes: POLY into 16 VCA levels or brightness controls for a field of moving amplitudes."""
},

"zephyr": {
"tagline": "A polyphonic oscillator and LFO with three families of waveforms, morphable in two directions.",
"panelMap": """ZEPHYR is a polyphonic oscillator and LFO built on three families of waveforms, arranged as a space you can move through in two directions. WAVE picks one of 16 shapes in a family, and WAVE SET moves between the three families, blending them in between. Both wrap around at the ends, so you can keep going forever.

- Set A: classic shapes. Pulses, saws, arches and spikes.
- Set B: harmonic and tonal shapes. Fourier series, formants and spectral sweeps.
- Set C: rhythmic and melodic gestures. Bitcrushed staircases, supersaws, zigzags and holds.
WAVE SET has soft detents at A, B and C, so it's easy to land on a pure family.

The display shows the current waveform for the first voice. At LFO rates a dot follows the playhead.

Sliders (each with trim and CV)
- WAVE SET: moves between families A, B and C.
- WAVE: moves through the 16 shapes.
- PHASE: offsets the start of the wave. Poly CV sets it per voice.
- FILTER: a low-pass after the shaper. Above about 0.8 it's out of the way; at LFO rates it's off.

Pitch
- RANGE switch: Audio, Low (6 octaves down) or Slow (12 octaves down, for LFOs).
- Big knob: frequency, ±4V.
- V/OCT: polyphonic, up to 16 voices.

FM and sync
- EXP: exponential FM input, with trim.
- LIN: linear through-zero FM input, with amount knob.
- HARD: hard sync. A rising edge restarts the wave.
- SOFT: soft sync. A rising edge reverses the wave's direction.

Outputs
- PHASOR: the oscillator's phase as a 0–10V ramp, polyphonic.
- OUT: the audio, polyphonic.

Context menu
- Output Range: ±5V (default), ±10V, 0–10V or 0–5V.
- Supersampling, and Oversampling Factor (Off, 2x default, 4x, 8x).""",
"basicUse": """1. Patch a poly V/oct into V/OCT. Use the knob to tune and RANGE for the octave.
2. Pick a family with WAVE SET and a shape with WAVE.
3. Modulate WAVE and WAVE SET to move through the shapes.
4. Use FILTER to soften the top end.
5. For an LFO, set RANGE to Slow and leave V/OCT unpatched. The knob sets the rate.""",
"patching": """• Poly synth: Poly V/oct from a sequencer or MIDI. A poly envelope on WAVE gives each note its own timbre, and a slow LFO on WAVE SET moves the whole sound.

• Two-way morphing: Two LFOs at different rates into WAVE and WAVE SET. The timbre keeps evolving without obvious repeats.

• Shaped LFO: RANGE on Slow. Set C gives rhythmic, gate-like contours; Set B gives smooth movement.

• FM pair: One ZEPHYR's OUT into another's LIN, with the amount knob set to taste.

• Sync sweep: One ZEPHYR's PHASOR into a second one's HARD, tuned higher. Sweep the second one's WAVE and WAVE SET while it's synced.

• Ramp source: PHASOR is a clean 0–10V ramp following the pitch, for waveshapers and scanners."""
},

"droplet": {
"tagline": "A strikeable resonator ring feeding a plate reverb, with clickable node modes, FM, and dynamics that move the sliders for you.",
"panelMap": """DROPLET is two physical models joined together: a ring of eight resonating nodes (the drop) feeding an eight-node plate reverb (the plate). Strike the ring for bells, tines and cymbals, or feed it audio and use it as a resonant reverb. Everything is polyphonic. The poly input with the most channels sets the voice count, and an input with fewer channels holds its last channel for the voices above it.

How it works
- The drop: each node is a tuned delay line with gentle saturation and its own compression. The eight nodes are spread across the stereo field. TEMPER couples each node to its neighbors.
- The plate: a network of allpass delays mixed together, shaped by PLATE, DIFFUSE, COUPLE, DECAY and DAMP.
- SHIMMER links the two. It slowly drifts the tuning of each node, which keeps the ring from building up on one note, and it raises extra connections: across the ring, across the plate, and from the plate back into the ring, following the lines on the panel. At zero those connections are off; turned up, the two models exchange more and more energy and the sound gets bigger and more complex.

Inputs (left)
- PITCH: knob and V/oct input for the ring's pitch, polyphonic.
- FM: input and FM amount trimmer, between PITCH and DROP IN. Exponential FM of the ring's pitch, polyphonic. The trimmer is tapered so small amounts get most of its travel (25% ≈ 0.016 oct/V, 50% ≈ 0.125, 100% = 1 oct/V). FM skips the pitch glide, so audio-rate FM works.
- DROP IN L/R: audio into the ring.
- PLATE IN L/R: audio straight into the plate.
- STRIKE: trigger input and button. Polyphonic triggers strike each voice separately; the button strikes them all.

The grid (center)
- Sixteen lights: the top two rows are the drop's nodes, the bottom two the plate's. The large light is the node's energy and the small white light its detuning. The grid shows the first voice.
- Every light is also a button that changes the node's mode. Modes are shared by all voices, saved with the patch, and crossfade when you click them. Hover over a node to see its mode.
  - Drop nodes: Normal (blue) or Hollow (white). A Hollow node flips its feedback and halves its delay, so it rings at the same pitch with odd harmonics only, like a tube or a clarinet. Hollow nodes ring much longer and bloom: they're held up at a steady level, then let go once they fade below a threshold.
  - Plate nodes: Normal (orange), Long (pink) or Short (yellow). Long reads the line at 4× its length for later reflections and a longer tail. Short reads it at ¼, a tight comb with a metallic, boxy ring.
- Eight node trims around the circle offset each drop node's tuning. The ? button randomizes them and the 0 button zeros them.

Mix (top right)
- WET: dry to wet, with trim and CV.
- BLEND: the wet sound, from pure ring (zero) to pure plate (full), with trim and CV. In between, the ring is mixed in inverted, as it would be physically, which gives a natural comb-like color.
- VOL.: output level, with CV.

Outputs
- OUTPUTS L/R: stereo, polyphonic.
- DROP: the ring's level as an envelope, 0–10V, per voice. Blue meter.
- STRIKE: the strike's envelope, 0–10V, per voice. Yellow meter.

Sliders (bottom, each with trim and CV)
- Drop (blue): SHAPE (how the nodes are spread: unison, spread, spread into chaos, pure chaos), SHIMMER, TEMPER, RES. (how long the ring sustains).
- Plate (yellow): DIFFUSE (density), PLATE (spacing and scatter of the plate nodes), COUPLE (energy shared between plate nodes), DECAY (tail length), DAMP (rolls off the highs in ring and plate; it fades in over the bottom quarter, then sweeps from 8 kHz down to 200 Hz).
- DYNAMICS (white): how much, and which way, the dynamics follower moves the sliders.

Dynamics
- The buttons above the first nine sliders choose which ones the dynamics follower moves.
- The button above DYNAMICS chooses the source: DROP level (blue), STRIKE envelope (yellow), or off.

Context menu
- Node Modes: Drop nodes (All Normal, All Hollow, Checkerboard, Randomize), Plate nodes (All Normal, All Long, All Short, Checkerboard Long / Short, Randomize), Randomize all node modes, Reset all node modes. The submenus show how many nodes are in each mode.
- Dynamics Envelope: Follow Time.
- Auto Rand. Thresh. and Rand. Range: randomize the node trims automatically when the ring gets loud enough, and set how far.
- Resonator Gain: drive inside the ring.
- Strike Character: Strike Length, Slant, Curve, Strike Intensity and Noise.
- Plate Seed (0–99999) and Re-roll Plate Character: each seed is a different plate.
- Panic: Clear All Energy.""",
"basicUse": """1. Strike it:
   - Set the pitch, then press STRIKE or patch triggers in. A poly V/oct and poly triggers give each note its own ring and plate.

2. Shape the ring:
   - SHAPE from unison to chaos, RES. for sustain, TEMPER to blend the nodes, SHIMMER to link ring and plate.

3. Shape the plate:
   - DIFFUSE, PLATE, COUPLE and DECAY set the space. DAMP darkens both.

4. Set the mix:
   - BLEND chooses between ring and plate; WET mixes in the dry sound. For a plain reverb send, set BLEND to full plate.

5. Feed it audio:
   - DROP IN excites the ring; PLATE IN goes straight to the plate.

6. Change the nodes:
   - Click drop nodes for Hollow, and plate nodes for Long or Short.

7. Add FM:
   - Patch a modulator into FM and raise the trimmer.

8. Let the dynamics play:
   - Light some DYN buttons, choose a source, and raise DYNAMICS.""",
"patching": """• Plate reverb: Audio into DROP IN, BLEND at full plate, WET to taste. Shape the tail with DIFFUSE and DECAY.

• Resonator: BLEND at zero and strike it, or feed it audio. A tuned comb or metallic resonator.

• Bells and tines: Leave the inputs empty, sequence PITCH and trigger STRIKE.

• Big steel: SHIMMER at 0.5–0.8. The ring and plate trade energy for long, complex, inharmonic decays.

• Cymbals: DAMP at zero, DECAY at 0.9, SHIMMER at 0.6–0.8, then press ? to randomize the trims.

• Hollow tubes: All drop nodes Hollow. Same pitch, odd harmonics only, with a long bloom.

• Long hall or metal box: All plate nodes Long for a bigger space; a few Short for a tight metallic ring on top.

• Bowed drone: An audio-rate gate into STRIKE keeps exciting the ring. Shape it with Strike Length and Slant.

• Reactive reverb: Drums into DROP IN, source on DROP (blue), DECAY's DYN button on. Loud hits lengthen the tail.

• Per-voice envelopes: Use STRIKE out to drive a VCA or filter for each voice.

• Audio-rate FM: An oscillator on the same V/oct into FM, trimmer at 25–40%, for gong and bell sidebands."""
},

"strands": {
"tagline": "A hurdy-gurdy: six strings bowed by a rosined wheel, twelve sympathetic strings, and the buzzing chien.",
"panelMap": """STRANDS is a physical model of a hurdy-gurdy. A turning wheel bows six strings at once. Two melody strings (chanterelles) follow V/oct and play left and right. Three drone strings (mouche, bourdon and trompette) sit at fixed intervals below the root. Twelve sympathetic strings, in six tuned pairs, ring along with the bowed strings. The trompette rests on the chien, a loose bridge that buzzes when you push the wheel harder, the hurdy-gurdy's signature rattle.

The wheel is a real rosined wheel, not a perfect one. Its surface repeats with every turn:
- Unevenness: broad high and low spots, the same for every string, so the instrument swells and dips once per turn.
- Grit: the rosin's grain. Each string runs on its own track across the wheel, catching and releasing on its own.
- Wobble: slow variation in the crank speed, from the player's hand. It fades out at very low speeds, so a stopped wheel really stops.
The bow's grip also follows the wheel speed, so a faster wheel is louder but keeps the clean sawtooth motion of a bowed string instead of turning thin and reedy.

The display shows the melody string, fixed at both ends, with an ellipse for the wheel's contact point and speed. It warms from blue-gray to amber as you bow harder and add DRIVE.

Stereo: the two chanterelles and the two trompettes each have their own chain (saturation and body resonator), one per side. The other drones and the sympathetic strings sit in the middle.

Sliders (each with trim and CV)
- TONE: brightness at the bridge, 300 Hz to 18 kHz.
- DRIVE: saturation after the strings, before the body.
- POS.: where the wheel touches the string. Low is round; high is bright and nasal, near the bridge.
- SYMP.: how much the sympathetic strings ring.

Knobs and jacks
- Big knob: melody pitch (±1V around C4), with V/OCT below. The drones follow the knob only, not V/OCT.
- BOW: wheel speed, -2 to +2, with trim and CV. Negative turns the wheel backwards. At zero the module sleeps.
- TIRANT: input and trim. Pushes on the chien; at zero it stays silent.
- VOL.: volume, with CV.
- FM: input and trim. FM on the melody strings; depth in semitones is set in the context menu.
- OUT L / R.

Context menu
- Bow Junction: Sticking Friction, Slip Falloff, Capture Velocity and String Impedance. These are the grip of the bow. They're set for a moderate wheel speed and scale with it above that.
- Drone Strings: Drone Mix Level, and the Mouche, Bourdon and Trompette intervals below the root.
- Melody / FM: FM Depth, and 2nd Chanterelle Detune (cents) for beating and width.
- Sympathetic Strings (12, 6 pairs): Max Coupling, Sympathetic Decay, Sympathetic Damping, Pair Spread (the two strings in a pair sit this many cents apart, so they beat slowly like a real course), and the interval of each pair.
- Wheel: Grit, Unevenness and Wobble.
- Body: Body Feedback and Body Diffusion, the resonance of the instrument's body.
- Trompette Chien: Enable, the Chien Pulse (Width and Amplitude of the rattle), Trigger Depth at Full Tirant, and 2nd Trompette Detune (which puts the buzz in stereo).
- Panic: Clear All Energy.""",
"basicUse": """1. Turn the wheel:
   - Turn up BOW. The strings start once the wheel is fast enough. An envelope into BOW CV makes each note bloom.

2. Play a melody:
   - Patch V/oct into V/OCT. The drones stay on the root set by the big knob.

3. Shape the tone:
   - TONE for brightness, POS. for where the wheel touches, DRIVE for grit.
   - The Bow Junction menu sets the grip. Less capture and more slip falloff sound crisper, and the display's wave sharpens toward a sawtooth.

4. Add the buzz:
   - Patch a CV into TIRANT. The chien fires when the trompette's vibration dips below a level set by the tirant. Zero never fires; more fires more often; past full it buzzes constantly.
   - Each fire is a short rattle of shrinking bounces. Chien Pulse Width and Amplitude set its length and level.
   - Two chiens, one per trompette, fire at slightly different times, so the buzz is in stereo.

5. Add the sympathetic strings:
   - Raise SYMP. They're tuned to the bowed strings' notes and hear the chanterelles fully and the drones lightly. They bloom when the melody lands on one of their notes.

6. Shape the wheel and body:
   - Wheel menu: Grit for a rough, rosiny catch, Unevenness for a swell on every turn, Wobble for hand drift. Set all three to zero for a perfectly smooth wheel.
   - Body menu: Body Feedback for sustain and a boxy warmth, Body Diffusion for its color.

7. If it locks up on high notes:
   - Notes above about +2V fold down an octave automatically. If it still saturates, use Panic.""",
"patching": """• Melody over drones: V/oct into V/OCT, an envelope into BOW. The melody speaks on each note over a constant drone.

• Drone only: BOW at a fixed level, nothing in V/OCT. Use SYMP. and Body Feedback to fill it out.

• Expressive bowing: A mod wheel or expression pedal into BOW. Slow is fragile and breathy; fast is loud and saturated.

• Rhythmic buzz: A stepped sequence into TIRANT so the chien buzzes on some notes and not others.

• Vibrato or sitar: A little LFO on FM for vibrato. More FM Depth and a faster LFO gives metallic, sitar-like tones.

• Sympathetic bloom: SYMP. high, and the six pairs tuned to notes of your scale. Raise Pair Spread for a wider, slower shimmer.

• Sul ponticello: POS. near the top, TONE bright, a little DRIVE, and less Capture Velocity, for a nasal folk fiddle.

• Width: Raise 2nd Chanterelle Detune and 2nd Trompette Detune for a wide, beating image; set both to zero for near mono.

• Violin: Drone Mix Level to zero, POS. at 0.39, SYMP. at 0.2, DRIVE at 0.2. In Bow Junction, Sticking Friction 2 and Capture Velocity 0.4. Lower Grit and Unevenness for a smoother stroke.

• Rustic wheel: Raise Grit and Unevenness with a slow BOW, like an old, well-played instrument. Speed up and the swells follow.

• Clean synth drone: Grit, Unevenness and Wobble at zero, with all the movement coming from BOW CV."""
},
}
