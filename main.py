import json

def add_problems():
    try:
        with open("problems.json","r") as f:
            problems = json.load(f)
    except:
        problems = []

    while True:
        a = input("name: ")
        b = input("difficulty: ")
        c = input("tags: ")

        c = c.split(",")
        c = [tag.strip() for tag in c]

        problem = {}
        problem["name"] = a
        problem["difficulty"] = b
        problem["tags"] = c

        problems.append(problem)

        answer = input("more problem? ").lower()
        if answer == "no":
            break
        elif answer == "yes":
            continue
        else:
            break

    with open("problems.json","w") as f:
            json.dump(problems,f)


def see_problem():
    try:
        with open("problems.json","r") as f:
            data = json.load(f)
        for problem in data:
            print(f"name:{problem['name']}")
            print(f"difficulty:{problem['difficulty']}")
            print(f"tags:{','.join(problem["tags"])}")
    except:
        print("No saved problems")

def problems_by_difficulty():
    try:
        with open("problems.json","r") as f:
            problems = json.load(f)
    except:
        print("No saved problems")
        return

    problem_type = input("difficulty: ").lower()

    for problem in problems:
        if problem["difficulty"] == problem_type:
            print(problem)

def Analyze():
    try:
        with open("problems.json","r") as f:
            problems = json.load(f)
    except:
        print("No saved problems")
        return
    
    count_difficulty,count_topic = {},{}
    for problem in problems:
        count_difficulty[problem["difficulty"]] = count_difficulty.get(problem["difficulty"],0) + 1
        for category in problem["tags"]:
            count_topic[category] = count_topic.get(category,0) + 1
    answer = input("problems by? ")
    if answer == "difficulty":
        for key in count_difficulty:
            print(f"{key}:{count_difficulty[key]}")
    elif answer == "tags":
        for key in count_topic:
            print(f"{key}:{count_topic[key]}")
    return 


while True:
    print("""Options:
1.Add problems
2.See all problems
3.See problems by difficulty
4.Analyze
5.Exit
""")
    try:
        answer = int(input())
    except:
        print("Invalid input")
        continue

    if answer == 1:
        add_problems()
    elif answer == 2:
        see_problem()
    elif answer == 3:
        problems_by_difficulty()
    elif answer == 4:
        Analyze()
    elif answer == 5:
        break
    else:
        print("Invalid value")


