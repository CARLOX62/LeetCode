import os
import re

README = "README.md"

# Difficulty based on LeetCode problem number
difficulty = {
    7: "🟢 Easy",
    9: "🟢 Easy",
    26: "🟢 Easy",
    53: "🟡 Medium",
    121: "🟢 Easy",
    128: "🟡 Medium",
    189: "🟡 Medium",
    283: "🟢 Easy",
    485: "🟢 Easy",
    509: "🟢 Easy",
    1768: "🟢 Easy",
    2149: "🟡 Medium",
}

problems = []

for folder in os.listdir("."):
    if not os.path.isdir(folder):
        continue

    match = re.match(r"(\d+)-(.+)", folder)

    if match:
        number = int(match.group(1))
        name = match.group(2).replace("-", " ").title()

        problems.append({
            "number": number,
            "name": name,
            "folder": folder,
            "difficulty": difficulty.get(number, "⚪ Unknown")
        })


# Sort by problem number
problems.sort(key=lambda x: x["number"])


# Create table
table = """# 📂 Solved Problems

| # | Problem | Difficulty |
|---|---------|------------|
"""

for problem in problems:
    table += (
        f'| {problem["number"]} | '
        f'[{problem["name"]}](https://github.com/CARLOX62/LeetCode/tree/master/'
        f'{problem["folder"]}) | '
        f'{problem["difficulty"]} |\n'
    )


# Read README
with open(README, "r", encoding="utf-8") as file:
    content = file.read()


# Replace Solved Problems section
pattern = r"# 📂 Solved Problems.*?(?=\n# 🎯 Roadmap)"

content = re.sub(
    pattern,
    table + "\n",
    content,
    flags=re.DOTALL
)


# Write README
with open(README, "w", encoding="utf-8") as file:
    file.write(content)

print(f"README updated with {len(problems)} problems.")
