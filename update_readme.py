import os
import re
import json
import time
import urllib.request
import urllib.error


README_FILE = "README.md"
GITHUB_REPO = "https://github.com/CARLOX62/LeetCode/tree/main"


# ---------------------------------------------------------
# Get LeetCode problem information
# ---------------------------------------------------------

def get_leetcode_data(title_slug):
    """
    Get problem information from LeetCode GraphQL API.
    """

    url = "https://leetcode.com/graphql"

    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            title
            difficulty
            topicTags {
                name
                slug
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {
            "titleSlug": title_slug
        }
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))

        question = result.get("data", {}).get("question")

        if question:
            return question

    except Exception as e:
        print(f"Could not fetch {title_slug}: {e}")

    return None


# ---------------------------------------------------------
# Convert difficulty to emoji
# ---------------------------------------------------------

def format_difficulty(difficulty):

    if difficulty == "Easy":
        return "🟢 Easy"

    if difficulty == "Medium":
        return "🟡 Medium"

    if difficulty == "Hard":
        return "🔴 Hard"

    return "⚪ Unknown"


# ---------------------------------------------------------
# Find all LeetCode folders
# ---------------------------------------------------------

def find_problems():

    problems = []

    for item in os.listdir("."):

        if not os.path.isdir(item):
            continue

        # Match folders like:
        # 0001-two-sum
        # 0054-spiral-matrix
        # 2877-create-a-dataframe-from-list

        match = re.match(r"^(\d+)-(.+)$", item)

        if not match:
            continue

        number = int(match.group(1))
        slug = match.group(2)

        print(f"Found problem: {number}-{slug}")

        problems.append({
            "number": number,
            "slug": slug,
            "folder": item
        })

    problems.sort(key=lambda x: x["number"])

    return problems


# ---------------------------------------------------------
# Get complete problem information
# ---------------------------------------------------------

def enrich_problems(problems):

    complete_problems = []

    for index, problem in enumerate(problems):

        print(
            f"[{index + 1}/{len(problems)}] "
            f"Fetching LeetCode #{problem['number']}..."
        )

        data = get_leetcode_data(problem["slug"])

        if data:

            problem["title"] = data.get(
                "title",
                problem["slug"].replace("-", " ").title()
            )

            problem["difficulty"] = format_difficulty(
                data.get("difficulty")
            )

            problem["topics"] = [
                tag["name"]
                for tag in data.get("topicTags", [])
            ]

        else:

            # Fallback if LeetCode API fails

            problem["title"] = (
                problem["slug"]
                .replace("-", " ")
                .title()
            )

            problem["difficulty"] = "⚪ Unknown"

            problem["topics"] = []

        complete_problems.append(problem)

        # Small delay to avoid sending too many requests
        time.sleep(0.3)

    return complete_problems


# ---------------------------------------------------------
# Create Solved Problems table
# ---------------------------------------------------------

def create_solved_table(problems):

    table = """
# 📂 Solved Problems

<!-- AUTO-GENERATED:SOLVED:START -->

| # | Problem | Difficulty |
|---|---------|------------|
"""

    for problem in problems:

        number = problem["number"]
        title = problem["title"]
        difficulty = problem["difficulty"]
        folder = problem["folder"]

        link = f"{GITHUB_REPO}/{folder}"

        table += (
            f"| {number} | "
            f"[{title}]({link}) | "
            f"{difficulty} |\n"
        )

    table += """
<!-- AUTO-GENERATED:SOLVED:END -->

"""

    return table


# ---------------------------------------------------------
# Create Topic sections
# ---------------------------------------------------------

def create_topic_section(problems):

    topics = {}

    for problem in problems:

        for topic in problem["topics"]:

            if topic not in topics:
                topics[topic] = []

            topics[topic].append(problem)

    # Sort topics alphabetically
    topics = dict(sorted(topics.items()))

    output = """
# 🧠 LeetCode Topics

<!-- AUTO-GENERATED:TOPICS:START -->

"""

    for topic, topic_problems in topics.items():

        output += f"## {topic}\n\n"

        output += "| # | Problem |\n"
        output += "|---|---------|\n"

        topic_problems.sort(key=lambda x: x["number"])

        for problem in topic_problems:

            number = problem["number"]
            title = problem["title"]
            folder = problem["folder"]

            link = f"{GITHUB_REPO}/{folder}"

            output += (
                f"| {number} | "
                f"[{title}]({link}) |\n"
            )

        output += "\n"

    output += "<!-- AUTO-GENERATED:TOPICS:END -->\n\n"

    return output


# ---------------------------------------------------------
# Replace an existing generated section
# ---------------------------------------------------------

def replace_section(content, start_marker, end_marker, new_content):

    pattern = (
        re.escape(start_marker)
        + r".*?"
        + re.escape(end_marker)
    )

    if re.search(pattern, content, flags=re.DOTALL):

        return re.sub(
            pattern,
            new_content.strip(),
            content,
            flags=re.DOTALL
        )

    return None


# ---------------------------------------------------------
# Update README
# ---------------------------------------------------------

def update_readme(problems):

    if not os.path.exists(README_FILE):

        print("README.md not found.")

        return

    with open(
        README_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    solved_table = create_solved_table(problems)
    topics_section = create_topic_section(problems)

    # -----------------------------------------------------
    # Update Solved Problems
    # -----------------------------------------------------

    solved_start = "<!-- AUTO-GENERATED:SOLVED:START -->"
    solved_end = "<!-- AUTO-GENERATED:SOLVED:END -->"

    solved_replacement = solved_table

    updated = replace_section(
        content,
        solved_start,
        solved_end,
        solved_replacement
    )

    if updated is not None:

        content = updated

    else:

        # If section does not exist, insert before Roadmap
        roadmap = "# 🎯 Roadmap"

        if roadmap in content:

            content = content.replace(
                roadmap,
                solved_table + roadmap,
                1
            )

        else:

            content += "\n" + solved_table

    # -----------------------------------------------------
    # Update Topics
    # -----------------------------------------------------

    topic_start = "<!-- AUTO-GENERATED:TOPICS:START -->"
    topic_end = "<!-- AUTO-GENERATED:TOPICS:END -->"

    topic_replacement = topics_section

    updated = replace_section(
        content,
        topic_start,
        topic_end,
        topic_replacement
    )

    if updated is not None:

        content = updated

    else:

        # If an old "LeetCode Topics" section exists,
        # remove it before adding the new generated section.

        old_topics_pattern = (
            r"# LeetCode Topics.*"
        )

        content = re.sub(
            old_topics_pattern,
            "",
            content,
            flags=re.DOTALL
        )

        content = content.rstrip() + "\n\n" + topics_section

    # -----------------------------------------------------
    # Save README
    # -----------------------------------------------------

    with open(
        README_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    print()
    print("=" * 50)
    print("README UPDATED SUCCESSFULLY")
    print("=" * 50)
    print(f"Total problems: {len(problems)}")
    print("=" * 50)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("=" * 50)
    print("LeetCode README Updater")
    print("=" * 50)
    print()

    problems = find_problems()

    if not problems:

        print("No LeetCode problem folders found.")

        return

    print()
    print(f"Found {len(problems)} problems.")
    print()

    problems = enrich_problems(problems)

    update_readme(problems)


if __name__ == "__main__":
    main()
