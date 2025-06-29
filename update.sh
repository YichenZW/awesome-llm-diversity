# after updated awesome-paperlist-maintainer/url_lists/url_list.txt
cd awesome-paperlist-maintainer
pip install -e .
PYTHONPATH=. python scripts/run.py
rsync -a outputs/main.md ../public/README.md 
