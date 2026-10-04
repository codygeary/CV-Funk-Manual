MODULES = {
"aulos": {
"tagline": "A polyphonic double-pipe wind instrument. Morph from flute to reed, flare the bore into brass, and overblow into higher registers.",
"panelMap": """AULOS is a physical model of a wind instrument, named after the ancient Greek double pipe. Each voice is a waveguide: a tube with waves travelling up and down it, reflecting at both ends. REED and BORE change those reflections directly, which reshapes the instrument itself. There are two pipes: MAIN, and a SECondary pipe you can tune to an interval or hold as a drone.

The display shows both tubes, MAIN on top and SEC. below. Each one shows its length, the breath filling it, a standing wave, its register and any overblow, with air streaming out of the bell and bursts of chiff on each attack. The bell flares with BORE, and the SEC. tube dims in drone mode.

Pitch: PIPE and FINGER
- PIPE input and knob (-1 to +4 octaves): the pipe's fundamental, the note the tube naturally wants to play. It doesn't have to follow the melody.
- FINGER input and knob (±1 octave): the fingering. This sets the tube's length, and the ratio of FINGER to PIPE sets the register. Around twice the PIPE pitch the tube overblows up an octave; around four times, up another. The change takes about 200 ms, so the tone morphs instead of jumping. Fingering below the pipe fundamental is allowed too, and gives a whistly low end.
- GATE input and button: polyphonic, up to 16 voices. The voice count follows the widest of GATE, FINGER and PIPE. The button holds the gate open for every voice.

Breath
- BREATH: breath pressure, with trim and CV. At zero there's no sound at all. Past a light threshold the note speaks and builds over its attack. More breath is louder and edgier, and at the top it pushes into overblow by itself.
- VIBRATO input and depth knob: with nothing patched, an internal LFO wobbles the pitch and the breath together. A patched CV replaces it and only moves the pitch.

Sliders (each with trim and CV)
- REED: flute to reed. At zero an air jet drives an open tube: the full harmonic series, breathy and hollow, like a flute. At the top a beating reed drives a closed tube: odd harmonics only, about an octave lower, buzzy and stable, like a clarinet. The middle is a crossover no real instrument has, with a sound all its own.
- BORE: the shape of the bell. Up to about 0.75 the tube widens like a clarinet body and the tone fills out without getting brighter. Past that it flares into a brass horn and brightens.
- DRIVE: saturation on the excitation only. The tube itself stays clean, so DRIVE adds harmonics without making the loop unstable.
- RES.: feedback in the tube. More resonance sustains more. If it squeals, turn it down.
- AIR: breath noise mixed into the excitation.
- CHIFF: the burst of air at the start of each note. Zero for none, up to a long, loud attack.
- SEC.: pitch of the second pipe, ±1 octave. Zero is unison, +0.585 a perfect fifth, +1 an octave.
- WOOD: damping inside the tube, from bright to warm and dark. It's scaled with register, so high notes keep their harmonics.

Other jacks
- DRONE button and input: locks the second pipe's gate on. It plays a little quieter than the main pipe and fades in and out without clicks. The input toggles it on each gate.
- EXT. IN and EXT. GAIN: feed audio into the tube to excite it from outside.
- VOLUME: output level, 0 to 3x, with trim and CV.
- ENVELOPE: the breath envelope, polyphonic, with a blue meter.
- RMS: a follower on the excitation, polyphonic, with a yellow meter.
- MAIN and SEC.: audio outputs for the two pipes. The second pipe only runs while SEC. is patched.

Context menu
- Aulos R Voice Mode: Tracking (interval preserved) keeps the second pipe at the same interval in every register. Two Pipes (fixed registers) lets each pipe find its own register from its own pitch.
- Resonator: Waveguide Gain (overall level into the tube) and Decay (ring-out after the gate falls).
- Envelope: Attack and Release times, and Envelope Curves for each (log to exponential).
- Vibrato: Rate (3–12 Hz) and Breath Coupling (how much the vibrato moves the breath as well as the pitch).
- Articulation: Legato. With a held gate, pitch changes slur instead of retriggering, with a little give in the tube at each slur. Legato Glide Time sets the glide.
- Dynamics Envelope: Follow Time for the RMS follower.
- Panic: Clear All Energy.""",
"basicUse": """1. Play a note:
   - Patch the same V/oct into PIPE and FINGER, and a gate into GATE. The tube plays at its fundamental.
   - Set BREATH. Too little and it won't speak; more makes it louder and edgier.

2. Choose the instrument:
   - REED low for flute, high for clarinet.
   - BORE above 0.75 for brass.
   - WOOD for a darker tone, DRIVE for more harmonics.

3. Add breath and attack:
   - AIR for breath noise, CHIFF for the tongued attack.

4. Overblow:
   - Send FINGER an octave above PIPE and the tube jumps to its next register, the way a real woodwind does.

5. Add the second pipe:
   - Patch SEC. and set the SEC. slider to an interval. Turn on DRONE to hold it while MAIN plays the melody.

6. Excite it with audio:
   - Patch a sound into EXT. IN and raise EXT. GAIN. The tube resonates at the PIPE pitch.""",
"patching": """• Flute melody: Same V/oct into PIPE and FINGER, REED near zero, DRIVE about 0.5, a little CHIFF.

• Reed lead: REED near the top. Add BORE past 0.75 for a brassier reed.

• Bore sweep: Sweep BORE from 0 to 1 with a slow LFO or envelope. The tone fills out, then flares into brass at the top, a morph no real instrument can make.

• Drone and melody: Patch SEC., set it to +0.585 (a fifth) or +1.0 (an octave), and turn on DRONE. The second pipe holds a drone under the melody and follows PIPE, so it stays in tune.

• Poly chords: Poly V/oct into FINGER and a poly gate into GATE. Every channel is a complete instrument with its own register.

• Crescendo from silence: Patch an expression pedal or slow envelope into BREATH CV. The note grows out of nothing. Use ENVELOPE to open a filter in step.

• Voice into the tube: Patch a vocal or formant sound into EXT. IN. The tube acts as a pitched resonator tuned by PIPE.

• Slurred phrases: Turn on Legato and keep the gate high while the pitch changes.

• Delayed vibrato: Automate the VIBRATO depth knob with a slow envelope so the vibrato swells in after the note starts.

• Dynamics follower: RMS rises with each attack and follows the playing. Use it to open a filter so louder notes are brighter."""
},

"glass": {
"tagline": "A glass armonica: 37 tuned glass bowls you play with friction. Polyphonic, stereo, with a 12-channel output by note.",
"panelMap": """GLASS is a physical model of a glass armonica, Benjamin Franklin's instrument of nested spinning glass bowls played with wet fingers. It has 37 bowls tuned chromatically from C3 to C6. Each bowl rings up while your finger is on it and keeps ringing after you lift it.

The display shows all 37 bowls. Ringing bowls glow in proportion to their energy.

Playing
- V/OCT (polyphonic): picks the bowls. Each channel plays the nearest bowl. With no GATE patched, V/OCT holds the bowls on.
- GATE (polyphonic): puts a finger on each bowl.
- PRESSURE (polyphonic, 0–10V): how hard each finger presses. More pressure is louder and rings up faster.
- MUTE GATE (polyphonic, matched to V/OCT): damps the matching bowl so it rings down instead of cutting off.
- DAMP ALL input and button: damps every ringing bowl.

Sliders (each with trim and CV)
- ROTATE: how fast the bowls spin, 0–6 Hz. Sets the excitation level and the speed of the wobble.
- WATER: how wet the glass is. Dry is noisy and scratchy; wet is pure and singing.
- DECAY: how long the bowls ring after you lift your finger.
- DAMP: the overall tone of all the bowls, from bright to dark.
- WOBBLE: how much the axle wobbles, adding tremolo at the rotation speed.

Lower panel
- ROOT: transposes everything, ±2 octaves.
- FM / OFFSET: pitch offset knob, plus CV with trim, applied to every bowl.
- EXT. IN and EXT. GAIN: feed audio into the bowls while they're gated.
- SPREAD: stereo width.
- VOLUME, with trim and CV.
- RMS: an envelope that follows the output level, 0–10V, with a 10-light meter.
- OUT L / R.

Poly out by note: turn it on in the context menu and OUT L, OUT R and RMS each become 12-channel poly cables, one channel per note name: channel 1 is C, channel 2 is C#, through to channel 12, which is B. Every octave of a note shares its channel, so the C3, C4, C5 and C6 bowls all come out on channel 1. SPREAD still applies, and each channel gets its own saturation and its own RMS envelope. The meter still shows the whole mix.

Context menu
- Pressure Envelope: Attack and Release for the finger pressure, and Envelope Curves (log to exponential) for each.
- Water (Grip) Noise Color: Max Noise Cutoff, how bright the noise is at the dry end of WATER.
- Poly out: one channel per note (C to B), as above.
- Damper Gate: Damper Depth, how dark a bowl goes when it's damped or muted.
- Panic: Clear All Bowl Energy.""",
"basicUse": """1. Patch a poly V/oct into V/OCT and a poly gate into GATE.
2. Set ROTATE to 1–4 Hz, the range a real player would turn the bowls.
3. Set WATER to about 0.6–0.75 for the clearest tone. Lower is scratchier; very high gets too slippery to speak.
4. Set DECAY for how long notes ring after release.
5. Shape the tone with DAMP.
6. Patch an envelope or velocity into PRESSURE for dynamics.
7. To process notes separately, turn on Poly out in the context menu and patch OUT into a poly filter, VCA or mixer.""",
"patching": """• Solo voice: One channel of V/oct and gate, an envelope into PRESSURE, WATER at 0.7, ROTATE at 2–3 Hz.

• Chords: The bowls share the available energy like a real armonica, so single notes ring louder and fuller than dense chords.

• Shaping single notes: Patch a poly gate into MUTE GATE, lined up with your V/oct channels. Muted bowls darken and fade instead of stopping dead.

• Slow blooms: A slow LFO on DAMP or WATER makes the tone open and close over time.

• Bowls as a resonator: Patch audio into EXT. IN. While gates are held, the audio excites the bowls.

• Damped rhythms: Patch a fast gate pattern into DAMP ALL with DECAY high. The bowls are cut off in rhythm against a long ring.

• Ambient clouds: DECAY high, WATER around 0.65, and short gates on a slow chord sequence. The bowls keep ringing and overlap into clouds of harmony.

• Per-note processing: Turn on Poly out and patch OUT into a poly filter or effect. Each note name has its own channel, so you can darken certain notes, delay the fifths, or pan each pitch class on its own.

• Note-name envelopes: In poly out mode RMS carries 12 envelopes, one per note name. Use them to drive a poly VCA on another voice, or to trigger something whenever a particular note rings."""
},

"haze": {
"tagline": "A stereo three-voice chorus that turns into a diffuse, resonant haze as you push it.",
"panelMap": """HAZE is a stereo chorus with three voices, each with its own feedback loop. The HAZE control takes it from a clean chorus shimmer into sustained, Doppler-drifting resonance. Each voice can also switch to a diffuse mode that smears it into something closer to a reverb.

There are six modulated delay lines, three for each side, all driven from one LFO. Left voices sit at 0°, 120° and 240°; right voices at 60°, 180° and 300°. That spacing gives natural stereo width from one control.

Nodes: the three circles at the corners of the triangle are lights and buttons, one per voice. In chorus mode a light glows blue on the positive half of its LFO and yellow on the negative half. Click it to switch that voice to diffuse mode, where it glows purple and green and the voice runs through a chain of four allpass filters. Switching fades over 3 ms, so it never clicks.

Sliders (each with trim and CV)
- RATE: LFO speed. Slow settings shimmer; fast settings give audible Doppler pitch wobble.
- DEPTH: how far the delays are modulated. The lower half is classic chorus; the upper half gets wild.
- HAZE: feedback and tone. At zero each voice dies away immediately, for a clean chorus. Turning it up feeds each delay back into itself, so the sound sustains and Doppler-shifted resonances build up. At the same time a filter in the feedback darkens the tail.

Knobs (each with trim and CV)
- DENSITY: how hard the feedback drives the saturator. Low is open and airy; high is thick and saturated.
- MIX: dry to wet.

Jacks
- IN L / R: a mono signal in L goes to both sides.
- GAIN: output level.
- OUT L / R.

Context menu
- Haze cutoff @ 0% and Haze cutoff @ 100%: the feedback filter's cutoff at each end of the HAZE slider. Set the 100% cutoff low for a dark tail, or high to keep it bright.
- Diffuse mode coefficient: how strongly the diffuse voices smear, 0.1–0.95. Default 0.7.""",
"basicUse": """1. Patch audio into IN and take OUT.

2. Start with a clean chorus:
   - RATE slow, DEPTH about a quarter, HAZE at zero, MIX at 50%.

3. Set the character:
   - DENSITY low for airy, high for thick.
   - GAIN for the output level.

4. Push into haze:
   - Raise HAZE slowly. The tails start to sustain and drift in pitch, and the tone darkens. Adjust the cutoffs in the context menu if it gets too dark or too bright.

5. Diffuse it:
   - Click a node to switch that voice to diffuse. Try one, two or all three for more smearing.

6. Modulate:
   - A slow LFO into RATE CV with the trim low gives a drifting chorus speed.
   - An envelope into HAZE CV pushes loud moments into resonance and lets quiet moments stay clean.""",
"patching": """• Classic stereo chorus: RATE slow, DEPTH a quarter, HAZE zero, MIX 50%. Widens a mono source without colouring it.

• Thick ensemble: Push DENSITY toward full for gentle saturation in the feedback.

• Shimmering tail: HAZE at 60–70%. The three voices resonate and drift with the LFO. Set the 100% cutoff below 1 kHz for a much darker tail.

• Flanger: DEPTH near the top with a very slow RATE. HAZE adds resonant peaks to the sweep.

• Diffuse cloud: All three nodes on diffuse and HAZE at 50%. The tail becomes a dense, smeared wash, good on drums and noise.

• Half and half: Put only one or two nodes in diffuse, for something between chorus and diffusion.

• Reactive fog: Patch an envelope follower into HAZE CV. Quiet passages stay clean and loud ones bloom.

• Self-oscillating resonator: HAZE at maximum and DEPTH about 20%. The voices sustain on their own and drift in pitch. Send in a short click for a pitched, ringing decay. RATE sets how fast the pitch drifts."""
},
}
