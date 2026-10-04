
const DATA = JSON.parse(document.getElementById("cvf-data").textContent);
const BASE = DATA.base;
const RATIO = DATA.ratios;
const COLL = {
  "free":{label:"Free", lib:"CVfunk", paid:false},
  "modulations":{label:"Modulations", lib:"CVfunkModulations", paid:true},
  "chord-caster":{label:"Chord Caster", lib:"CVfunkChordCaster", paid:true},
  "sands":{label:"Sands", lib:"CVfunkSands", paid:true}
};
const ORDER = ["free","modulations","chord-caster","sands"];
const SECTIONS = [["panelMap","Panel map"],["basicUse","Basic use"],["patching","Patch ideas"],["videos","Videos"]];
const yt = (id, t) => `https://www.youtube.com/watch?v=${id}${t ? `&t=${t}s` : ""}`;
const mmss = t => `${Math.floor(t / 60)}:${String(t % 60).padStart(2, "0")}`;
function videosHTML(vs){
  return `<ul class="videos">${vs.map(v => `<li><a class="vt" href="${yt(v.id, v.start)}" target="_blank" rel="noreferrer">▶ ${esc(v.title)}</a><div class="vm">${esc(v.by)}${v.start ? ` · from ${mmss(v.start)}` : ""}</div>${(v.chapters || []).length ? `<div class="vc">${v.chapters.map(([t, l]) => `<a href="${yt(v.id, t)}" target="_blank" rel="noreferrer">${mmss(t)} ${esc(l)}</a>`).join("")}</div>` : ""}</li>`).join("")}</ul>`;
}

let MODS = [], COLLS = {}, slug = null, tab = "panelMap";
// One selection at a time: everything, one collection, one type, or a search.
let sel = {kind:"all", value:null};
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const normTag = t => { t = t.trim().toLowerCase(); return t[0].toUpperCase() + t.slice(1); };
const names = l => { const n = l.map(m => m.name); return n.length > 6 ? n.slice(0,5).join(", ") + ` and ${n.length - 5} more` : n.join(", ").replace(/, ([^,]*)$/, " and $1"); };
const libUrl = (c, m) => `https://library.vcvrack.com/${COLL[c].lib}${m ? "/" + m.vcvSlug : ""}`;

function isDark(){
  const t = document.documentElement.dataset.theme;
  return t ? t === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
}
const img = s => `${BASE}panels-web/${s}${isDark() ? "-dark" : ""}.jpg`;

/* ---------- inline text ---------- */
function inline(text){
  let h = esc(text);
  h = h.replace(/(?<![\w/-])([A-Z][A-Z0-9]*(?:[\/][A-Z0-9]+)*(?: (?:[A-Z][A-Z0-9]+|I{1,3})(?:[\/][A-Z0-9]+)*)*)(?![\w-])/g,
    m => (m.length < 2 || /^(I|A|B|L|R|V|CV|LFO|RMS|ADAA|FM|VCA|DC|LPF|ITD|MIDI|ASR|AD|FFT|NaN|MIT)$/.test(m)) ? m : `<span class="lbl">${m}</span>`);
  if (sel.kind === "search" && sel.value.length > 1){
    const words = sel.value.split(/\s+/).filter(w => w.length > 1).map(w => w.replace(/[.*+?^${}()|[\]\\]/g,"\\$&"));
    if (words.length) h = h.replace(new RegExp("(" + words.join("|") + ")(?![^<]*>)","gi"), "<mark>$1</mark>");
  }
  return h;
}
function termSplit(s){
  const i = s.indexOf(": ");
  return (i > 0 && i < 80) ? `<span class="term">${inline(s.slice(0,i))}</span>: ${inline(s.slice(i+2))}` : inline(s);
}

/* ---------- structured renderer for the plain-text sections ---------- */
function render(text, kind){
  const blocks = text.split(/\n\s*\n/).map(b => b.replace(/\s+$/,"")).filter(Boolean);
  if (kind === "patching"){
    return `<div class="patches">${blocks.map(b => {
      const s = b.replace(/^[•\-]\s*/,""), i = s.indexOf(": ");
      const title = i > 0 && i < 60 ? s.slice(0,i) : "";
      return `<article class="patch">${title ? `<h4>${esc(title)}</h4>` : ""}<p>${inline(title ? s.slice(i+2) : s).replace(/\n/g,"<br>")}</p></article>`;
    }).join("")}</div>`;
  }
  let out = "";
  for (const b of blocks){
    const lines = b.split("\n");
    if (/^\d+\.\s/.test(lines[0])){
      let html = "<ol>", open = false, sub = false;
      for (const ln of lines){
        const m = ln.match(/^(\d+)\.\s+(.*)$/);
        if (m){ if (sub){html += "</ul>"; sub = false} if (open) html += "</div></li>";
          html += `<li style="counter-set:s ${+m[1]}"><div class="st">${termSplit(m[2])}</div><div>`; open = true; continue; }
        const s = ln.match(/^\s+[-•]\s+(.*)$/);
        if (s){ if (!sub){html += "<ul>"; sub = true} html += `<li>${termSplit(s[1])}</li>`; continue; }
        if (ln.trim()){ if (sub){html += "</ul>"; sub = false} html += `<p>${termSplit(ln.trim())}</p>`; }
      }
      if (sub) html += "</ul>";
      if (open) html += "</div></li>";
      out += html + "</ol>"; continue;
    }
    let i = 0;
    if (lines.length > 1 && /:\s*$/.test(lines[0]) && !/^\s*-\s/.test(lines[0]) && lines[0].length < 90){
      out += `<h3>${esc(lines[0].replace(/:\s*$/,""))}</h3>`; i = 1;
    }
    const rest = lines.slice(i);
    if (rest.length && rest.every(l => /^\s*-\s/.test(l) || /^\s{2,}\S/.test(l))){
      let html = "<ul>", nest = false;
      for (const l of rest){
        const t = l.replace(/^\s*-\s*/,"").trim();
        if (/^\s{2,}-\s/.test(l)){ if (!nest){ html = html.replace(/<\/li>$/,"") + "<ul>"; nest = true } html += `<li>${termSplit(t)}</li>`; }
        else { if (nest){ html += "</ul></li>"; nest = false } html += `<li>${termSplit(t)}</li>`; }
      }
      out += html + (nest ? "</ul></li>" : "") + "</ul>";
    } else if (rest.length){
      const para = rest.filter(l => !/^\s*-\s/.test(l)), ul = rest.filter(l => /^\s*-\s/.test(l)).map(l => l.replace(/^\s*-\s*/,""));
      if (para.length) out += `<p>${para.map(inline).join("<br>")}</p>`;
      if (ul.length) out += `<ul>${ul.map(t => `<li>${termSplit(t)}</li>`).join("")}</ul>`;
    }
  }
  return out;
}

/* ---------- selection ---------- */
function matches(m){
  if (sel.kind === "coll") return m.collection === sel.value;
  if (sel.kind === "tag") return m.tags.map(normTag).includes(sel.value);
  if (sel.kind === "search" && sel.value.length > 1){
    const hay = (m.name+" "+m.tagline+" "+m.tags.join(" ")+" "+Object.values(m.sections).join(" ")).toLowerCase();
    return sel.value.toLowerCase().split(/\s+/).every(w => hay.includes(w));
  }
  return true;
}
const shown = () => MODS.filter(matches);

function buildChips(){
  const counts = {};
  MODS.forEach(m => m.tags.forEach(t => { t = normTag(t); counts[t] = (counts[t]||0) + 1; }));
  const types = Object.entries(counts).filter(([t,n]) => n >= 3 && t !== "Blank").sort((a,b) => a[0].localeCompare(b[0]));
  const on = (k,v) => sel.kind === k && (v === undefined || sel.value === v);
  $("#colls").innerHTML =
    `<button class="segbtn" data-all aria-pressed="${on("all") || sel.kind === "tag"}">All</button>` +
    ORDER.map(c => `<button class="segbtn" data-coll="${c}" aria-pressed="${on("coll",c)}"><span class="dot" style="background:var(--c-${c})"></span>${COLL[c].label}</button>`).join("");
  $("#type").innerHTML = `<option value="">All types</option>` +
    types.map(([t,n]) => `<option value="${esc(t)}"${on("tag",t) ? " selected" : ""}>${esc(t)} (${n})</option>`).join("");
}

function buildBanner(list){
  const b = $("#banner");
  b.style.removeProperty("--cc");
  if (sel.kind === "coll"){
    const c = sel.value, meta = COLL[c], col = COLLS[c] || {};
    b.style.setProperty("--cc", `var(--c-${c})`);
    b.innerHTML = `<p><span class="dot"></span><strong>${meta.label}</strong> · ${list.length} modules · ${meta.paid ? "Premium" : "Free and open source"}. ${esc(col.tagline || "")}</p>
      <a class="cta small" href="${libUrl(c)}" target="_blank" rel="noreferrer">${meta.paid ? "Buy" : "Install"} in the VCV Library</a>`;
  } else if (sel.kind === "tag"){
    const colls = [...new Set(list.map(m => m.collection))].map(c => COLL[c].label);
    b.innerHTML = `<p><strong>${esc(sel.value)}</strong> · ${list.length} module${list.length === 1 ? "" : "s"} in ${colls.join(", ").replace(/, ([^,]*)$/, " and $1")}.</p>`;
  } else if (sel.kind === "search"){
    b.innerHTML = `<p>${list.length ? `<strong>${list.length} module${list.length === 1 ? "" : "s"}</strong> mention “${esc(sel.value)}”.` : `Nothing in the manual matches “${esc(sel.value)}”. Try a control name like HEAT, or a technique like FM.`}</p>`;
  } else {
    b.innerHTML = `<p>Click a faceplate to open its manual.</p>`;
  }
}

function buildRack(list){
  let html = `<div class="rail"></div><div class="rackrow">`;
  if (!list.length) html += `<div class="none">No modules to show</div>`;
  for (const c of ORDER){
    const g = list.filter(m => m.collection === c);
    if (!g.length) continue;
    html += `<div class="group"><div class="gname"><i style="background:var(--c-${c})"></i>${COLL[c].label}
      <a href="${libUrl(c)}" target="_blank" rel="noreferrer">${COLL[c].paid ? "Buy ↗" : "Free ↗"}</a></div><div class="panels">`;
    for (const m of g) html += `<button class="pnl${m.slug === slug ? " on" : ""}" data-slug="${m.slug}" aria-label="${esc(m.name)}" style="aspect-ratio:${RATIO[m.slug] || .5}"><img loading="lazy" alt="" data-slug="${m.slug}" src="${img(m.slug)}"></button>`;
    html += `</div></div>`;
  }
  $("#type").addEventListener("change", e => e.target.value ? select("tag", e.target.value) : select("all", null));
const rack = $("#rack");
  rack.innerHTML = html + `</div><div class="rail"></div>`;
  rack.style.scrollBehavior = "auto"; rack.scrollLeft = 0; rack.style.scrollBehavior = "";
  $("#count").textContent = sel.kind === "all" ? `${MODS.length} modules` : `Showing ${list.length} of ${MODS.length} modules`;
  updateEdges();
}

function updateEdges(){
  const r = $("#rack"), box = $("#rackbox");
  const l = r.scrollLeft > 4, rr = r.scrollLeft + r.clientWidth < r.scrollWidth - 4;
  box.classList.toggle("more-l", l); box.classList.toggle("more-r", rr);
  const b = r.getBoundingClientRect(), ps = [...r.querySelectorAll(".pnl")].map(p => p.getBoundingClientRect());
  const nl = ps.filter(a => a.right < b.left + 20).length, nr = ps.filter(a => a.left > b.right - 20).length;
  $("#nl").textContent = nl ? "+" + nl : ""; $("#nr").textContent = nr ? "+" + nr : "";
  $("#left").setAttribute("aria-label", `Scroll left, ${nl} more panels`); $("#right").setAttribute("aria-label", `Scroll right, ${nr} more panels`);
}

function select(kind, value){
  sel = {kind, value};
  if (kind !== "search") $("#q").value = "";
  const list = shown();
  buildChips(); buildBanner(list); buildRack(list);
  if (list.length && !list.some(m => m.slug === slug)) open(list[0].slug);
  else if (slug && $("#sec")) showTab(tab);
}

/* ---------- module view ---------- */
function open(s, scroll, quiet){
  const m = MODS.find(x => x.slug === s); if (!m) return;
  slug = s;
  if (!quiet) try { history.replaceState(null, "", "#" + s); } catch {}
  const c = m.collection, col = COLLS[c] || {}, meta = COLL[c];
  const peers = MODS.filter(x => x.collection === c), i = peers.indexOf(m);
  const prev = peers[(i - 1 + peers.length) % peers.length], next = peers[(i + 1) % peers.length];
  const pdf = col.manualUrl ? `<a href="${col.manualUrl}" target="_blank" rel="noreferrer">${meta.label} PDF</a>` : `<span>${meta.label} PDF coming soon</span>`;
  const el = $("#mod");
  el.style.setProperty("--cc", `var(--c-${c})`);
  el.innerHTML = `
    <div class="face">
      <img src="${img(s)}" data-slug="${s}" alt="${esc(m.name)} panel">
      <div class="facenav">
        <button type="button" data-go="${prev.slug}"><small>Previous</small><span>${esc(prev.name)}</span></button>
        <button type="button" data-go="${next.slug}"><small>Next</small><span>${esc(next.name)}</span></button>
      </div>
    </div>
    <div class="doc">
      <div class="eyebrow"><span class="coll">${meta.label}${meta.paid ? " · Premium" : ""}</span>${col.version ? `<span>v${col.version}</span>` : ""}</div>
      <h2 class="name">${esc(m.name)}</h2>
      <p class="tagline">${esc(m.tagline)}</p>
      <div class="meta">${m.tags.map(t => `<button class="tag" data-tag="${esc(normTag(t))}">${esc(normTag(t))}</button>`).join("")}</div>
      <div class="links"><a class="${meta.paid ? "buy" : ""}" href="${libUrl(c, m)}" target="_blank" rel="noreferrer">${meta.paid ? "Buy in the VCV Library" : "Get it free in the VCV Library"}</a>${pdf}</div>
      <div class="tabs" role="tablist">${SECTIONS.filter(([k]) => k === "videos" ? (m.videos || []).length : m.sections[k]?.trim()).map(([k,l]) =>
        `<button role="tab" data-tab="${k}" aria-selected="${tab === k}">${l}${k === "videos" ? ` (${m.videos.length})` : ""}</button>`).join("")}</div>
      <div class="sec" id="sec"></div>
    </div>`;
  showTab((tab === "videos" ? (m.videos || []).length : m.sections[tab]?.trim()) ? tab : "panelMap");
  document.querySelectorAll(".pnl").forEach(p => p.classList.toggle("on", p.dataset.slug === s));
  const p = document.querySelector(`.pnl[data-slug="${s}"]`), r = $("#rack");
  if (p) r.scrollTo({left: p.offsetLeft - r.clientWidth / 2 + p.offsetWidth / 2});
  if (scroll) el.scrollIntoView({behavior:"smooth", block:"start"});
}
function showTab(k){
  tab = k;
  const m = MODS.find(x => x.slug === slug);
  document.querySelectorAll(".tabs button").forEach(b => b.setAttribute("aria-selected", b.dataset.tab === k));
  const s = $("#sec");
  s.className = "sec" + (k === "patching" ? " wide" : "");
  s.innerHTML = k === "videos" ? videosHTML(m.videos || []) : sectionHTML(m, k);
}
/* Figures: "[[fig:id]]" on its own line places a figure; unplaced ones go at the end of their section. */
const FIG_LINE = /^\s*\[\[fig:([\w-]+)\]\]\s*$/;
function figHTML(f){
  const src = BASE + f.src.replace(/^\/+/, "");
  return `<figure class="fig"><img loading="lazy" src="${src}" alt="${esc(f.alt || f.caption || "")}">${f.caption ? `<figcaption>${inline(f.caption)}</figcaption>` : ""}</figure>`;
}
function sectionHTML(m, k){
  const figs = m.figures || [], placed = new Set();
  Object.values(m.sections).forEach(t => t.split("\n").forEach(l => { const x = l.match(FIG_LINE); if (x) placed.add(x[1]); }));
  let out = "", buf = [];
  const flush = () => { const t = buf.join("\n").trim(); if (t) out += render(t, k); buf = []; };
  for (const line of (m.sections[k] || "").split("\n")){
    const x = line.match(FIG_LINE);
    if (!x){ buf.push(line); continue; }
    flush();
    const f = figs.find(f => f.id === x[1]); if (f) out += figHTML(f);
  }
  flush();
  figs.filter(f => !placed.has(f.id) && (f.section || "panelMap") === k).forEach(f => out += figHTML(f));
  return out;
}

/* ---------- events ---------- */
document.addEventListener("click", e => {
  const t = e.target.closest("[data-tab]"); if (t){ showTab(t.dataset.tab); return; }
  const g = e.target.closest("[data-go]"); if (g){ open(g.dataset.go); return; }
  const pn = e.target.closest(".pnl"); if (pn){ open(pn.dataset.slug, true); return; }
  if (e.target.closest("[data-all]")){ select("all", null); return; }
  const c = e.target.closest("[data-coll]");
  if (c){ select("coll", c.dataset.coll); if (c.hasAttribute("data-go-modules")) $("#modules").scrollIntoView({behavior:"smooth"}); return; }
  const tg = e.target.closest("[data-tag]");
  if (tg){ select("tag", tg.dataset.tag); $("#modules").scrollIntoView({behavior:"smooth"}); }
});
const rack = $("#rack");
rack.addEventListener("scroll", updateEdges, {passive:true});
addEventListener("resize", updateEdges);
$("#left").addEventListener("click", () => rack.scrollBy({left: -rack.clientWidth * .8}));
$("#right").addEventListener("click", () => rack.scrollBy({left: rack.clientWidth * .8}));
const tip = $("#tip");
rack.addEventListener("pointermove", e => {
  const b = e.target.closest(".pnl"); if (!b){ tip.hidden = true; return; }
  tip.textContent = MODS.find(x => x.slug === b.dataset.slug).name; tip.hidden = false;
  tip.style.left = Math.min(e.clientX + 12, innerWidth - tip.offsetWidth - 8) + "px"; tip.style.top = (e.clientY + 14) + "px";
});
rack.addEventListener("pointerleave", () => tip.hidden = true);
let qt; $("#q").addEventListener("input", e => { clearTimeout(qt); qt = setTimeout(() => {
  const v = e.target.value.trim(); v.length > 1 ? select("search", v) : (sel.kind === "search" && select("all", null)); }, 150); });
$("#home").addEventListener("click", e => { e.preventDefault(); select("all", null); scrollTo({top:0, behavior:"smooth"}); });
function swapImages(){ document.querySelectorAll("img[data-slug]").forEach(i => i.src = img(i.dataset.slug)); }
$("#theme").addEventListener("click", () => {
  const next = isDark() ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  try { localStorage.setItem("cvfunk-theme", next); } catch {}
  swapImages();
});
matchMedia("(prefers-color-scheme: dark)").addEventListener("change", swapImages);
try { const t = localStorage.getItem("cvfunk-theme"); if (t) document.documentElement.dataset.theme = t; } catch {}

/* ---------- boot ---------- */
(() => {
  MODS = ORDER.flatMap(c => DATA.modules.filter(m => m.collection === c));
  DATA.collections.forEach(c => COLLS[c.id] = c);
  $("#vers").textContent = DATA.collections.map(c => `${c.name} ${c.version}`).join(" · ");
  const h = location.hash.slice(1);
  // "#c-sands" opens a collection (the old /sands/ page redirects here); "#twang" opens a module.
  const coll = h.startsWith("c-") ? h.slice(2) : null;
  slug = MODS.some(m => m.slug === h) ? h : (coll ? (MODS.find(m => m.collection === coll) || MODS[0]).slug : MODS[0].slug);
  select(coll && COLL[coll] ? "coll" : "all", coll && COLL[coll] ? coll : null);
  const isModule = MODS.some(m => m.slug === h);
  // plain section anchors (#collections, #about) are left to the browser
  open(slug, false, !(isModule || coll));
  swapImages();
  // deep links land on their content, not the hero
  const target = isModule ? $("#mod") : coll ? $("#modules") : (h && document.getElementById(h));
  if (target){
    if ("scrollRestoration" in history) history.scrollRestoration = "manual";
    // images above the target keep loading and shifting it, so stay aligned while the layout settles
    const go = () => target.scrollIntoView();
    const settle = () => {
      go();
      const ro = new ResizeObserver(go); ro.observe(document.body);
      const stop = () => ro.disconnect();
      setTimeout(stop, 2000); addEventListener("wheel", stop, { once: true }); addEventListener("touchstart", stop, { once: true });
    };
    document.readyState === "complete" ? settle() : addEventListener("load", settle, { once: true });
  }
})();
