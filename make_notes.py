#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
from datetime import datetime
import json
import os
import re
import shutil
import subprocess


parser = argparse.ArgumentParser(description="Make donation thank you notes.")
parser.add_argument(
    "-j", "--join", action="store_true", help="combine output into one pdf"
)
parser.add_argument(
    "csv_path",
    nargs="?",
    default="donations.csv",
    help="path to CSV file of donations (default: %(default)s)",
)
args = parser.parse_args()

directory_name = "notes"
if os.path.exists(directory_name):
    shutil.rmtree(directory_name)
os.makedirs(directory_name)

with open("info.json") as file:
    info = json.load(file)

today = datetime.today()
event_date = datetime.strptime(info["Event date and time"], "%Y-%m-%d %H:%M")
assert today < event_date, "Event date and time in info.json must be in the future"

with open(os.path.join("support", "note-info.tex"), "w") as file:
    file.write("\\newcommand\\SigmaStreet{{{}}}\n".format(info["Sigma address"][0]))
    file.write(
        "\\newcommand\\SigmaCityStateAndZIP{{{}}}\n".format(info["Sigma address"][1])
    )
    file.write("\\newcommand\\eventName{{{}}}\n".format(info["Event name"]))
    date_format = "{date:%A}, {date:%B} {date.day}"
    if event_date.year != today.year:
        date_format += ", {date.year}"
    date_format += " at {date.hour}"
    if event_date.minute > 0:
        date_format += ":{date:%M}"
    else:
        # U+2019 is the code point of ’, a right single quotation mark. Use the
        # code point instead of a literal ’ to avoid text encoding issues with
        # Python 3 on Windows.
        date_format += ' o\\char"2019clock'
    file.write("\\newcommand\\eventDate{" + date_format.format(date=event_date) + "}\n")

generated_files = []

with open(args.csv_path) as file:
    note_number = 0
    for row in csv.DictReader(file):
        with open(os.path.join("support", "donor-info.tex"), "w") as file:
            file.write(
                "\\newcommand\\donorDisplayName{{{}}}\n".format(
                    row["Display name"].strip()
                )
            )
            file.write(
                "\\newcommand\\donorLastName{{{}}}\n".format(row["Last name"].strip())
            )
            file.write(
                "\\newcommand\\donorStreet{{{}}}\n".format(
                    re.sub(
                        r"\n|\r\n?", r"\\\\", row["Street"].strip(), flags=re.MULTILINE
                    ).upper()
                )
            )
            file.write("\\newcommand\\donorCity{{{}}}\n".format(row["City"].strip()))
            file.write("\\newcommand\\donorState{{{}}}\n".format(row["State"].strip()))
            file.write("\\newcommand\\donorZIP{{{}}}\n".format(row["ZIP"].strip()))
            file.write(
                "\\newcommand\\donationAmount{{\\${}}}\n".format(
                    re.sub(r"\.0*$", "", "{:,.2f}".format(float(row["Amount"])))
                )
            )
            file.write("\\newcommand\\donationMessage{")
            if row["Anonymous"] == "TRUE":
                file.write("As requested, your gift will remain anonymous. ")
            if row["Scholarships only"] == "TRUE":
                file.write("We will use your gift to provide scholarships")
            else:
                file.write(
                    "We will use your gift to provide the best possible Fraternal experience"
                )
            file.write("}\n")

        note_number += 1
        subprocess.check_call(
            [
                "lualatex",
                "-jobname=Note{}".format(note_number),
                "-interaction=batchmode",
                "-output-directory=" + directory_name,
                "Note.tex",
            ]
        )

        generated_files.append(directory_name + "/Note{}.pdf".format(note_number))

    if args.join:
        subprocess.check_call(
            ["pdfjoin", "--outfile", directory_name + "/Joined.pdf"] + generated_files
        )
