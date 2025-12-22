from pathlib import Path

years = {
    "2025": 
        ["boi", "tour", "tower", "developer", "exponents", "gcd"]
    ,
    "2024": 
        ["jobs", "portal", "trains", "fire", "tiles", "wall"]
    ,
    "2023": 
        ["astronomer", "staringcontest", "tycho", "minequake", "mineraldeposits", "sequence"]
    ,
    "2022":
        ["art", "events", "vault", "communication", "island", "passes"]
    ,
    "2021":
        ["books", "servers", "watchmen", "prison", "swaps", "xanadu"]
    ,
    "2020":
        ["colors", "mixture", "joker", "graph", "village", "viruses"]
    ,
    "2019":
        ["flash", "nautilus", "valley", "kitchen", "necklace", "olympiads"]
    ,
    "2018":
        ["day1", "day2"]
    ,
    "2017": # These years having no editorials is shameful
        [("political", "https://hackmd.io/sq5UfdRKQYKPTbEiaqf1LQ"), "", "", "", "", ""]
    ,
    "2016": # These years having no editorials is shameful
        ["", ("park", "https://hackmd.io/Xpf7nQRcS7WcAKkxiXxnBw")]
    ,
    "2015": # These years having no editorials is shameful
        ["", "", ("network", "https://hackmd.io/ycF_LYeMRJ6VMMIUQs-zsQ"), "", "", ("Tug of War", "https://hackmd.io/9HwGfPTXQsWuN0DQRJq2gw")]
    ,
    "2014":
        ["coprobber","friends","sequence","demarcation","portals",("postmen", "https://hackmd.io/-0c9lHR_QICv85TIXwPAbw")]
    ,
    "2013":
        ["ballmachine", "numbers", "pipes", "brunhilda", "tracks", "vim"]
    ,
    "2012": # Missing: tiny (output only with open input)
        ["brackets", "mobile", "peaks", "fire", "melody", ""]
    ,
    "2011":
        ["trees", "icecream", "lamp", "vikings", "meetings", "plagiarism", "polygon", "mirroring"]
    ,
    "2010":
        ["bears", "lego", "pbc", "bins", "candies", "mines"]
    ,
    "2009":
        ["beetle", "candy", "subway", "rectangle", "triangulation", "monument"]
    ,
    "2008":
        ["editorial"]
    ,
    "2007":
        ["editorial"]
    ,
    "2006": # Website has no editorials (https://www.cs.helsinki.fi/group/boi2006/). Cses only has some
        # Missing: coins (normal task), city (normal task)
        ["bitwise", "", "countries", "", "RLE", "jump"]
    ,
    "2005": # Missing manuscript (normal task)
        ["camp", "magic", "maze", "", "bustrip", "polygon"]
    ,
    "2004": # CSES only has code solutions. Website has no editorials (http://www.boi2004.lv/)
        ["", "", "", "", "", ""]
    ,
    "2003": # The missing task, table, is open input heuristic
        ["barrel", "gems", "", "gangs", "lamps", "regs"]
    ,
    "2002":
        ["speed", "tennis", "triangles", "bicriterial", "lgame", "robots"]
    ,
    "2001":
        ["editorial"]
    ,
    "2000": # Not in English....
        ["editorial(u)"]
    ,
    "1999": # website up but no editorials https://www.lio.lv/boi99/. Cses only has code solutions
        ["", "", "", "", "", ""]
    ,
    "1998": # CSES archive lists no solutions, cant find website
        ["", "", "", "", "", ""]
    ,
    "1997": # CSES archive only has code solutions, cant find website
        ["", "", "", "", "", ""]
    ,
    "1996":
        ["square", "sequence", "logexp", "barrels", "journey", "nbgame"]
    ,
    "1995":
        ["currency", "expression", "prime", "rectangles", "taxi", "ifthenelse"]
}

header = ["Year", "D1-1", "D1-2", "D1-3", "D2-1", "D2-2", "D2-3", "", ""]

print("Editorials marked with \\* are unofficial, X are missing and (u) are not in English. Feel free to contact me if you have any (or a better one than mine) available.\n")

print("| " + " | ".join(header) + " |")
print("|" + "|".join(["------"] * len(header)) + "|")

extensions = ["pdf", "md", "txt"]
def format_url(year, task):
    if isinstance(task, str):
        for ext in extensions:
            if (Path("editions") / year / f"{task}.{ext}").exists():
                extension = ext
                break
        else:
            assert 0, f"Nothing for {year}/{task}"
        return f"[{task.capitalize()}](editions/{year}/{task}.{extension})"
    else:
        return f"[{task[0].capitalize()}]({task[1]})\\*"

tot = 0
has = 0
for year, p_list in years.items():
    if len(p_list) == 0:
        continue
    tasks = []
    if len(p_list) in (6, 8):
        tasks = p_list
    elif len(p_list) == 2:
        tasks = [p_list[0], p_list[0], p_list[0], p_list[1], p_list[1], p_list[1]]
    elif len(p_list) == 1:
        tasks = [p_list[0] for i in range(6)]
    else:
        print(p_list)
        assert 0
    row = [year]

    for task in tasks:
        tot += 1
        if task:
            if "(u)" not in task:
                has += 1
            row.append(format_url(year, task))
        else:
            row.append("X")
    
    print("| " + " | ".join(row) + " |")

print(f"\n\nProgress: {has/tot*100:.2f}%")
