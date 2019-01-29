# Donation Thank You Note

[![Build status](https://ci.appveyor.com/api/projects/status/yrco52v0ay9t50a0?svg=true)](https://ci.appveyor.com/project/lcamichigan/donation-thank-you-note)
[![Build Status](https://travis-ci.org/lcamichigan/donation-thank-you-note.svg?branch=master)](https://travis-ci.org/lcamichigan/donation-thank-you-note)

This is a collection of resources for creating thank you notes for donations to
[Sigma Alumni Association](https://lcamichigan.com).

## Contents

* [Getting Started](#getting-started)
  * [On Windows](#on-windows)
  * [On macOS](#on-macos)
* [How to Make Thank You Notes](#how-to-make-thank-you-notes)
  * [Before Making Thank You Notes for the First Time…](#before-making-thank-you-notes-for-the-first-time)
  * [Update info\.json](#update-infojson)
  * [Update donations\.csv](#update-donationscsv)
  * [Make Thank You Notes](#make-thank-you-notes)

## Getting Started

To make thank you notes, you need [LuaTeX](http://www.luatex.org), the
[cross-and-crescent](https://github.com/lcamichigan/cross-and-crescent)
LaTeX package, [Python](https://www.python.org), and
[Ghostscript](https://www.ghostscript.com). All of these are free and
cross-platform. You also need the OpenType versions of the fonts
[Linux Libertine](http://libertine-fonts.org) and
[Gillius](http://arkandis.tuxfamily.org/adffonts.html). These are also free, and
you’ll get them automatically when you install LuaTeX.

You don’t need to do any TeX or Python programming to make thank you notes.
However, you should be familiar with entering commands in PowerShell or Command
Prompt on Windows, or in Terminal on macOS. It’ll also be helpful to have some
exposure to [JSON](https://en.wikipedia.org/wiki/JSON), but this isn’t
essential.

### On Windows

The most reliable way to install LuaTeX is probably to install
[TeX Live](https://www.tug.org/texlive/). To install TeX Live, visit
https://www.tug.org/texlive/acquire-netinstall.html, and then download and run
install-tl-windows.exe. Note that installing TeX Live can take a few hours.

To install the cross-and-crescent package, follow the instructions at
https://github.com/lcamichigan/cross-and-crescent#installing.

To install Python, visit https://www.python.org/downloads/windows/, and then
download and run an installer for the latest release of Python 2 or 3 (you can
use either version). Make sure you add python.exe to your Windows PATH when you
install Python.

To install Ghostscript, visit https://www.ghostscript.com/download/gsdnld.html,
and then download and run an installer for the latest release of Ghostscript.

To view thank you notes, you need a PDF viewer. On Windows 10, you can view PDF
files in the built-in
[Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge)
browser. On Windows 7 and later, you can use
[Adobe Acrobat Reader](https://get.adobe.com/reader/) or
[Google Chrome](https://www.google.com/chrome/).

### On macOS

The easiest way to install LuaTeX is probably to install
[MacTeX](https://www.tug.org/mactex/). To install MacTeX, visit
https://tug.org/mactex/mactex-download.html, download MacTeX.pkg, and then
double-click MacTeX.pkg.

To install the cross-and-crescent package, follow the instructions at
https://github.com/lcamichigan/cross-and-crescent#installing.

The easiest way to install Ghostscript is probably through
[Homebrew](https://brew.sh). To install Homebrew, follow the instructions at
https://brew.sh. After you install Homebrew, enter `brew install ghostscript` in
Terminal.

Python is included with macOS.

## How to Make Thank You Notes

First, download this repository as a ZIP archive. To do this, click
[here](https://github.com/lcamichigan/donation-thank-you-note/archive/master.zip).
Unzip the archive wherever you wish.

To make thank you notes, you enter commands in PowerShell or Command Prompt on
Windows, or in Terminal on macOS. Open PowerShell or Command Prompt on Windows,
or Terminal on macOS, and then `cd` to the folder you just unzipped.

### Before Making Thank You Notes for the First Time…

If you’re making thank you notes for the first time, enter:

```sh
python init.py
```

This runs the Python script [init.py](init.py). This script creates an info.json
file and a donations.csv file.

Now, enter:

```sh
python make_notes.py
```

This will create (in a folder named “notes”) PDF files of thank you notes using
the information in info.json and donations.csv. You’ll see placeholder
information in the thank you notes. You must update info.json and donations.csv
with information about the notes you’re making.

### Update info.json

Open info.json in a text editor (you can use Notepad on Windows or TextEdit on
macOS). The contents of info.json will be something like:

```json
{
    "Sigma address": [
        "123 Main St",
        "Anywhere MI 00000-0000"
    ],
    "Event name": "Founders Day Brunch",
    "Event date and time": "2018-03-24 11:00"
}
```

Most of info.json is arranged like

```json
"⟨key⟩": "⟨value⟩"
```

You should edit only the values, not the keys. For example, if the next alumni
event is Homecoming, change

```json
"Event name": "Founders Day Brunch"
```

to

```json
"Event name": "Homecoming Brunch"
```

The event date is formatted as YYYY-MM-DD hh:mm.

### Update donations.csv

You can open and edit donations.csv in many applications for working with
spreadsheets, including
[Microsoft Excel](https://products.office.com/en-us/excel),
[Apple Numbers](https://www.apple.com/numbers/), and
[Google Sheets](https://www.google.com/sheets/about/). You can also open
donations.csv in any text editor.

By default, donations.csv contains data like this:

Display name         | Last name | Street  | City  | State  | ZIP  | Amount | Scholarships only
---------------------|-----------|---------|-------|--------|------|--------|------------------
FirstName1 LastName1 | LastName1 | Street1 | City1 | State1 | ZIP1 | 100    | FALSE
FirstName2 LastName2 | LastName2 | Street2 | City2 | State2 | ZIP2 | 200    | TRUE

Replace the default data with information about donations.

### Make Thank You Notes

To make thank you notes, enter:

```sh
python make_notes.py
```

It’s often convenient to combine several thank you notes into one PDF file, and
you can do this with Ghostscript.

To combine thank you notes into a PDF file named Notes.pdf on Windows, enter in
PowerShell:

```powershell
gswin64c -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile='Notes.pdf' $(foreach ($file in Get-ChildItem notes\*.pdf) { 'notes\' + $file.Name })
```

or in Command Prompt:

```batch
if exist filenames.txt del filenames.txt
for %G in (notes\*.pdf) do @echo %G >> filenames.txt
gswin64c -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=Notes.pdf @filenames.txt
```

If you see an error that `gswin64c` can’t be found, then you need to replace
`gswin64c` with its absolute path. This will usually be something like
`"C:\Program Files\gs\gs#.##\bin\gswin64c"`, where `#.##` is Ghostscript’s
version. In PowerShell, precede the absolute path of `gswin64c` by a call
operator
([`&`](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_operators?view=powershell-6#call-operator-)).

To combine thank you notes into a PDF file named Notes.pdf on macOS, enter in
Terminal:

```sh
gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=Notes.pdf notes/*.pdf
```
