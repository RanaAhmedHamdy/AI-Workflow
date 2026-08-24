"""Compatibility build hook; package metadata lives exclusively in pyproject.toml."""
from pathlib import Path

from setuptools import setup

ROOT = Path(__file__).parent
DATA_ROOT = Path("share") / "ai-workflow"


def tree_data_files(source: Path):
    entries = []
    for directory in [source, *sorted(path for path in source.rglob("*") if path.is_dir())]:
        files = [str(path.relative_to(ROOT)) for path in sorted(directory.iterdir()) if path.is_file() and path.name != ".DS_Store"]
        if files:
            entries.append((str(DATA_ROOT / directory.relative_to(ROOT)), files))
    return entries


data_files = []
for relative in [
    "routing",
    "Greenfield_AI_Mobile_Governance_Package_v1_10_0/skills",
    "Greenfield_AI_Mobile_Governance_Package_v1_10_0/templates",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/skills",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/templates",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/repository-starter",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/checklists",
    "Brownfield_AI_Playbook_Reusable_Package_v4_4/playbook",
]:
    data_files.extend(tree_data_files(ROOT / relative))

setup(data_files=data_files)
