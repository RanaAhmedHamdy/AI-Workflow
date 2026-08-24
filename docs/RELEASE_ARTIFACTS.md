# Release artifacts

The release is built once from the approved tag. The same wheel and sdist are
used for PyPI and attached to the GitHub Release; the clean source ZIP is the
repository evaluation artifact.

Expected files for `0.9.0`:

```text
ai_workflow-0.9.0-py3-none-any.whl
ai_workflow-0.9.0.tar.gz
AI-Workflow-0.9.0-source.zip
SHA256SUMS
RELEASE_MANIFEST.json
```

`RELEASE_MANIFEST.json` records the project version, exact Git commit, artifact
type, filename, SHA-256, and build timestamp. Python-normalized distribution
filenames must be retained; do not rename them manually.

The source ZIP includes the Android and iOS examples. The wheel and sdist
include the installer assets but not the native demo trees. The release build
must reject `.git`, `AUDIT`, `AUDIT.zip`, `.obsidian`, macOS metadata, build
outputs, caches, virtual environments, and developer-local files.

The owner must retain the build logs and `RELEASE_MANIFEST.json` with the
release evidence. A checksum match is required before attaching or publishing
an artifact.
