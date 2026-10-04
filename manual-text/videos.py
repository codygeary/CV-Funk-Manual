# Videos for each module and collection. "start" is in seconds. "chapters" are
# listed when the whole video is about that module or collection.
OMRI, SAT = "Omri Cohen", "SATURATA MODULAR"
SEPT = {"id": "EdPVROhwRts", "title": "New Modules, September 2025", "by": OMRI, "start": 541}
NOV  = {"id": "r3QMHA-M_ZM", "title": "New Modules, November 2025", "by": OMRI, "start": 1026}
MODS = {"id": "eaU2KAXOeCI", "title": "CV funk Modulations overview and tutorial", "by": OMRI}
PATCHWERK = {"id": "yBYJJB05Drw", "title": "PatchWerk with Miles, EP11: CV funk Modules", "by": "Warm Natural", "start": 0}
FR = {"id": "sm0ftWGepqM", "title": "Modules CV funk pour VCV Rack: patch « Weather Resistance » (en français)", "by": "Arnaud Pfliger"}
SANDS = {"id": "x1XtCPUz2BU", "title": "Exploring CV funk Sands: 5 generative patches", "by": SAT}

def at(v, start, **kw):
    d = dict(v); d["start"] = start; d.update(kw); return d

MODULES = {
    "chord-caster": [{"id": "x65hqgAlfEA", "title": "Chord Caster overview and tutorial", "by": OMRI, "start": 0, "chapters": [
        [20, "Basic functionality"], [300, "Voices"], [476, "Editing steps"], [690, "Strum"],
        [837, "Inputs"], [1052, "Outputs"], [1185, "Miscellaneous"]]}],
    "syzygy": [at(MODS, 48)], "arrange-xl": [at(MODS, 373)],
    "super-wonk": [at(MODS, 862)], "envelope-city": [at(MODS, 1103)],
    "sirocco": [{"id": "71VM0LNKil4", "title": "Generative ambient with SIROCCO: a living ecosystem as modulation", "by": SAT, "start": 0}],
    "droplet": [{"id": "Rb3OGfsvwug", "title": "What happens when you process external audio with Droplet", "by": OMRI, "start": 0, "chapters": [
        [0, "Drums"], [128, "Noise"], [198, "A drone"], [266, "A sequence"], [407, "Feedback"]]},
        at(SANDS, 410, title="Exploring CV funk Sands: patch 3, Droplets")],
    "cartesia": [{"id": "hlZukBHdDws", "title": "Cartesian sequencing with Cartesia", "by": OMRI, "start": 0, "chapters": [
        [11, "Basic functionality"], [271, "With trigger sequencers"], [485, "With CV"], [785, "Polyphony"]]},
        {"id": "WDYUZTbBZ9I", "title": "Transforming an ambient patch live (slow, fast, slow)", "by": SAT, "start": 0}],
    "step-wave": [{"id": "LT-7bXAbz20", "title": "Unlock endless rhythmic variations with Step Wave", "by": OMRI, "start": 0, "chapters": [
        [11, "Basic functionality"], [238, "Beats and shapes"], [424, "S&H and T&H"], [585, "As an oscillator"]]},
        at(FR, 580)],
    "ouros": [at(PATCHWERK, 0), at(FR, 129)],
    "envelope-array": [at(FR, 163)], "signals": [at(FR, 173)], "tri-delay": [at(FR, 185)],
    "impulse-controller": [at(PATCHWERK, 0), at(FR, 340)],
    "penta-sequencer": [at(FR, 462)], "flower-patch": [at(FR, 528)],
    "magnets": [at(PATCHWERK, 0), at(FR, 610)],
    "pressed-duck": [at(PATCHWERK, 0)], "hex-mod": [at(PATCHWERK, 0)],
    "strings": [at(PATCHWERK, 0)], "collatz": [at(PATCHWERK, 0)],
}
for slug in ["hammer", "picus", "wonk", "weave", "junk-dna", "node"]:
    MODULES[slug] = [SEPT]
for slug in ["alloy", "clpy", "onion", "count", "rat", "tuner"]:
    MODULES[slug] = [NOV]

COLLECTIONS = {
    "sands": [{**SANDS, "start": 0, "chapters": [[29, "Patch 1: Sands"], [273, "Patch 2: Sands"], [410, "Patch 3: Droplets"], [547, "Patch 4: Drone"], [646, "Patch 5: Sands"]]}],
    "chord-caster": [{"id": "x65hqgAlfEA", "title": "Chord Caster overview and tutorial", "by": OMRI, "start": 0}],
    "modulations": [{**MODS, "start": 0, "chapters": [[48, "SYZYGY"], [373, "Arrange XL"], [862, "Super Wonk"], [1103, "Envelope City"]]}],
}
