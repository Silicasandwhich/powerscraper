import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as file:
    html_lines = file.readlines()

html_string = "".join(html_lines)

csv = ""

parsed_html = BeautifulSoup(html_string)
for tag in parsed_html.body.div.table.tbody.find_all("tr")[3].td.table.tbody.find_all(
    "tr"
):
    for data in tag.find_all("td"):
        csv += f'"{data.string.strip()}",'
    csv += "\n"
csv = csv.replace("\n                     ", "")
print(csv)

with open("output.csv", "w") as file:
    file.write(csv)
