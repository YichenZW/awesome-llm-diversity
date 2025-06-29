import json
from src.paper import Paper
from config.config import CUSTOM_CATEGORY_ORDER

url_list_file = 'url_lists/url_list.txt'
rawlist_file = 'data/raw_paper_list.json'
paperlist_brief_file = 'data/paper_list_brief.json'
md_beginning_file = 'textual_framework/beginning.md'
md_brief_file = 'outputs/main.md'

brief = True #[todo: a concise version of the paper list containing tldr and tags]

def url2rawlist(url_file_dir, rawlist_file_dir):
    """
    Convert a list of URLs to a raw list of papers.
    """
    def load_url_list(url_file_dir):
        with open(url_file_dir, 'r') as file:
            url_list = [line.strip() for line in file if line.strip()]
        return url_list 

    def save_rawlist(rawlist, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(rawlist, file, indent=4)
            print(f"Raw list saved to {file_path}.")
        except IOError as e:
            print(f"Error saving raw list to {file_path}: {e}")

    def generate_rawlist(url_list):
        rawlist = []
        for url_line in url_list:
            parts = url_line.split(", ")
            url = parts[0]
            topic = parts[1]
            if len(parts) > 2:
                keywords = parts[2].split("/")
                keywords = [keyword.strip() for keyword in keywords]
            else:
                keywords = []
            rawlist.append({
                "title": "",
                "link": url.replace("https", "http"),
                "topic": topic,
                "keywords": keywords,
            })
        return rawlist

    url_list = load_url_list(url_file_dir)
    if url_list:
        rawlist = generate_rawlist(url_list)
        save_rawlist(rawlist, rawlist_file_dir)
    return rawlist

def generate_brief_paper_list(rawlist_file_dir, output_file_dir):
    """
    Generate a brief readable list of papers from a raw list of papers.
    """
    def load_raw_paper_list(file_path):
        with open(file_path, 'r') as file:
            raw_paper_list = json.load(file)
        return raw_paper_list
        
    def save_brief_paper_list(brief_list, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(brief_list, file, indent=4)
            print(f"Brief paper list saved to {file_path}.")
        except IOError as e:
            print(f"Error saving brief paper list to {file_path}: {e}")

    def generate_brief_paper_list(raw_paper_list):
        brief_list = []
        for paper in raw_paper_list:
            paper_obj = Paper(paper)
            success = paper_obj.get_info_arxiv() 
            if success is False:
                continue
            brief_list.append(paper_obj.__dict__)
        return brief_list

    rawlist = load_raw_paper_list(rawlist_file_dir)
    print(f"Successfully loaded {len(rawlist)} papers.")
    if rawlist:
        brief_paper_list = generate_brief_paper_list(rawlist)       
        save_brief_paper_list(brief_paper_list, output_file_dir)
    return brief_paper_list

def generate_markdown(paperlist_file_dir, output_md_file_dir):
    """
    Generate a markdown file from a list of papers with 2-level hierarchy.
    """
    def load_paperlist(file_path):
        try:
            with open(file_path, 'r') as file:
                paper_list = json.load(file)
            return paper_list
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {file_path}.")
            return []
    
    def organize_papers_by_hierarchy(papers):
        """Organize papers into a hierarchical structure."""
        hierarchy = {}
        
        for paper in papers:
            topic = paper.get("topic", "")
            if "/" in topic:
                # This is a subcategory (e.g., "Methodology/Finetuning")
                main_category, sub_category = topic.split("/", 1)
                if main_category not in hierarchy:
                    hierarchy[main_category] = {}
                if sub_category not in hierarchy[main_category]:
                    hierarchy[main_category][sub_category] = []
                hierarchy[main_category][sub_category].append(paper)
            else:
                # This is a main category (e.g., "Alignment")
                if topic not in hierarchy:
                    hierarchy[topic] = {}
                if "General" not in hierarchy[topic]:
                    hierarchy[topic]["General"] = []
                hierarchy[topic]["General"].append(paper)
        
        return hierarchy
    
    papers = load_paperlist(paperlist_file_dir)
    print(f"Successfully parsed {len(papers)} papers.")
    hierarchy = organize_papers_by_hierarchy(papers)

    with open(output_md_file_dir, 'w') as md_file:
        # Input the beginning content
        with open(md_beginning_file, 'r', encoding='utf-8') as md_beginning_f:
            beginning = md_beginning_f.read()
        md_file.write(beginning)

        print("Beginning content copied successfully.")
        print(f"Length of beginning content: {len(beginning)} characters")
        
        def sort_main_categories(category):
            """Sort main categories by custom order, with unspecified categories at the end."""
            try:
                return CUSTOM_CATEGORY_ORDER.index(category)
            except ValueError:
                # If category is not in the custom order, put it at the end
                return len(CUSTOM_CATEGORY_ORDER) + 1
        
        for main_category in sorted(hierarchy.keys(), key=sort_main_categories):
            md_file.write(f"## {main_category}\n\n")
            
            # Sort subcategories alphabetically, but put "General" last
            def sort_key(sub_cat):
                return (sub_cat == "General", sub_cat)
            
            for sub_category in sorted(hierarchy[main_category].keys(), key=sort_key):
                if sub_category != "General":
                    md_file.write(f"### {sub_category}\n\n")
                else:
                    md_file.write("\n\n")
                
                # Sort papers by time (newest first)
                category_papers = hierarchy[main_category][sub_category]
                category_papers.sort(key=lambda x: x.get("time", ""), reverse=True)
                
                for i, paper in enumerate(category_papers, start=1):
                    try:
                        paper_obj = Paper(paper)
                    except ValueError as e:
                        print(f"Skipping paper due to error: {e}")
                        continue
                    if brief:
                        md_file.write(paper_obj.brief_str() + "\n\n")
                    else:
                        md_file.write(repr(paper_obj) + "\n\n")


def main():
    rawlist = url2rawlist(url_file_dir=url_list_file, rawlist_file_dir=rawlist_file)

    brief_paperlist = generate_brief_paper_list(rawlist_file_dir=rawlist_file, output_file_dir=paperlist_brief_file)

    if brief_paperlist:
        generate_markdown(paperlist_file_dir=paperlist_brief_file, output_md_file_dir=md_brief_file)
        print(f"Markdown file generated: {md_brief_file}")

if __name__ == "__main__":
    main()