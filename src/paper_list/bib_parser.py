from bibtexparser import Library, parse_string
from typing import List


def check_conferences(conference: str) -> str:
    c = conference.lower()
    if "dac" in c or "design automation conference" in c:
        return "DAC"
    if "hpca" in c or "high performance computer architecture" in c:
        return "HPCA"
    if "date" in c or "in europe" in c:
        return "DATE"
    if "isca" in c or "international symposium on computer" in c:
        return "ISCA"
    if "micro" in c:
        return "MICRO"
    if "arxiv" in c:
        return "arXiv"
    else:
        print(c)
        raise "Unknown conference"


def check_commas(author: str) -> str:
    if "," in author:
        name = author.split(",")
        assert len(name) == 2
        return f"{name[1].strip()} {name[0].strip()}"
    else:
        return author


def author_list(authors: str) -> List[str]:
    authors = authors.split("and")
    authors = [check_commas(x.strip()) for x in authors]

    return authors


def check_publisher(pub: str) -> str:
    if "{ACM}" in pub:
        return '"ACM"'
    elif "{IEEE}" in pub:
        return '"IEEE"'
    else:
        return pub


with open("works.bib", "r") as f:
    library: Library = parse_string(f.read())
    n = 1
    for entry in library.entries:
        title = entry["title"]
        title = f'paper-{n}-{title.replace(" ", "_").lower()}.md'
        title = title.replace(":", "")
        n += 1
        s = "---\n"
        for key, val in entry.items():
            if key == "author":
                val = author_list(val)
            if key == "conference":
                val = check_conferences(val)
            if key == "title" or key == "abstract":
                val = f'"{val}"'
            if key == "publisher":
                val = check_publisher(val)
            s += f"{key}: {val}\n"

        if not entry.__contains__("url"):
            s += "url: TBP\n"
        if "doi" not in entry:
            s += "doi: TBP\n"
        # s += f'citation: "{entry._raw.replace("\n", " ")
        #                    .replace("\t", " ")
        #                    .replace("@", "")}"\n'
        s += "---\n"

        with open(title, "w") as of:
            of.write(s)
