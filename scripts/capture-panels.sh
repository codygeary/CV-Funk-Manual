#!/bin/zsh
# Render every CV funk panel, light and dark, with VCV Rack's screenshot mode.
#
#   scripts/capture-panels.sh                 all four plugins
#   scripts/capture-panels.sh CVfunk          just the free collection
#
# Rack runs twice against throwaway user folders that hold only the CV funk
# plugins, so your own Rack settings and patch are untouched. Quit Rack first.
# Renders land in panel-captures/light and panel-captures/dark (git-ignored).
# Review them, then:
#   python3 scripts/place-panels.py && python3 scripts/make-web-panels.py
#
# Screenshot mode doesn't switch themed panels, jacks and screws to their dark
# art, so the dark pass runs on copies where every X-dark.svg is copied over
# X.svg: the plugins' res folders and Rack's own (passed with -s). The copy
# links back to the app's libRack.dylib so plugins load a single libRack.

set -e
APP="/Applications/VCV Rack 2 Free.app/Contents"
PLUGINS="$HOME/Library/Application Support/Rack2/plugins-mac-arm64"
ROOT="${0:A:h:h}"
WORK="$ROOT/panel-captures"
ZOOM=2
SLUGS=("$@")
(( $#SLUGS )) || SLUGS=(CVfunk CVfunkModulations CVfunkChordCaster CVfunkSands)

if pgrep -xq Rack; then echo "Quit VCV Rack first."; exit 1; fi

darken() { find "$@" -name "*-dark.svg" | while read f; do cp "$f" "${f%-dark.svg}.svg"; done }

rm -rf "$WORK"; mkdir -p "$WORK"
for theme in light dark; do
  U="$WORK/user-$theme"
  mkdir -p "$U/plugins-mac-arm64"
  for s in $SLUGS; do cp -R "$PLUGINS/$s" "$U/plugins-mac-arm64/"; done
  args=(-u "$U" -t $ZOOM)
  if [[ $theme == dark ]]; then
    SYS="$WORK/system-dark"
    cp -R "$APP/Resources" "$SYS"
    ln -sf "$APP/Resources/libRack.dylib" "$SYS/libRack.dylib"
    darken "$SYS/res" "$U/plugins-mac-arm64"
    echo '{"preferDarkPanels": true}' > "$U/settings.json"
    args=(-s "$SYS" $args)
  else
    echo '{"preferDarkPanels": false}' > "$U/settings.json"
  fi
  echo "Rendering $theme panels..."
  "$APP/MacOS/Rack" $args > /dev/null 2>&1 || true
  cp "$U/log.txt" "$WORK/rack-$theme.log" 2>/dev/null || true
  if grep -q "Could not load plugin\|fatal" "$WORK/rack-$theme.log"; then
    echo "Rack reported a problem; see $WORK/rack-$theme.log"; exit 1
  fi
  mv "$U/screenshots" "$WORK/$theme"
  rm -rf "$U" "$WORK/system-dark"
done
# Rack also renders its own Core and Fundamental modules; keep only ours.
for theme in light dark; do rm -rf "$WORK/$theme/Core" "$WORK/$theme/Fundamental"; done
echo "Done: $(find "$WORK" -name '*.png' | wc -l | tr -d ' ') panels in $WORK"
