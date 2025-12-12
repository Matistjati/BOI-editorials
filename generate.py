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
    "2017":
        []
    ,
    "2016":
        ["", ("park", "https://hackmd.io/Xpf7nQRcS7WcAKkxiXxnBw")]
    ,
    "2015":
        ["", "", ("network", "https://hackmd.io/ycF_LYeMRJ6VMMIUQs-zsQ"), "", "", ("Tug of War", "https://hackmd.io/9HwGfPTXQsWuN0DQRJq2gw")]
    ,
    "2014":
        ["coprobber","friends","sequence","demarcation","portals",("postmen", "https://hackmd.io/-0c9lHR_QICv85TIXwPAbw")]
    ,
}

header = ["Year", "D1-1", "D1-2", "D1-3", "D2-1", "D2-2", "D2-3", "", ""]

print("Editorials marked with \\* are unofficial. Feel free to contact me if you have a better one available.\n")

print("| " + " | ".join(header) + " |")
print("|" + "|".join(["------"] * len(header)) + "|")

def format_url(year, task):
    if isinstance(task, str):
        if (Path("editions") / year / f"{task}.pdf").exists():
            extension = "pdf"
        else:
            extension = "md"
        return f"[{task.capitalize()}](editions/{year}/{task}.{extension})"
    else:
        return f"[{task[0].capitalize()}]({task[1]})\\*"

    return 

for year, p_list in years.items():
    if len(p_list) == 0:
        continue
    tasks = []
    if len(p_list) == 6:
        tasks = p_list
    elif len(p_list) == 2:
        tasks = [p_list[0], "", "", p_list[1]]
    else:
        print(p_list)
        assert 0
    row = [year]
    
    for task in tasks:
        if task:
            row.append(format_url(year, task))
        else:
            row.append("")
    
    print("| " + " | ".join(row) + " |")
