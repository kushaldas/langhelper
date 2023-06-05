import csv
import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    if len(sys.argv) > 1:
        outputname = "index2.html"
    else:
        outputname = "index.html"
    print(f"Creating {outputname}.")

    output = []
    recent_output = []

    with open("swedish.csv") as csvfile:
        reader = csv.reader(csvfile)
        words = []
        result = {}
        for row in reader:
            word = row[0]
            word = word.strip()
            word = word.capitalize()
            words.append(word)
            tran = row[1]
            result[word] = tran

        recent = words.copy()
        recent.reverse()

        # For the index page
        words.sort()
        for word in words:
            filename = word.replace(" ", "_")
            fullname = f"{filename}.mp3"
            fullname = fullname.lower()
            tran = result[word]
            output.append((word.capitalize(), tran, fullname))

        for word in recent:
            filename = word.replace(" ", "_")
            fullname = f"{filename}.mp3"
            fullname = fullname.lower()
            tran = result[word]
            recent_output.append((word.capitalize(), tran, fullname))

    env = Environment(
        loader=FileSystemLoader("templates"), autoescape=select_autoescape()
    )

    template = env.get_template(f"{outputname}.j2")
    html = template.render(words=output)
    with open(outputname, "w") as fobj:
        fobj.write(html)

    template = env.get_template("recent.html.j2")
    html = template.render(words=recent_output)
    with open("recent.html", "w") as fobj:
        fobj.write(html)


if __name__ == "__main__":
    main()
