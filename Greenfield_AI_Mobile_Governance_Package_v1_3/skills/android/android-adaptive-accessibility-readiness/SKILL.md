---
name: adaptive-compose
description: Establishes and verifies a concrete Compose screen adaptation contract across approved windows, orientations, inputs, RTL, and large text.
---
# Adaptive Compose

Before implementation output a screen adaptation contract: compact/medium/expanded arrangements; portrait/landscape; resize/multi-window; applicable devices; navigation ownership; state preservation; RTL; font/display scale; insets/IME; keyboard/pointer/focus; fold posture relevance; previews; runtime matrix; unsupported/unverified configurations.

Prefer flexible constraints, content-width limits, grids/flows/panes, and one shared business state. Flag fixed phone roots, portrait assumptions, raw-pixel logic, duplicate state per layout, leaf-owned shell navigation, hardcoded left/right, clipped text, and stretch-only tablet layouts.

Static previews do not prove runtime compatibility.
