---
name: android-adaptive-ui-readiness
description: Establishes and verifies a concrete Android adaptive-layout and accessibility contract across approved windows, inputs, RTL, large text, and assistive technology.
---
# Android Adaptive UI Readiness

Before implementation output a screen adaptation contract: compact/medium/expanded arrangements; portrait/landscape; resize/multi-window; applicable devices; navigation ownership; state preservation; RTL; font/display scale; insets/IME; keyboard/pointer/focus; fold posture relevance; semantic roles and labels; TalkBack traversal; focus visibility/order; touch-target and contrast checks; previews; runtime matrix; unsupported/unverified configurations.

Prefer flexible constraints, content-width limits, grids/flows/panes, and one shared business state. Flag fixed phone roots, portrait assumptions, raw-pixel logic, duplicate state per layout, leaf-owned shell navigation, hardcoded left/right, clipped text, and stretch-only tablet layouts.

Static previews do not prove runtime compatibility, TalkBack behavior, keyboard focus, or large-text usability. Exercise the approved representative adaptive configuration, large-font configuration, and assistive-technology journey at runtime.
