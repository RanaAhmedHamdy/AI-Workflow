# Example release-artifact policy

The native examples are source material for evaluation, not runtime dependencies.

| Artifact | Includes examples? | Rationale |
| --- | --- | --- |
| GitHub repository | Yes | Readers need the scenarios, source, routes, and evidence notes. |
| Generated public source ZIP | Yes | It is the clean-source evaluation artifact. |
| Python sdist | No | The distribution builds the installer package; native demo tooling would add unnecessary source weight. |
| Python wheel | No | The CLI runtime needs installer assets, not Android/Xcode fixtures. |

`tools/build_release.py` explicitly permits `examples/` in the public source ZIP. `tools/package_check.py` requires both fixture READMEs there and rejects them in wheel/sdist runtime distributions.
