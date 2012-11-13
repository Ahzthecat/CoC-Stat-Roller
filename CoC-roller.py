

##Cthulhu Character Generator
import random


## Defined functions are dice rolls, main generation script
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

    print"\n\n"

    print investigator,"has the following primary attributes.\n"

    strength=r3sixes()
    print investigator,"has a strength of",strength,"\n"

    con=r3sixes()
    print investigator,"has a constitution of",con,"\n"

    dex=r3sixes()
    print investigator,"has a dexterity of",dex,"\n"

    smarts=r2sixes6()
    print investigator,"has an intelligence of",smarts,"\n"

    app=r3sixes()
    print investigator,"has an appearance of",app,"\n"

    edu=r2sixes6()
    print investigator,"has an education of",edu+3,"\n"

    power=r3sixes()
    print investigator,"has a power of",power,"\n"

    size=r2sixes6()
    print investigator,"has a size of",size,"\n\n"

    raw_input("Press enter to derive the secondary attributes\n\n")

    ##derived attributes##

    print investigator,"has the following secondary attributes.\n"

    idea=smarts*5
    print investigator,"has an Idea score of",idea,"\n"

    know=edu*5+15
    print investigator,"has a Knowledge score of",know,"\n"

    luck=power*5
    print investigator,"has a Luck score of",luck,"\n"

    san=luck
    print investigator,"has a starting Sanity score of",san,"\n"

    ##Magic Points are equal to Power##
    print investigator,"has",power,"Magic points\n"

    hp=round((size+con)/2.0)
    print investigator,"has",hp,"hit points\n"

    db=strength+size
    if db>=2 and db<=12:
        print investigator,"has a damage bonus of",random.randint(-1,-6),"\n"
    elif db>=13 and db<=16:
        print investigator,"has a damage bonus of",random.randint(-1,-4),"\n"
    elif db>=17 and db<=24:
        print investigator,"has a damage bonus of 0\n"
    elif db>=25 and db<=32:
        print investigator,"has a damage bonus of",random.randint(1,4),"\n"
    elif db>=33 and db<=40:
        print investigator,"has a damage bonus of",random.randint(1,6),"\n"
    else:
        print "Something has gone awry.\n\n"

    occpts=edu*15
    print investigator,"has",occpts,"occupation building points\n"
    
    

def main():
    
    print investigator,"eh? An excellent name."
    job=raw_input("What occupation have you chosen?")
    go=raw_input("Shall we begin? (y/n)")
    while go.upper()=="Y":
        generator()
        print "\n\nWould you like to reroll",investigator,"the",job,"?"
        go=raw_input("Reroll? (y/n)")

def again():
        ##investigator=raw_input('What is this investigator\'s name?\n')
        main()



print"""
            ****************************
            **   The Call of Cthulhu  **
            **   Character Generator  **
            ****************************
            """

investigator=raw_input('What is your investigator\'s name?\n')
main()
print"\n\nWould you like to generate another character?"
newchar=raw_input("Generate? (Y/N):")
while newchar.upper()=="Y":
    investigator=raw_input('What is this investigator\'s name?\n')
    again()
    newchar=raw_input("\n\nWould you like to generate another character? (Y/N)")
    


   
    
print "\n\nThe Great Cthulhu awaits you."
raw_input("Press enter to venture forth into the darkness.")
