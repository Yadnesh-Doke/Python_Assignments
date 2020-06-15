import json
import sys
from collections import Counter
from bokeh.plotting import figure, show, output_file

file = "birthdays.json"
try:
    f = open(file)
except FileNotFoundError:
    print(f"No such file found named '{file}'")
    sys.exit(1)

birthday_dictionary = json.load(f)

months_dictionary = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []

for birth_date in birthday_dictionary.values():
    month = int(birth_date.split("/")[1])
    months.append(months_dictionary[month])


output_file("plot.html")
months_list = ["January","February","March","April","May","June",
                "July","August","September","October","November","December"]

x = []
y = []
for b_month in Counter(months):
     x.append(b_month)
     y.append(Counter(months)[b_month])

p = figure(x_range = months_list)
p.vbar(x=x, top=y, width=0.5)

show(p)
