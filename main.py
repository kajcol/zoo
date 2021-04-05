SUMMERMONTHS = ["04","05","06","07","08"]
class Animal:
 
    def __init__(self, name, hibernation, wake, sleep, feed ):
        self.name = name
        self.hibernation = hibernation
        self.wake = wake
        self.sleep = sleep 
        self.feed = feed

    def isInHibernation(self,date):
        return self.hibernation == dateIsInSummerOrWinter(date)

class Visit:
    def __init__(self, visitingDate, visitingHours):
        self.visitingDate = visitingDate
        visitStarts, visitEnds = visitingHours.split('-')
        
        #till int så att vi kan göra jämförelser        
        self.visitStarts = int(visitStarts)
        self.visitEnds = int(visitEnds)

#Funktion för att kolla om det är sommmar- eller vinter månad. 
def dateIsInSummerOrWinter(theDate):
    year, month, date = theDate.split('-')

    if month in SUMMERMONTHS: 
        return "Sommar"
    else: 
        return "Vinter"

#skapa en tom djurlista
theAnimalList = []

# Läs filen row by row
theFile = open("animalsfile.txt", "r")
for row in theFile:
    # för varje rad skapa djuret och lägg till i listan
    name, hibernate, wakehours, feed = row.split('/')
    wake, sleep = wakehours.split('-') 
    #Här skapar vi en Animal som vi direkt lägger till i listan   
    theAnimalList.append(Animal(name.strip(), hibernate.strip(), int(wake) ,int(sleep), int(feed.replace('\n', ''))))

visitingDate = input("Hej, vilket datum vill du besöka oss?(YYYY-MM-DD): ")
visitingHours = input("Mellan vilka tider(HH-HH): ")

#Skapa ett Visit objekt
myVisit = Visit(visitingDate, visitingHours)

# Rensa bort alla djuren som ligger i ide
for animal in theAnimalList:
    if animal.isInHibernation(visitingDate):
        theAnimalList.remove(animal)

# Skriv ut djuren
for animal in theAnimalList:
    print (animal.name)
    if((myVisit.visitStarts <= animal.feed) and (myVisit.visitEnds >= animal.feed)):
        print("som matas klockan:" + str(animal.feed))
