from pathlib import Path

years = {
    "2025": 
        ["BOI", "Tour", "Tower", "Developer", "Exponents", "GCD"]
    ,
    "2024": 
        ["Jobs", "Portal", "Trains", "Fire", "Tiles", "Wall"]
    ,
    "2023": 
        ["Astronomer", "Staring Contest", "Tycho", "Minequake", "Mineral Deposits", "Sequence"]
    ,
    "2022":
        ["Art", "Events", "Vault", "Communication", "Island", "Passes"]
    ,
    "2021":
        ["Books", "Servers", "Watchmen", "Prison", "Swaps", "Xanadu"]
    ,
    "2020":
        ["Colors", "Mixture", "Joker", "Graph", "Village", "Viruses"]
    ,
    "2019":
        ["Flash", "Nautilus", "Valley", "Kitchen", "Necklace", "Olympiads"]
    ,
    "2018":
        [("Love Polygon", "day1.pdf"), ("Martian DNA", "day1.pdf"), ("Worm Worries", "day1.pdf"), ("Alternating Current", "day2.pdf"), ("Genetics", "day2.pdf"), ("Paths", "day2.pdf")]
    ,
    "2017": # These years having no editorials is shameful
        [("Political*", "https://hackmd.io/sq5UfdRKQYKPTbEiaqf1LQ"), "", "", "", "", ""]
    ,
    "2016": # These years having no editorials is shameful
        ["", ("Park*", "https://hackmd.io/Xpf7nQRcS7WcAKkxiXxnBw"), "", "", "", ""]
    ,
    "2015": # These years having no editorials is shameful
        ["", "", ("Network*", "https://hackmd.io/ycF_LYeMRJ6VMMIUQs-zsQ"), "", "", ("Tug of War*", "https://hackmd.io/9HwGfPTXQsWuN0DQRJq2gw")]
    ,
    "2014":
        ["Cop and Robber", "Friends", "Sequence", "Demarcation", "Portals", ("Postmen*", "https://hackmd.io/-0c9lHR_QICv85TIXwPAbw")]
    ,
    "2013":
        ["Ball Machine", "Numbers", "Pipes", "Brunhilda", "Tracks", "Vim"]
    ,
    "2012": # Missing: tiny (output only with open input)
        ["Brackets", "Mobile", "Peaks", "Fire", "Melody", ""]
    ,
    "2011":
        ["Trees", "Icecream", "Lamp", "Vikings", "Meetings", "Plagiarism", "Polygon", "Mirroring"]
    ,
    "2010":
        ["Bears", "Lego", "PBC", "Bins", "Candies", "Mines"]
    ,
    "2009":
        ["Beetle", "Candy", "Subway", "Rectangle", "Triangulation", "Monument"]
    ,
    "2008":
        ["editorial"]
    ,
    "2007":
        ["editorial"]
    ,
    "2006": # Website has no editorials (https://www.cs.helsinki.fi/group/boi2006/). Cses only has some
        # Missing: coins (normal task), city (normal task)
        ["Bitwise", "", "Countries", "", "RLE", "Jump"]
    ,
    "2005": # Missing manuscript (normal task)
        ["Camp", "Magic", "Maze", "Ancient(t)", "Bustrip", "Polygon"]
    ,
    "2004": # CSES only has code solutions. Website has no editorials (http://www.boi2004.lv/)
        ["", "", "", "", "", ""]
    ,
    "2003":
        ["Barrel", "Gems", "Table*", "Gangs", "Lamps", "Regs"]
    ,
    "2002":
        ["Speed", "Tennis", "Triangles", "Bicriterial", "Lgame", "Robots"]
    ,
    "2001":
        ["Editorial"]
    ,
    "2000": # Not in English....
        ["Editorial(u)"]
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
        ["Square", "Sequence", "LogExp", "Barrels", "Journey", "NBgame"]
    ,
    "1995":
        ["Currency", "Expression", "Prime", "Rectangles", "Taxi", "IfThenElse"]
}

header = ["Year", "D1-1", "D1-2", "D1-3", "D2-1", "D2-2", "D2-3", "", ""]

print("""Legend:
- X: missing
- *: unofficial
- (t) translated
- (u) untranslated, not in English

Please contact me if you have any of the missing editorials.
Also feel free to contact me if you believe you have a better version of any of the unofficial ones.
""")

print("| " + " | ".join(header) + " |")
print("|" + "|".join(["------"] * len(header)) + "|")

extensions = ["pdf", "md", "txt"]
def format_url(year, task):
    task_name = None
    task_url = None
    if isinstance(task, str):
        task_name = task
    else:
        task_name = task[0]

    suffix = ""
    for mark in ["(u)", "(t)", "*"]:
        if mark in task_name:
            suffix += mark
            task_name = task_name.replace(mark, "")
    
    if isinstance(task, str):
        task_shortname = ''.join(task_name.split()).lower()
        for ext in extensions:
            if (Path("editions") / year / f"{task_shortname}.{ext}").exists():
                extension = ext
                break
        else:
            assert 0, f"Nothing for {year}/{task_name}"
        task_url = f"editions/{year}/{task_shortname}.{extension}"
    else:
        if "https" in task[1]:
            task_url = task[1]
        else:
            task_url = f"editions/{year}/{task[1]}"

    return f"[{task_name}]({task_url}){suffix}"

tot = 0
has = 0
for year, p_list in years.items():
    if len(p_list) == 0:
        continue
    tasks = []
    if len(p_list) in (6, 8):
        tasks = p_list
    elif len(p_list) == 1:
        tasks = [p_list[0]] * 6
    else:
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

print(f"\n\nProgress: {has/tot*100:.2f}% ({has}/{tot})")
