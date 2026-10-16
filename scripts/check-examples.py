"""Compile every example with Typst without leaving output files in the repository."""
import argparse
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--typst", default="typst", help="Typst executable (default: PATH)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    examples = sorted((root / "examples").rglob("*.typ"))
    if not examples:
        parser.error("No example .typ files found")
    subprocess.run([args.typst, "--version"], check=True)
    with tempfile.TemporaryDirectory(prefix="term-examples-") as output:
        for index, source in enumerate(examples):
            # A page placeholder supports examples that expand to more than one page.
            destination = Path(output) / f"{index}-{{p}}.svg"
            subprocess.run([args.typst, "compile", "--root", str(root), str(source), str(destination)], check=True, timeout=60)
            print(f"PASS {source.relative_to(root).as_posix()}", flush=True)
    print(f"Compiled {len(examples)} examples successfully.")


if __name__ == "__main__":
    main()
