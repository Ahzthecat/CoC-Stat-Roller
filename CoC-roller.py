##Cthulhu Character Generator
import random



def sixsider():
    roll=random.randint(1,6)
    return roll

def r3sixes():
    total=sixsider()+sixsider()+sixsider()
    return total

def r2sixes6():
    total=sixsider()+sixsider()+6
    return total

def generator():

    print investigator,"has the following stats.\n"

    strength=r3sixes()
    print investigator,"has a strength of",strength,"\n"

    dex=r3sixes()
    print investigator,"has a dexterity of",dex,"\n"

    app=r3sixes()
    print investigator,"has an appearance of",app,"\n"

    edu=r2sixes6()
    print investigator,"has an education of",edu,"\n"

    power=r2sixes6()
    print investigator,"has a power of",power,"\n"

    size=r2sixes6()
    print investigator,"has a size of",size,"\n"

    

investigator=raw_input('What is your Investigator\'s name?\n')
print investigator,"eh? An excellent name."
go=raw_input("Shall we begin? (y/n)")
while go.upper()=="Y":
    print generator()
    print "\n\nAre these statistics satisfactory, or shall we reroll?"
    go=raw_input("Reroll? (y/n)")

print "\n\nThe Great Cthulhu awaits you,",investigator,"."
raw_input("Press enter to venture forth into the darkness.")

