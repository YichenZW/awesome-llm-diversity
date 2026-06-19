# Run from the awesome-llm-diversity root directory.
# Updates the diversity paper list and syncs it to public/README.md.
cd "$(dirname "$0")"
MAINTAINER=../awesome-paper/awesome-paperlist_maintainer
cd "$MAINTAINER"
pip install -e . -q
PROJECT_NAME=diversity PYTHONPATH=. python scripts/run.py
rsync -a outputs/diversity.md ../awesome-llm-diversity/README.md
echo "Done. README.md updated."
