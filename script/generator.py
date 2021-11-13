import csv

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

print("Select CSV file")
csvPath = filedialog.askopenfilename()

outHTML = ""

def removeLastSpace(word):
    if word == "":
        return(word)
    elif word[-1] == " ":
        return(word[:-1])
    return(word)

def author_sorting(authors, corpAuthor):
    removeLastSpace(authors)
    removeLastSpace(corpAuthor)
    authorSector = ""
    if corpAuthor != "":
        authorSector = corpAuthor
    else:
        authors = authors.split(":")
        if len(authors) == 1:
            names = authors[0].split(" ")
            authorSector += names[-1] + ", " #Lastname
            for name in names[:-1]:
                authorSector += name[0] + "."
        else:
            for n, names in enumerate(authors):
                if n == 0:
                    pass
                elif n == len(authors)-1:
                    authorSector += ", and "
                else:
                    authorSector += ", "
                nameList = names.split(" ")
                authorSector+= nameList[-1] + ", " #Lastname
                for name in nameList[:-1]:
                    authorSector += name[0] + "."
    return (authorSector)

def year_sorting(yearData):
    removeLastSpace(yearData)
    if yearData == "":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!Year data is Missing")
    else:
        return(" (" + str(yearData) + "). ")

def title_sorting(titleData):
    removeLastSpace(titleData)
    if titleData == "":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!Title data is Missing")
    else:
        if titleData[-1] !=".":
            titleData += "."
        return(titleData)

def url_sorting(urlData):
    removeLastSpace(urlData)
    if urlData == "":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!URL data is Missing")
    else:
        if urlData[-1] !=".":
            urlData += "."
        return(" Available at " + urlData)

def accessed_sorting(day, month, year):
    for data in [day, month, year]:
        removeLastSpace(data)
    return(" Accessed " + day + " " + month + " " + year + ".")

def journal(dataRow):
    citationDetail = ""
    #Author
    citationDetail += str(author_sorting(dataRow["Author"], dataRow["Corporate Author"]))
    #Year #Must
    citationDetail += str(year_sorting(dataRow["Year"]))
    #Title #Must
    citationDetail += str(title_sorting(dataRow["Title"]))

    #Journal Name
    journalName = dataRow["Journal Name"]
    if journalName != "":
        citationDetail += "<em>" + journalName + "</em>, "
        #Volume
        volume = dataRow["Volume"]
        if volume != "":
            citationDetail += volume
        #Issue
        issue = dataRow["Issue"]
        if issue != "":
            citationDetail += "(" + issue + "),"
        #page
        page = dataRow["Pages"]
        if page != "":
            citationDetail += " pp. " + page +"."

    return ("<p>" + citationDetail + "</p>\n")

def website(dataRow):
    citationDetail = ""
    #Author
    citationDetail += str(author_sorting(dataRow["Author"], dataRow["Corporate Author"]))
    #Year #Must
    citationDetail += str(year_sorting(dataRow["Year"]))
    #Title #Must
    citationDetail += str(title_sorting(dataRow["Title"]))
    #URL #Must
    citationDetail += str(url_sorting(dataRow["URL"]))
    #Accessed date #Must
    citationDetail += str(accessed_sorting(dataRow["Day Accessed"],dataRow["Month Accessed"],dataRow["Year Accessed"]))
    return ("<p>" + citationDetail + "</p>\n")

with open(csvPath, newline = "",encoding="utf-8-sig") as csvfile:
    reference = csv.DictReader(csvfile)
    for row in reference:
        t = row["Type"]
        if t == "Journal":
            result = (journal(row))
        if t == "Website":
            result = (website(row))
        outHTML += str(result)

print("Select result exporting location")
htmlPath = filedialog.asksaveasfilename()
htmlPath = htmlPath+".html"

outHTML = sorted(outHTML)
with open(htmlPath, "w") as f:
    f.write(outHTML)
