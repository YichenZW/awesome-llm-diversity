# Awesome Paperlist Maintainer

An automated maintenance tool for curated academic awesome paper lists on Github. Simply maintain a plain text file containing paper URLs. The system will automatically handle formatting, sectioning, ordering, etc.

### Setup
Run `pip install -e .` first.

### Add new papers
Add paper entry in `url_lists/url_list.txt`, following the format introduced in `url_lists/README.md`. Section structure (topic titles) and paper venues are defined in `src/config.py`. All papers with unmatched topic strings will be sectioned into 'Other'.

### Generate paper list
Run `python scripts/run.py` or `PYTHONPATH=. python scripts/run.py`. The output Markdown page will be at `outputs/main.md`. Each paper entry would show its title, paper link, time, authors, venue (if applicable), and keywords (optional).

For example,

> * **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?** [[paper](http://arxiv.org/abs/2310.06770)] 2023-10  
 Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan. ICLR 2024.
 Keywords: Code, Benchmark

Papers will be organized into sections and follow the time order (newest first). 
