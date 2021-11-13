import csv

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

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
                authorSector += name[0].upper() + "."
        else:
            for n, names in enumerate(authors):
                if n == 0:
                    pass
                elif n == len(authors)-1:
                    authorSector += " and "
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

def book(dataRow):
    citationDetail = ""
    #Author
    citationDetail += str(author_sorting(dataRow["Author"], dataRow["Corporate Author"]))
    #Year #Must
    citationDetail += str(year_sorting(dataRow["Year"]))
    #Title #Must
    citationDetail += "<em>" + str(title_sorting(dataRow["Title"])) + "</em>"
    #Edition #Must
    edition = dataRow["Edition"]
    if edition != "":
        citationDetail += " " + edition + " ed"
    #Publisher #Must
    publisher = dataRow["Publisher"]
    if publisher != "":
        citationDetail += ", " + publisher
    #Publisher #Must
    city = dataRow["City"]
    if city != "":
        citationDetail += ", " + city + "."

    return ("<p>" + citationDetail + "</p>\n")

def exportHTML():
    print("Select CSV database file")
    csvPath = filedialog.askopenfilename()
    htmlList = []
    with open(csvPath,"r", newline = "",encoding="utf-8-sig") as csvfile:
        reference = csv.DictReader(csvfile)
        for row in reference:
            t = row["Type"]
            if t == "Journal":
                result = (journal(row))
            if t == "Website":
                result = (website(row))
            if t == "Book":
                result = (book(row))
            htmlList.append(str(result))

    htmlList = sorted(htmlList)
    print("Select result exporting location")
    htmlPath = filedialog.asksaveasfilename()
    if ".html" not in htmlPath:
        htmlPath = htmlPath+".html"
    outHTML = ""
    for h in htmlList:
        outHTML += str(h)

    with open(htmlPath, "w") as f:
        f.write(outHTML)

#---------------------------------------------
# Writing
#---------------------------------------------
def writecsv(dataDict):
    print("Select CSV database file")
    csvPath = filedialog.askopenfilename()
    with open(csvPath,"r", newline = "",encoding="utf-8-sig") as csvfile:
        fieldnames = csvfile.readline().split(",")
    with open(csvPath,"a", newline = "",encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(dataDict)

def add_author():
    authors = {}
    while 1:
        print("""Individual Author / Corporate Author
    1.Individual
    2.Corporate Author""")
        choice = input("Action Number: ")

        print("Author Name (FirstName MiddleName LastName)")
        name = input()
        if name != "":
            break

def add_journal():
    add_author()

def writePortal():
    while 1:
        try:
            print("""What type of document you want to add?
    1.Journal / Dissertation
    2.Website
    3.Book""")
            choice = int(input("Document Type Number: "))
            if choice == 1:
                add_journal()
                
            else:
                continue
            
            print("Do you want to add more? Y/N")
            more = input("Y/N? : ")
            if more == "Y":
                continue
            else:
                break
        except:
            print("Please only type in a number <--------------------------------------")
            continue

#---------------------------------------------
# Selection
#---------------------------------------------
def action():
    while 1:
        print("""State your business:
    1.Create new references (Not Finish yet)
    2.Export from existing database
        """
        )
        try:
            choice = int(input("Action number: "))
            if choice in range(1,3):
                return(choice)
                break
            else:
                continue
        except:
            print("Please only type in a number <--------------------------------------")
            continue

if __name__ == '__main__':
    choice = action()
    if choice == 2:
        exportHTML()
    elif choice == 1:
        writePortal()
