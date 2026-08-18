\
#!/usr/bin/env python3
"""Install AI-Workflow skills into another repository."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GREEN = ROOT / "Greenfield_AI_Mobile_Governance_Package_v1_9_1" / "skills"
BROWN = ROOT / "Brownfield_AI_Playbook_Reusable_Package_v4_4" / "skills"


def copy_item(src: Path, dst: Path, *, force: bool, dry_run: bool) -> None:
    if dst.exists() and not force:
        raise FileExistsError(f"destination exists: {dst} (use --force to replace)")
    print(f"{'WOULD COPY' if dry_run else 'COPY'} {src.relative_to(ROOT)} -> {dst}")
    if dry_run:
        return
    if dst.exists():
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("package", choices=["greenfield", "brownfield"])
    ap.add_argument("--platform", choices=["android", "ios"], help="required for greenfield")
    ap.add_argument("--target", type=Path, default=Path.cwd(), help="receiving repository root")
    ap.add_argument("--force", action="store_true", help="replace existing installed skill paths")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    target = args.target.resolve()
    skills_root = target / ".agents" / "skills"

    if args.package == "greenfield":
        if not args.platform:
            ap.error("--platform is required for greenfield")
        src = GREEN / args.platform
        dst = skills_root / args.platform
        copy_item(src, dst, force=args.force, dry_run=args.dry_run)
    else:
        if args.platform:
            ap.error("--platform is not used for brownfield")
        for src in sorted(BROWN.iterdir()):
            if src.is_dir() and (src / "SKILL.md").exists():
                copy_item(src, skills_root / src.name, force=args.force, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
