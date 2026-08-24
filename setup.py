from pathlib import Path
import sys
from setuptools import find_packages, setup

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
from ai_workflow.assets import BROWN_PACKAGE, GREEN_PACKAGE

GREEN = ROOT / GREEN_PACKAGE
BROWN = ROOT / BROWN_PACKAGE
DATA_ROOT = Path("share") / "ai-workflow"


def tree_data_files(source: Path, destination: Path):
    entries = []
    for directory in sorted(p for p in source.rglob("*") if p.is_dir()):
        files = [
            str(p)
            for p in sorted(directory.iterdir())
            if p.is_file() and p.name != ".DS_Store"
        ]
        if files:
            relative = directory.relative_to(ROOT)
            entries.append((str(destination / relative), files))
    files = [
        str(p)
        for p in sorted(source.iterdir())
        if p.is_file() and p.name != ".DS_Store"
    ]
    if files:
        relative = source.relative_to(ROOT)
        entries.append((str(destination / relative), files))
    return entries


data_files = []
for source in [
    GREEN / "skills",
    GREEN / "templates",
    BROWN / "skills",
    BROWN / "templates",
    BROWN / "repository-starter",
    BROWN / "checklists",
]:
    data_files.extend(tree_data_files(source, DATA_ROOT))

data_files.append(
    (
        str(DATA_ROOT / BROWN.name / "playbook"),
        [str(BROWN / "playbook" / "BROWNFIELD_PLAYBOOK.md")],
    )
)

setup(
    name="ai-workflow",
    version="0.9.0",
    description="Repository bootstrap CLI for AI-assisted native mobile governance workflows",
    long_description=(ROOT / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/RanaAhmedHamdy/AI-Workflow",
    license="Apache-2.0",
    python_requires=">=3.10",
    package_dir={"": "src"},
    packages=find_packages("src"),
    data_files=data_files,
    entry_points={"console_scripts": ["ai-workflow=ai_workflow.cli:main"]},
)
