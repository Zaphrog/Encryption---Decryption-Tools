import random
random.seed ()
def modifier (x):
    if x == 1:
        modifier = -5
    elif x == 2:
         modifier = -4
    elif x == 3:
        modifier = -4
    elif x == 4 :
        modifier = -3
    elif x == 5:
        modifier = -3
    elif x == 6:
        modifier = -2
    elif x == 7 :
        modifier  = -2
    elif x == 8:
        modifier = -1
    elif x == 9:
        modifier = -1
    elif x == 10:
        modifier = 0
    elif x == 11:
        modifier = 0
    elif x == 12:
        modifier = 1
    elif x == 13:
        modifier = 1
    elif x == 14:
         modifier = 2
    elif x == 15:
        modifier = 2
    elif x == 16 :
        modifier = 3
    elif x == 17:
        modifier = 3
    elif x == 18:
        modifier = 4
    elif x == 19 :
        modifier  = 4
    else:
        modifier = 5
    print ("Your modifier for the previous is ", modifier)
print ("Write your Character's name")
name = input()
print ("Your Character is ",name)

print ("ABILITY SCORES AND MODIFIERS")
x = random.randint (1,20)
print (name,"'s Strength will be ", x)
modifier (x)
STR = x

x = random.randint (1,20)
print (name,"'s Dexterity will be ", x)
modifier (x)
DEX = x

x = random.randint (1,20)
print (name,"'s Constitution will be ", x)
modifier (x)
CON = x

x = random.randint (1,20)
print (name,"'s Intelligence will be ", x)
modifier (x)
INT = x

x = random.randint (1,20)
print (name,"'s Wisdom will be ", x)
modifier (x)
WIS = x

x = random.randint (1,20)
print (name,"'s Charisma will be ", x)
modifier (x)
CHA = x


print ("RACE")
def CHOOSERACE ():
    while True:
        print ("Choose your Race")
        race = input ()
        if race =="Hill Dwarf":
            print ("Your new Constitution is ", CON + 2 ," Your new Wisdom is ", WIS + 1 )
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Dwarvish features and measures are: You live for 350 years tops. Your speed is 25. You reach adulthood at 50. You are Good. You are Medium. You can speak and write Common and Dwarvish")
            print ("You have Darkvision, Dwarven Resiliance . You have Stonecunning. You have Dwarven Toughness.")
            print ("You have proficiency with battleaxe, lightaxe, light hammer, warhammer and you can choose proficiency between smith, brewer or mason's tools.")

        elif race == "Mountain Dwarf":
            print ("Your new Constitution is ", CON + 2 ," Your new Strength is ", STR + 1 )
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Dwarvish measures are: You live for 350 years tops. You reach adulthood at 50. Your speed is 25. You are Good. You are Medium. You can speak and write Common and Dwarvish")
            print ("You have Darkvision, Dwarven Resiliance and Stonecunning.")
            print ("You have proficiency with battleaxe, lightaxe, light hammer, warhammer, light and medium armor and you can choose proficiency between smith, brewer or mason's tools.")

        elif race == "High Elf":
            print ("Your new Dexterity is ", DEX + 2 ," Your new Intelligence is ", INT + 1 )
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Elvish features and measures are: You live for 750 years tops. Your speed is 30. You reach adulthood at 100. You are Good. You are Medium. You can speak and write Common and Elvish")
            print ("You have Darkvision, Fey Ancestry, Trance, a Cantrip from the wizard spell list, (Spellcasting ability is INT) and an Extra Language of your choice")
            print ("You have proficiency with the perception skill")

        elif race == "Wood Elf":
            print ("Your new Dexterity is ", DEX + 2 ," Your new Wisdom is ", WIS + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Elvish features and measures are: You live for 750 years tops. You reach adulthood at 100. You are Good. You are Medium. You can speak and write Common and Elvish")
            print ("You have Darkvision, Fey Ancestry, Trance, Fleet of Foot and Mask of the Wild.")
            print ("You have proficiency with the perception skill, longsword, shortsword, shortbow and longbow.")

        elif race == "Drow":
            print ("Your new Dexterity is ", DEX + 2 ," Your new Charisma is ", CHA + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Elvish features and measures are: You live for 750 years tops. You reach adulthood at 100. You are Evil. You are Medium. You can speak and write Common and Elvish")
            print ("You have Superior Darkvision, Sunlight Sensitivity, Fey Ancestry, Trance.")
            print ("You know the dancing lights cantrip, when you reach 3rd level you can cast faerie fire and when you reach 5th level you can cast darkness. Spellcasting ability (CHA)")
            print ("You have proficiency with the perception skill, rapiers, shortswords and hand crossbows")

        elif race == "Lightfoot Halfling":
            print ("Your new Dexterity is ", DEX + 2 ," Your new Charisma is ", CHA + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Halfling features and measures are: You live for 250 years tops. You reach adulthood at 20. You may be Lawful Good. You are Small. You can speak, read and write Common and Halfling")
            print ("You are Lucky, Brave, Naturally Stealthy and have Halfling Nimbleness")
            print ("You have no current proficiencies")

        elif race == "Stout Halfling":
            print ("Your new Dexterity is ", DEX + 2 ," Your new Constitution is ", CON + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Halfling features and measures are: You live for 250 years tops. You reach adulthood at 20. You may be Lawful Good. You are Small. You can speak, read and write Common and Halfling")
            print ("You are Lucky, Brave, have Halfling Nimbleness and Stout Resilience")
            print ("You have no current proficiencies")

        elif race == "Human":
            print ("Your new values are (in order):", STR + 1, DEX + 1, CON + 1, INT + 1, WIS + 1, CHA + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Human features and measures are: You live for 100 years tops. You reach adulthood at 20. You have no alignment as human. You are Medium. You can speak and write Common and one of your choice")
            print ("You have no otherworldly features")
            print ("You have no current proficiencies")

        elif race == "Dragonborn":
            print ("Your new Strength is ", STR + 2 ," Your new Charisma is ", CHA + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Draconic features and measures are: You live for 80 years tops. You reach adulthood at 15. Your alignment tends to be extreme (usually good). You are Medium. You can speak and write Common and Draconic")
            print ("You have Draconic Ancestry of your choice, you also have a Breath Weapon and Resistance that your Ancestry indicates")
            print ("You have no current proficiencies")

        elif race== "Forest Gnome":
            print ("Your new Intelligence is ", INT + 2, "Your new Dexterity is ", DEX + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Gnomish features and measures are: You live for 500 years tops. You reach adulthood at 40. Your alignment tends to be Good. You are Small. You can speak and write Common and Gnomish")
            print ("You have Darkvision, Gnome Cunning and can Speak with Small Beasts. You know the minor illusion cantrip (Spellcasting ability INT)")
            print ("You have no current proficiencies")

        elif race== "Rock Gnome":
            print ("Your new Intelligence is ", INT + 2, "Your new Constitution is ", CON + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Gnomish features and measures are: You live for 500 years tops. You reach adulthood at 40. Your alignment tends to be Good. You are Small. You can speak and write Common and Gnomish")
            print ("You have Darkvision, Gnome Cunning and Tinker ")
            print ("You have proficiency with artisan's tools")

        elif race == "Half-Elf":
            print ("Your new Charisma is ", CHA + 2, "You can add 1 to two ability scores of your choice")
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Half-Elvish features and measures are: You live for 200 years tops. You reach adulthood at 20. Your alignment tends to be Chaotic. You are Medium. You can speak and write Common, Elvish and one of your choice")
            print ("You have Darkvision and Fey Ancestry")
            print ("You have proficiency with two skills of your choice")

        elif race == "Half Orc":
            print ("Your new Strength is ", STR + 2, "Your new Constitution is", CON + 1)
            print ("Change your modifiers ( if your new number is even or your old number was odd, add 1")
            print ("Your Half-Orc features and measures are: You live for 75 years tops. You reach adulthood at 14. Your alignment tends to be Chaotic. You are Medium. You can speak and write Common and Orc")
            print ("You have Darkvision, Relentless Endurance and Savage Attacks")
            print ("You have proficiency with the Intimidation Skill")

        elif race == "Tiefling":
            print ("Your new Charisma is ", CHA + 2, "Your new Intelligence is", INT + 1)
            print ("Change your modifiers (if your new number is even or your old number was odd, add 1")
            print ("Your Tiefling features and measures are: You live for 100 years tops. You reach adulthood at 20. Your alignment tends to be Evil. You are Medium. You can speak and write Common and Infernal")
            print ("You have Darkvision")
            print ("You know the thaumaturgy cantrip, you can cast hellish rebuke as a 2nd level spell at 3rd level and you can cast darkness at 5th level")
            print ("You have no current proficiencies")

        else:
            print ("Specify the Subrace or make sure you are spelling correctly")
            continue
        return

CHOOSERACE ()


print ("CLASS")
if STR >= 13:
    print ("Your suggested classes based on your Strength are Barbarian or Fighter")
if DEX >= 13:
    print ("Your suggested classes based on your Dexterity are Fighter or Rogue")
if INT >= 13:
    print ("Your suggested class based on your Intelligence is Wizard")
if CHA >= 13:
    print ("Your suggested classes based on your Charisma are Bard, Sorcerer or Warlock")
if WIS >= 13:
    print ("Your suggested classes based on your wisdom are Cleric or Druid")
if DEX + WIS >= 26:
    print ("Your suggested classes based on your Dexterity and Wisdom are Monk or Ranger")
if STR + CHA >= 26:
    print ("You suggested class based on your Strength and Charisma is Paladin")
if STR<13 and DEX<13 and INT<13 and CHA<13 and WIS<13:
    print ("Your Character is too bad at everything. I would start again.")



print ("Write your class (See recommendation above)")
def CHOOSECLASS ():
    while True:    
        CLASS = input ()
        if CLASS == "Barbarian":
            print ("You have 1d12 Hit die per Barbarian level, you have 12 + your CONmod hitpoints")
            print (" Proficiency bonus: +2. Your proficiencies are: Light and Medium Armor, Shields, simple and martial weapons, Strength and Constitution saving throws")
            print ("You can choose two skills between Animal Handling, Athletics, Intimidation, Nature, Perception and Survival")
            print ("Your features are Rage (2 Rages, +2 Rage Damage) and Unarmored Defense")
            print ("Your equipment is: an explorer's pack, four javelins you can choose between (a) a greataxe or (b) any martial weapon. Choose")
            option = input ()
            if option == "a":
                print ("1d12 Slashing, Heavy and two handed")
            elif option == "b":
                print ("Choose from the table")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) two handaxes or (b) any simple weapon")
            option == input ()
            if option == "a":
                print ("1d6 Slashing, light and thrown")
            elif option == "b":
                print ("Choose from the table")
            else:
                print ("Choose an option")



        elif CLASS == "Bard":
            print ("You have 1d8 Hit die par Bard level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Light Armor, simple weapons, Hand Crossbows, longswords, rapiers, shortswords, you can choose 3 musical intruments and Dexterity and Charisma saving throws")
            print ("You can choose any three skills")
            print ("Your feature is  Bardic Inspiration")
            print ("You know the Dancing Lights and Vicious Mockery cantrips along with the 1st level spells: Charm Person, Detect Magic, Healing Word and Thunderwave.")
            print ("You have two first level Spell Slots, Charisma is your Spellcasting ability, your Spell save DC is 8+proficiency bonus+CHAmod. Your spell attack modifier is proficiency bonus+CHAmod")
            print ("Your equipment is: leather armor, dagger, you can choose between (a) a rapier , (b) any simple weapon or (c) a longsword. Choose")
            option = input ()
            if option == "a":
                print ("1d8 Piercing, Finesse")
            elif option == "b":
                print ("Choose from the table")
            elif option == "c":
                print ("1d8 Slashing, Versatile (1d10)")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) a diplomat's pack or (b) an entertainer's pack")



        elif CLASS == "Cleric":
            print ("You have 1d8 Hit die per Cleric level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Light and Medium Armor, shields, simple weapons and Wisdom and Charisma saving throws")
            print ("You can choose two from History, Insight, Medicine, Persuasion and Religion")
            print ("Your feature is  Divine Domain")
            print ("You know three cantrips of the Cleric spell list along with a number of 1st level spells equal to your WISmod + Cleric lvl.")
            print ("You have two first level Spell Slots, WIS is your Spellcasting ability, your Spell save DC is 8+proficiency bonus+WISmod. Your spell attack modifier is proficiency bonus+WISmod")
            print ("Your equipment is: shield, holy symbol, you can choose between (a) a mace or (b) a warhammer (if proficient). Choose")
            option = input ()
            if option == "a":
                print ("1d6 Bludgeoning, -")
            elif option == "b":
                print ("1d8 Bludgeoning, Versatile (1d10)")
            elif option == "c":
                print ("1d8 Slashing, Versatile (1d10)")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) a scale mail, (b) a leather armor and (c) a chain mail (if proficient)")
            option = input ()
            if option == "a":
                print ("14 + DEXmod, Stealth Disadvantage")
            elif option == "b":
                print ("11 + DEXmod, No Disadvantage")
            elif option == "c":
                print ("STR 13, 16, Stealth Disadvantage")
            else:
                print ("Choose an option")
            print ("You can choose between (a) a light crossbow with 20 bolts or (b) any simple weapon")
            option = input ()
            if option == "a":
                print ("1d8 piercing, loaded, two handed")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")

            print ("You can choose between  a priest's pack or an explorer's pack")



        elif CLASS == "Druid":
            print ("You have 1d8 Hit die per Druid level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Light and Medium Armor, shields, herbalism kit, club, dagger, dart, javelin, mace, quarterstaff, sickle, scimitars, slings, spears and Wisdom and Intelligence saving throws")
            print ("You can choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion and Survival")
            print ("Your feature is  Druidic. Druids won't wear armors or shields made of metal")
            print ("You know two cantrips of the Druid spell list and yo can prepare a number of 1st level spells equal to your WISmod + Druid lvl.")
            print ("You have two first level Spell Slots, WIS is your Spellcasting ability, your Spell save DC is 8+proficiency bonus+WISmod. Your spell attack modifier is proficiency bonus+WISmod")
            print ("Your equipment is: leather armor, an explorer's pack, a druidic focus of your choice, you can choose between (a) a wooden shield and (b) any simple weapon. Choose")
            option = input ()
            if option == "a":
                print ("+2")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")

            print ("You can choose between (a) a scimitar and (b) any simple melee weapon.")
            option = input ()
            if option == "a":
                print ("1d6 slashing, finesse, light")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")



        elif CLASS == "Fighter":
            print ("You have 1d10 Hit die per Fighter level, you have 10 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: All Armors and Shields, simple and martial weapons and Strength and Constitution saving throws")
            print ("You can choose two from  Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception and Survival ")
            print ("Your features are Second Wind and you can choose a Fighting Style between (a) Archery, (b) Defense, (c) Dueling, (d) Great Weapon Fighting, (e) Protection and (f) Two Weapon Fighting.")
            option = input ()
            if option == "a":
                print ("Gain +2 bonus to attack rolls with ranged weapons")
            elif option == "b":
                print ("You gain + 1 AC when wearing armor")
            elif option == "c":
                print ("When wielding a melee weapon in one hand and no other weapon, you gain a +2 bonus on damage rolls")
            elif option == "d":
                print ("If you roll a 1 on a damage die when using a two handed or versatile weapon, you can reroll and have to keep the new roll, regardless the result")
            elif option == "e":
                print ("When a creature attacks a target other than you within 5ft of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield")
            elif option == "f":
                print ("When you engade in two weapon fighting, you can add your ability modifier to the second damage roll")
            else:
                print ("Choose an option")
            print ("Your equipment is: (a) a chain mail or (b) a leather armor, longbow and 20 arrows. Choose")
            option = input ()
            if option == "a":
                print ("16, Str 13, Disadvantage")
            elif option == "b":
                print ("11+DEXmod. 1d8 Piercing, heavy, Two Handed")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) a martial weapon and a shield and (b) two martial weapons")
            option = input ()
            if option == "a":
                print ("Choose from table. +2")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) a light crossbow and 20 bolts and (b) two handaxes")
            option = input ()
            if option == "a":
                print ("1d8 Piercing, Loading, two handed")
            elif option == "b":
                print ("1d6 Slashing, Light, thrown")
            else:
                print ("Choose an option")
            print ("You can also choose between a dungeoneer's pack and an explorer's pack")



        elif CLASS == "Monk":
            print ("You have 1d8 Hit die per Monk level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Simple Weapons, shortswords and Strength and Dexterity saving throws")
            print ("You can choose two from Acrobatics, Athletics, Insight, Religion and Stealth")
            print ("Your features are Unarmored Defense and Martial Arts")
            print ("Your equipment is: 10 darts, you can choose between (a) a shortsword and (b) any simple weapon. Choose")
            option = input ()
            if option == "a":
                print ("1d6, finesse, light")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can choose between a dungeoneer's pack or an explorer's pack")



        elif CLASS == "Paladin":
            print ("You have 1d10 Hit die per Paladin level, you have 10 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Simple Weapons, martial weapons, all armor, shields and Wisdom and Charisma saving throws")
            print ("You can choose two from Athletics, Insight, Intimidation, Medicine, Persuasion and Religion")
            print ("Your features are Divine Sense and Lay on Hands")
            print ("Your equipment is: chain mail (16, STR 13), a holy symbol, you can choose between (a) a martial weapon and a shield or  (b) two martial weapons. Choose")
            option = input ()
            if option == "a":
                print ("Choose from the table, +2)")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can also choose between (a) 5 javelins or (b) any simple weapons")
            option = input ()
            if option == "a":
                print ("1d6 Piercing, Thrown")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can choose between an explorer's pack or a priest's pack")



        elif CLASS == "Ranger":
            print ("You have 1d10 Hit die per Ranger level, you have 10 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Simple Weapons, martial weapons, Light and Medium Armor, shields and Strength and Dexterity saving throws")
            print ("You can choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth and Survival")
            print ("Your features are Favored Enemy and Natural Explorer")
            print ("Your equipment is: longbow and quiver with 20 arrows, you can choose between (a) a scale mail or  (b) a leather armor weapons. Choose")
            option = input ()
            if option == "a":
                print ("14 + DEXmod, Disadvantage")
            elif option == "b":
                print ("11 + DEXmod")
            else:
                print ("Choose an option")
            print ("You can choose between (a) two shortswords or (b) two simple melee weapons")
            option = input ()
            if option == "a":
                print ("1d6, Finesse, light")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can choose between an explorer's pack or a dungeoneer's pack")



        elif CLASS == "Rogue":
            print ("You have 1d8 Hit die per Rogue level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Simple Weapons, hand crossbows, longswords, rapiers, shortswords, Light Armor, Thieve's tools and Intelligence and Dexterity saving throws")
            print ("You can choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Sleight of Hand and Stealth")
            print ("Your features are Expertise, Sneak Attack (1d6) and Thieve's Cant")
            print ("Your equipment is: leather armor, two daggers, thieve's tools, you can choose between (a) a rapier or  (b) a shortsword. Choose")
            option = input ()
            if option == "a":
                print ("1d8 Piercing, Finesse")
            elif option == "b":
                print ("1d6 Piercing, Finesse, light")
            else:
                print ("Choose an option")
            print ("You can choose between (a) a shortbow and quiver of 20 arrows or (b) a shortsword")
            option = input ()
            if option == "a":
                print ("1d6 Piercing, Two Handed")
            elif option == "b":
                print ("1d6 Piercing, Finesse, light")
            else:
                print ("Choose an option")
            print ("You can choose between a burglar's pack, a dungeoneer's pack or an explorer's pack")



        elif CLASS == "Sorcerer":
            print ("You have 1d6 Hit die per Sorcerer level, you have 6 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Dagger, darts, slings, quarterstaff, light crossbow and Constitution and Charisma saving throws")
            print ("You can choose two from Arcana, Deception, Insight, Intimidation, Persuasion and Religion")
            print ("Your feature is Sorcerous Origin: Choose between (a), Draconic Bloodline or (b) Wild Magic")
            option = input ()
            if option == "a":
                print ("Your magic comes from draconic magic that flows in your blood. You can choose a type of draconic ancestry. Your hit point maximum increases by 1 and you AC without Armor is 13 + DEXmod")
            elif option == "b":
                print ("Your magic comes from the forces of Chaos which underlie the order of creation. Once per turn, the DM can have you roll a d20. If you roll a 1, you can roll on the Magic Surge table. ")
            else:
                print ("Choose an option")
            print ("You know 4 cantrips from the Sorcerer spell list. You know two 1st level Spells and have two 1st level Spell Slots")
            print (" CHA is your Spellcasting ability. Ypur Spell save DC is 8 + proficiency bonus + CHAmod. Your spell attack mod is your poficiency bonus + CHAmod")
            print ("Your equipment is: two daggers, you can choose between (a) a light crossbow with 20 bolts or  (b) a any simple weapon. Choose")
            option = input ()
            if option == "a":
                print ("1d8 Piercing, loading, two handed")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can choose between a component pouch or an arcane focus")
            print ("You can choose between a dungeoneer's pack or an explorer's pack")



        elif CLASS == "Warlock":
            print ("You have 1d8 Hit die per Warlock level, you have 8 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: Light Armor, simple weapons and Wisdom and Charisma saving throws")
            print ("You can choose two from Arcana, Deception, History, Intimidation, Investigation, Nature and Religion")
            print ("Your feature is Otherworldly Patron: Choose between (a) The Archfey, (b) The Fiend or (c) The Great Old One")
            option = input ()
            if option == "a":
                print ("Your patron is a lord or lady of the Fey.The Archfey lets you choose from an expanded spell list. The following are added to your spell list at 1st level: faerie fire and sleep.")
                print ("At you turn, you can cause each creature within a 10 foot cube from  you  to make a Wisdom saving throw against your spell save DC. The creatures that fail are either charmed or frightened (your choice)")
            elif option == "b":
                print ("Your patron is a fiend form the lower plains of existence. At 1st level you know the additional spells: burning hands and command.")
                print ("When you reduce a creature to 0 hitpoins, you gain temporary hitpoints equal to your CHAmod + your warlock level")
            elif option == "c":
                print ("Your patron is a mysterious entity. At 1st level you know the additional spells dissonant whispers and Tasha's hideous laughter")
                print ("You can telepathically speak to any creature within 30ft of you. The creature must know at least 1 language")        
            else:
                print ("Choose an option")
            print ("You know 2 cantrips from the Warlock spell list. You know two 1st level Spells and have 1 1st level Spell Slot")
            print ("CHA is your Spellcasting ability. Your Spell save DC is 8 + proficiency bonus + CHAmod. Your spell attack mod is your poficiency bonus + CHAmod")
            print ("Your equipment is: A Leather Armor, any simple weapon, two daggers, you can choose between (a) a light crossbow with 20 bolts or (b) any simple weapon")
            option = input ()
            if option == "a":
                print ("1d8 Piercing, loading, two handed")
            elif option == "b":
                print ("Choose from table")
            else:
                print ("Choose an option")
            print ("You can choose between a component pouch or an arcane focus")
            print ("You can choose between a scholar's pack or a dungeoneer's pack")



        elif CLASS == "Wizard":
            print ("You have 1d6 Hit die per Wizard level, you have 6 + your CONmod hitpoints")
            print ("Proficiency bonus: +2. Your proficiencies are: darts, slings, quarterstaffs, light crossbows and Wisdom and Intelligence saving throws")
            print ("You can choose two from Arcana, History, Insight, Investigation, Medicine and Religion")
            print ("Your feature is Arcane Recovery")
            print ("You know the Mage Hand, Light and Ray of Frost cantrips and you can prepare a number of 1st level Spells which equals your INTmod+ Wizard lvl. You have 2 1st level Spell Slots.")
            print ("Your spellbook has currently 6 spells")
            print ("INT is your Spellcasting ability. Your Spell save DC is 8 + proficiency bonus + INTmod. Your spell attack mod is your poficiency bonus + INTmod")
            print ("Your equipment is: a spellbook, you can choose between (a) a quarterstaff or (b) a dagger. Choose")
            option = input ()
            if option == "a":
                print ("1d6 Bludgeoning, Versatile (1d8)")
            elif option == "b":
                print ("1d4 Piecing, Finesse, light, thrown")
            else:
                print ("Choose an option")
            print ("You can choose between acomponent pouch or an arcane focus. You can also choose between an explorer's pack or a scholar's pack")
        else:
            print ("Write a valid class")
            continue
        return
    
CHOOSECLASS ()

print ("ARMOR CLASS")
print ("Unless your Character has the Unarmored Defense feature, its Armor Class when not wearing Armor or shields is 10+ DEXmod")



print ("BACKGROUND")

def BACKGROUND ():
    while True:
        CLASS = input ()
        if CLASS == "Barbarian" or CLASS == "Ranger":
            print ("Your background is Outlander")
            print ("You grew up in the wilds far from civilization. The wilds are in your blood")
            print ("The proficiencies are Athletics, Survival, a musical instrument of your choice and One Language of your choice. Feature: Wanderer")
            print ("Your additional equipment is: A staff, a hunting trap, a trophy from a killed animal, a set of traveler's clothes and a pouch containing 10gp")
            x = random.randint (1,10)
            if x == 1:
                print ("Your Origin is Forester")
            elif x == 2:
                print ("Your Origin is Trapper")
            elif x == 3:
                print ("Your Origin is Homesteader")
            elif x == 4:
                print ("Your Origin is Guide")
            elif x == 5:
                print ("Your Origin is Exile or Outcast")
            elif x == 6:
                print ("Your Origin is Bounty Hunter")
            elif x == 7:
                print ("Your Origin is Pilgrim")
            elif x == 8:
                print ("Your Origin is Tribal Nomad")
            elif x == 9:
                print ("Your Origin is Hunter-Gatherer")
            else:
                print ("Your Origin is Tribal Marauder")
            print ("Outlanders are often considered rude among civilized folk")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is a wanderlust")
            elif x == 2:
                print ("Your personality trait is a need to watch over your friends")
            elif x == 3:
                print ("Your personality trait is a great sense of duty to protect your village")
            elif x == 4:
                print ("Your personality trait is: You have a lesson for every situation")
            elif x == 5:
                print ("Your personality trait is a disrespect for money and manners")
            elif x == 6:
                print ("Your personality trait is an urge to pick up and fiddle with things, often breaking them")
            elif x == 7:
                print ("Your personality trait is a greater comfort around animals than people")
            else:
                print ("Your personality trait is that you were, in fact, raised by wolves")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that life is in constant change (Chaotic)")
            elif x == 2:
                print ("Your ideal is that the happiness of the tribe is everyone's responsibility (Good)")
            elif x == 3:
                print ("Your ideal that if you dishonor yourself, you dishonor your tribe (Lawful)")
            elif x == 4:
                print ("Your ideal is that the strongest are meant to rule (Evil)")
            elif x == 5:
                print ("Your ideal is that the natural world is more important than civilization (Neutral)")
            else:
                print ("Your ideal is that you must earn glory in battle, for yourself and the clan (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is your family, clan or tribe is your most important thing")
            elif x == 2:
                print ("Your Bond is the wilderness of your home, you have to protect it")
            elif x == 3:
                print ("Your Bond is your evildoers who destroyed your homeland, you will kill them")
            elif x == 4:
                print ("Your Bond is the names of your dead tribe, you will ensure those names enter legend")
            elif x == 5:
                print ("Your Bond is your terrible visions of destuction, you will do anything to prevent them")
            else:
                print ("Your Bond is your tribe, you need to provide children for it")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is your love for beer, ale and other intoxicants")
            elif x == 2:
                print ("Your Flaw is your disregard for danger")
            elif x == 3:
                print ("Your Flaw is your memory for every insult you've recieved and resentment for insulters")
            elif x == 4:
                print ("Your Flaw is your great distrust for everyone else")
            elif x == 5:
                print ("Your Flaw is your violent nature")
            else:
                print ("Your Flaw is you won't help those who can't help themselves")



        elif CLASS == "Bard":
            print ("Your background is Entertainer")
            print ("You thrive in front of an audience, you know how to entrance, entertain, and even inspire them")
            print ("The proficiencies are Acrobatics, Performance, One instrument of your choice, disguise Kit. Feature: By Popular Demand")
            print ("Your additional equipment is: A musical instrument, the favor of an admirer, a costume and a pouch containing 15gp")
            x = random.randint (1,10)
            if x == 1:
                print ("Your Entertainer Routine is Actor")
            elif x == 2:
                print ("Your Entertainer Routine is Dancer")
            elif x == 3:
                print ("Your Entertainer Routine is Fire-Eater")
            elif x == 4:
                print ("Your Entertainer Routine is Jester")
            elif x == 5:
                print ("Your Entertainer Routine is Juggler")
            elif x == 6:
                print ("Your Entertainer Routine is Instrumentalist")
            elif x == 7:
                print ("Your Entertainer Routine is Poet")
            elif x == 8:
                print ("Your Entertainer Routine is Singer")
            elif x == 9:
                print ("Your Entertainer Routine is Storyteller")
            else:
                print ("Your Entertainer Routine is Tumbler ")
            print ("Entertainers tend to have flamboyant or even forceful personalities")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is a story known for every situation")
            elif x == 2:
                print ("Your personality trait is a need to collect and spread gossip")
            elif x == 3:
                print ("Your personality trait is a hopeless romanticism")
            elif x == 4:
                print ("Your personality trait is a capacity to diffuse any amount of tension in and between people")
            elif x == 5:
                print ("Your personality trait is a love for good insults, even when directed a you")
            elif x == 6:
                print ("Your personality trait is a need to be the center of attention")
            elif x == 7:
                print ("Your personality trait is perfectionism")
            else:
                print ("Your personality trait is rapid mood changes")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that you make the world a better place when you perform (Good)")
            elif x == 2:
                print ("Your ideal is that the old stories and songs must not be forgotten (Lawful)")
            elif x == 3:
                print ("Your ideal is that the world is in need of new ideas and bold action (Chaotic)")
            elif x == 4:
                print ("Your ideal is that you need to become rich and famous (Evil)")
            elif x == 5:
                print ("Your ideal is that the smiles of the people when you perform are the only thing that matters (Neutral)")
            else:
                print ("Your ideal is that Art should reflect the soul of the artist (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is your instrument is the most important thing")
            elif x == 2:
                print ("Your Bond is the need to recover your stolen instrument")
            elif x == 3:
                print ("Your Bond is you need to be famous, no matter what")
            elif x == 4:
                print ("Your Bond is the hero of old tales. You're always comparing yourself with him")
            elif x == 5:
                print ("Your Bond is your hated rival. You will do anything to prove yourself superior.")
            else:
                print ("Your Bond is your old troupe. You would do anything for them")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is you would do anything to win fame and renown")
            elif x == 2:
                print ("Your Flaw is you are a sucker for a prety face")
            elif x == 3:
                print ("Your Flaw is a scandal which prevents you from going back home, that kind of trouble seems to follow you around")
            elif x == 4:
                print ("Your Flaw is you once satirized a noble who still wants your head")
            elif x == 5:
                print ("Your Flaw is your sharp toungue which lands you in trouble")
            else:
                print ("Your Flaw is you are unreliable to your friends")



        elif CLASS == "Cleric":
            print ("Your background is Acolyte")
            print ("You have spent your life in the srevice of a Temple to a specific god")
            print ("The proficiencies are Insight and Religion. Feature: Shelter of the Faithful. You know two additional languages")
            print ("Your additional equipment is: A holy symbol, a prayer book, 5 sticks of incense, vestments, a set of common clothes and a pouch containing 15gp")
            print ("Acolytes are shaped by the experience in temples")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is a hero whom you idolize and constantly refer to")
            elif x == 2:
                print ("Your personality trait is a capacity to empathize with your enemy")
            elif x == 3:
                print ("Your personality trait is that you are constantly seeing omens")
            elif x == 4:
                print ("Your personality trait is a very optimistic attitude")
            elif x == 5:
                print ("Your personality trait is that you quote or misquote sacred texts and proverbs in every situation")
            elif x == 6:
                print ("Your personality trait is that you are tolerant (or intolerant) of other faiths and respect (or condemn) the worship of othr gods")
            elif x == 7:
                print ("Your personality trait is that rough living grates on you")
            else:
                print ("Your personality trait is that you have little experience dealing with other people")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that old traditions and rituals must be preserved and upheld (Lawful)")
            elif x == 2:
                print ("Your ideal is that you always try to help people in need. No matter what (Good)")
            elif x == 3:
                print ("Your ideal is that you must help bring out the changes the gods are working (Chaotic)")
            elif x == 4:
                print ("Your ideal is that you hope to rise to the top of your religious hierarchy (Evil)")
            elif x == 5:
                print ("Your ideal is that a deity will guide your actions. If you work hard, things will go well (Lawful)")
            else:
                print ("Your ideal is that you seek to prove yourself worthy of your god's favor (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is you would die for a relic stolen many years ago")
            elif x == 2:
                print ("Your Bond is the need to get revenge to the corrupt temple hierarchy ")
            elif x == 3:
                print ("Your Bond is you owe your life to the priest who took you in when your parents died")
            elif x == 4:
                print ("Your Bond is the common people. Everything you do is for them")
            elif x == 5:
                print ("Your Bond is the temple you served in. You would do anything to protect it")
            else:
                print ("Your Bond is you seek to protect a scared text which your enemies consider heretical and seek to destroy")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is you judge others harshly. You judge yourself even more severely")
            elif x == 2:
                print ("Your Flaw is you put too much trust in those who wield power")
            elif x == 3:
                print ("Your Flaw is you sometimes blindly trust those who share your faith")
            elif x == 4:
                print ("Your Flaw is you are inflexible in your thinking ")
            elif x == 5:
                print ("Your Flaw is you are suspicious of strangers and expect the worst of them")
            else:
                print ("Your Flaw is once you pick a goal, you become obsessed")



        elif CLASS == "Druid"  or CLASS =="Monk"  or CLASS == "Sorcerer":
            print ("Your background is Hermit")
            print ("You lived in seclusion for a formative part of your life")
            print ("The proficiencies are Medicine, Religion, herbalism kit. Feature: Discovery")
            print ("Your additional equipment is: a scroll case full of notes from your studies, a winter blanket, a set of common clothes, a herbalism kit and a pouch containing 5gp")
            x = random.randint (1,8)
            if x == 1:
                print ("Your Life of Seclusion is a search for spirital enlightment")
            elif x == 2:
                print ("Your Life of Seclusion is a communal living in accordance to a religious order")
            elif x == 3:
                print ("Your Life of Seclusion is an exile from a crime you didn't commit")
            elif x == 4:
                print ("Your Life of Seclusion is a retreat from society after a life-changing event")
            elif x == 5:
                print ("Your Life of Seclusion is a need for a quiet place to work")
            elif x == 6:
                print ("Your Life of Seclusion is a need to commune with nature")
            elif x == 7:
                print ("Your Life of Seclusion is a duty to protect an ancient ruin or relic")
            else:
                print ("Your Life of Seclusion is a pilgrimage in search for a person, place or personal relic")
            print ("The solitary life shapes hermits's attitudes and ideals")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is that you barely speak")
            elif x == 2:
                print ("Your personality trait is an uncanny serenity in all situations")
            elif x == 3:
                print ("Your personality trait is an eagerness to share your wisdom")
            elif x == 4:
                print ("Your personality trait is a tremendous empathy for all who suffer")
            elif x == 5:
                print ("Your personality trait is that you are oblivious to etiquette and social expectations")
            elif x == 6:
                print ("Your personality trait is a belief that everything is connected to a cosmic plan")
            elif x == 7:
                print ("Your personality trait is that you often get lost in thought and become oblivious to your surroundings")
            else:
                print ("Your personality trait is that your philosophical ideas must be shared")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that your gifts must be shared with all (Good)")
            elif x == 2:
                print ("Your ideal is that emotions should not cloud judgement (Lawful)")
            elif x == 3:
                print ("Your ideal is that inquiry and curiosity are the pillars of progress (Chaotic)")
            elif x == 4:
                print ("Your ideal is that solitude and contemplation are the path to mystical or magical power (Evil)")
            elif x == 5:
                print ("Your ideal is that meddling with the affairs of others only causes trouble (Neutral)")
            else:
                print ("Your ideal is that if you know yourself, there is nothing left to know (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is the other members of your hermitage, order or association")
            elif x == 2:
                print ("Your Bond is that you entered seclusion to hide from those who might still be hunting you")
            elif x == 3:
                print ("Your Bond is that you are still searching enlightment, and it still eludes you ")
            elif x == 4:
                print ("Your Bond is that you loved someone you could not have")
            elif x == 5:
                print ("Your Bond is your discovery. It should not come to light.")
            else:
                print ("Your Bond is that your isolation gave you great insight into a great evil only you can destroy")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is you enjoy the world's delights a bit too much")
            elif x == 2:
                print ("Your Flaw is you harbor dark, blodthirsty thoughts")
            elif x == 3:
                print ("Your Flaw is that you are dogmatic")
            elif x == 4:
                print ("Your Flaw is you let your need to win arguments overshadow friendships")
            elif x == 5:
                print ("Your Flaw is your thirst for knowledge. You would do anything for it")
            else:
                print ("Your Flaw is that you like keeping secrets")



        elif CLASS == "Fighter":
            print ("Your background is Soldier")
            print ("War has been your life for as long as you care to remember")
            print ("The proficiencies are Athletics, Intimidation, one type of gaming set and land vehicles. Feature: Military Rank")
            print ("Your additional equipment is: An insignia of a rank, a trophy taken from a fallen enemy, a set of bone dice or a deck of cards and a pouch containing 10gp")
            x = random.randint (1,8)
            if x == 1:
                print ("Your Specialty is Officer")
            elif x == 2:
                print ("Your Specialty is Scout")
            elif x == 3:
                print ("Your Specialty is Infantry")
            elif x == 4:
                print ("Your Specialty is Cavalry")
            elif x == 5:
                print ("Your Specialty is Healer")
            elif x == 6:
                print ("Your Specialty is Quartermaster")
            elif x == 7:
                print ("Your Specialty is Standard bBearer")
            else:
                print ("Your Specialty is Support Staff ")
            print ("The horrors of war tend to shape the fighter's ideals, create strong bonds and often leave them scarred")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is a very polite and respectful nature")
            elif x == 2:
                print ("Your personality trait is that you are haunted by the memories of war")
            elif x == 3:
                print ("Your personality trait is a slowness to make friends")
            elif x == 4:
                print ("Your personality trait is that you are full of inspiring tales from your years in the army. You have a lot of combat experience")
            elif x == 5:
                print ("Your personality trait is that you can stare down a hell hound without flinching")
            elif x == 6:
                print ("Your personality trait is a pleasure taken by breaking things")
            elif x == 7:
                print ("Your personality trait is a very crude sense of humor")
            else:
                print ("Your personality trait is that you face problems head-on")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that the army should give their lives in thee defense of others (Good)")
            elif x == 2:
                print ("Your ideal is that you obey authority (Lawful)")
            elif x == 3:
                print ("Your ideal is that people should not follow orders blindly (Chaotic)")
            elif x == 4:
                print ("Your ideal is that the strongest force wins (Evil)")
            elif x == 5:
                print ("Your ideal is that ideals are not worth killing over for (Neutral)")
            else:
                print ("Your ideal is that your nation is all that matters (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is the people you served with. You would do anything for them")
            elif x == 2:
                print ("Your Bond is the sodier who saved your life on the battlefield. You will never leave a friend behind")
            elif x == 3:
                print ("Your Bond is your honor")
            elif x == 4:
                print ("Your Bond is the crushing defeat of your company. You will never forget it")
            elif x == 5:
                print ("Your Bond is those who fight beside you. Only they are worth dying for")
            else:
                print ("Your Bond is those who can't fight for themselves. You will protect them")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is you fear a monstrous enemy you've faced in the battlefield before")
            elif x == 2:
                print ("Your Flaw is you have little respect for those who haven't served in a battlefield")
            elif x == 3:
                print ("Your Flaw is a mistake which cost a lot of lives. You will do anything to keeo it a secret")
            elif x == 4:
                print ("Your Flaw is that your hatred for your enemies is blind and unreasoning")
            elif x == 5:
                print ("Your Flaw is that you obey every law, no matter what")
            else:
                print ("Your Flaw is that you never admit you are wrong")




        elif CLASS == "Paladin":
            print ("Your background is Noble")
            print ("You understand wealth, power and privilege")
            print ("The proficiencies are History, Persuasion, one type of gaming set and one additional language of your choice. Feature: Position of Privilege")
            print ("Your additional equipment is: a set of fine clothes, a signet ring, a scroll of pedigree and a purse containing 25gp")
            print ("Nobles are born and raised in a very different manner than common folk, and their personalities reflect that upbringing")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is that your eloquent flattery makes people feel good")
            elif x == 2:
                print ("Your personality trait is that the common folk love you for your kindness and generosity")
            elif x == 3:
                print ("Your personality trait that you dress as a noble (always washed)")
            elif x == 4:
                print ("Your personality trait is a need to look good and folow the latest fashions")
            elif x == 5:
                print ("Your personality trait is that you don't like getting your hands dirty")
            elif x == 6:
                print ("Your personality trait is a great sense of equality")
            elif x == 7:
                print ("Your personality trait is that your favor, once lost, is lost forever")
            else:
                print ("Your personality trait is that if someone does you an injury, you will crush them, their names and friends")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that everyone deserves respect (Good)")
            elif x == 2:
                print ("Your ideal is that it is everyone's duty to respect authority (Lawful)")
            elif x == 3:
                print ("Your ideal is that you must prove that you can handle yourself without the support of your family (Chaotic)")
            elif x == 4:
                print ("Your ideal is that if you gain more power, no one will ever tell you what to do (Evil)")
            elif x == 5:
                print ("Your ideal is that ,Blood runs thicker than water'. You are loyal to your family (Any)")
            else:
                print ("Your ideal is that it's your duty to protect your people (Good)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is your family. You'd do anything to please them")
            elif x == 2:
                print ("Your Bond is the alliance with another noble house. It needs to be sustained")
            elif x == 3:
                print ("Your Bond is that nothing is more important than the other members of your family")
            elif x == 4:
                print ("Your Bond is that you are in love with the heir of a family that your familiy despises")
            elif x == 5:
                print ("Your Bond is your loyalty to your sovereign.")
            else:
                print ("Your Bond is that the common folk must see you as a hero of the people")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is that you secretly think that everyone is beneath you")
            elif x == 2:
                print ("Your Flaw is that you hold a truly scandalous secret which could bring ruin to your family")
            elif x == 3:
                print ("Your Flaw is that you often hear veiled insults and threats in every word and you are quick to anger")
            elif x == 4:
                print ("Your Flaw is you have an insatiable desire for carnal pleasures")
            elif x == 5:
                print ("Your Flaw is your belief that the world does resolve around you")
            else:
                print ("Your Flaw is that you often bring shame to your family by your words and actions")




        elif CLASS == "Rogue"  or CLASS == "Warlock":
            print ("Your background is Charlatan")
            print ("You have always had a way with people. ")
            print ("The proficiencies are Deception, sleight of Hand, forgery and disguise kits. Feature: False Identity")
            print ("Your additional equipment is: A disguise kit, tools of the con of your choice, a set of fine clothes and a pouch containing 15gp")
            x = random.randint (1,10)
            if x == 1:
                print ("Your Favorite Scam is cheating at games of chance")
            elif x == 2:
                print ("Your Favorite Scam is shaving coins or forgind documents")
            elif x == 3:
                print ("Your Favorite Scam is insinuating yourself into poeple's lives and prey on their weakness and secure their fortunes")
            elif x == 4:
                print ("Your Favorite Scam is to put on new identities")
            elif x == 5:
                print ("Your Favorite Scam is running sleight of hand cons on the streets")
            else:
                print ("Your Favorite Scam is convincing people that worthless junk is worth their money")
            print ("Charlatans are colorful characters who conceal their true selves")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is that you fall in and out of love very easily")
            elif x == 2:
                print ("Your personality trait is a joke for every occasion, even inappropiate")
            elif x == 3:
                print ("Your personality trait is that flattery is your way of getting what you want")
            elif x == 4:
                print ("Your personality trait is that you are a born gambler")
            elif x == 5:
                print ("Your personality trait is a need to lie for almost everything")
            elif x == 6:
                print ("Your personality trait is that you keep a lot of holy symbols and prey to all of them to invoke whatever deity will help")
            elif x == 7:
                print ("Your personality trait is that sarcasm and insults are your main weapon")
            else:
                print ("Your personality trait is that pocket everything that might have some value")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that you are a free spirit (Chaotic)")
            elif x == 2:
                print ("Your ideal is that you never target those without money (Lawful)")
            elif x == 3:
                print ("Your ideal that you distribute the money you earn among those who need it (Good)")
            elif x == 4:
                print ("Your ideal is that you must never run the same con twice (Chaotic)")
            elif x == 5:
                print ("Your ideal is that bonds of friendship are worth more than material goods (Good)")
            else:
                print ("Your ideal is that you are determined to make something of yourself (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is that you must ensure never to cross paths again with the people you fleeced")
            elif x == 2:
                print ("Your Bond is your mentor whom you owe everything to (he's probably rotting in a jail)")
            elif x == 3:
                print ("Your Bond is your child who doesn't know you. You will make the world a better place for him/her.")
            elif x == 4:
                print ("Your Bond is your noble family. One day you will return to claim what is yours")
            elif x == 5:
                print ("Your Bond is a powerful person who killed someone you love. You will soon have your revenge")
            else:
                print ("Your Bond is a person you swindled and ruined. You are trying to atone for your misdeeds")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is your love for pretty faces")
            elif x == 2:
                print ("Your Flaw is your constant debt")
            elif x == 3:
                print ("Your Flaw is that you are convinced no one can fool you")
            elif x == 4:
                print ("Your Flaw is your greediness")
            elif x == 5:
                print ("Your Flaw is your urge to swindle those who are more powerful than you")
            else:
                print ("Your Flaw is that you will run and preserve your own if the going gets tough")



        elif CLASS == "Wizard":
            print ("Your background is Sage")
            print ("You spent years learning the lore of the multiverse")
            print ("The proficiencies are Arcana and History. Feature: Researcher. You know two additional languages")
            print ("Your additional equipment is: A bottle of black ink, a quill, a small knife, a letter of a dead colleague posing questions you haven't been able to answer, a set of common clothes and a pouch containing 10gp")
            x = random.randint (1,8)
            if x == 1:
                print ("Your Specialty is Alchemist")
            elif x == 2:
                print ("Your Specialty is Astronomer")
            elif x == 3:
                print ("Your Specialty is Discredited Academic")
            elif x == 4:
                print ("Your Specialty is Librarian")
            elif x == 5:
                print ("Your Specialty is Professor")
            elif x == 6:
                print ("Your Specialty is Researcher")
            elif x == 7:
                print ("Your Specialty is Wizard's Apprentice")
            else:
                print ("Your Specialty is Scribe ")
            print ("Sages are defined by their extensive studies.")
            x = random.randint (1,8)
            if x == 1:
                print ("Your personality trait is a polysyllabic vocabulary")
            elif x == 2:
                print ("Your personality trait is that you've read every single book in the great library")
            elif x == 3:
                print ("Your personality trait is  great patience")
            elif x == 4:
                print ("Your personality trait is that you enjoy a good mystery")
            elif x == 5:
                print ("Your personality trait is that you will listen to both sides of an argument before judging")
            elif x == 6:
                print ("Your personality trait is that you speak very slowly when talking to those with an inferior intelligence")
            elif x == 7:
                print ("Your personality trait is that you are terribly awkward in social situations")
            else:
                print ("Your personality trait is that you are convinced that people are trying to steal your secrets")
            x = random.randint (1,6)
            if x == 1:
                print ("Your ideal is that the path to power is through knowledge (Neutral)")
            elif x == 2:
                print ("Your ideal is that what is beautiful points us beyond itself towards truth (Good)")
            elif x == 3:
                print ("Your ideal is that emotions shouldn't cloud our judgment (Lawful)")
            elif x == 4:
                print ("Your ideal is that nothing should fetter the infinite possibility innherent in all existance (Chaotic)")
            elif x == 5:
                print ("Your ideal is that knowledge is the path to domination (Evil)")
            else:
                print ("Your ideal is that the goal of a life of study is the betterment of oneself (Any)")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Bond is the your students. You would do anything to protect them")
            elif x == 2:
                print ("Your Bond is the ancient text you hold. It must not fall into the wrong hands")
            elif x == 3:
                print ("Your Bond is your need to preserve a library, university, monastery or scriptorium")
            elif x == 4:
                print ("Your Bond is your life's work")
            elif x == 5:
                print ("Your Bond is the search for anwsers you've been looking for your entire life")
            else:
                print ("Your Bond is your soul. You sold it for knowledge and hope to do great deeds to get it back")
            x = random.randint (1,6)
            if x == 1:
                print ("Your Flaw is that you are easily distracted by the promise of information")
            elif x == 2:
                print ("Your Flaw is that you have to learn more, no matter what.")
            elif x == 3:
                print ("Your Flaw is that you believe that unlocking an ancient mystery is worth the price of a civilization")
            elif x == 4:
                print ("Your Flaw is that you overlook obvious solutions in favor to overcomplicated ones")
            elif x == 5:
                print ("Your Flaw is that you speak without thinking")
            else:
                print ("Your Flaw is that you can't keep secrets")

        else:
            print ("Make sure you are spelling correctly")
            continue
        return


print ("Rewrite your Class")
BACKGROUND ()


print ("If you have a Spellcasting Class, please write it to see your cantrip and 1st level spell list. If not, write your class")

def SPELLLISTS ():
    while True:
        Spellclass = input ()
        if Spellclass == "Bard":
            print ("Your Spell and Cantrip suggestions are above, but if you wish to see the lists, here they are")
            Cantrips = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigitation", "True Strike", "Vicious Mockery"]
            print ("Your available cantrips are:")
            print (Cantrips [0:11])
            BardSpells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Faerie fire", "Feather Fall", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Talk to animals", "Tasha's hideous laughter", "Thunderwave", "Unseen Servant"]
            print ("Your available Spells are:")
            print (BardSpells [0:20])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Cleric":
            Cantrips = ["Guidance", "Lights", "Mending", "Resistance", "Sacred Flame", "Spare the dying", "Thaumaturgy"]
            print ("Your available cantrips are:")
            print (Cantrips [0:6])
            ClericSpells = ["Bane", "Bless", "Commmand", "Create or Destroy Water", "Cure Wounds", "Detect Evil or Good", "Detect Magic", "Detect Poison and Disease", "Guiding Bolt", "Healing Word", "Heroism", "Inflict Wounds", "Protection from Evil and Good", "Purify Food and Drink", "Sanctuary", "Shield of Faith"]
            print ("Your available Spells are:")
            print (ClericSpells [0:14])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Druid":
            Cantrips = ["Druidcraft", "Guidance", "Mending", "Poison Spray", "Produce Flame", "Resistance", "Shillelagh", "Thorn Whip"]
            print ("Your available cantrips are:")
            print (Cantrips [0:7])
            DruidSpells = ["Animal Friendship", "Charm Person", "Create or Destroy Water", "Cure Wounds", "Detect Magic", "Detect Poison and Disease", "Entangle", "Farie fire", "Fog Cloud", "Goodberry", "Healing Word", "Jump", "Longstrider", "Purify Food and Drink", "Speak with Animals", "Thunderwave"]
            print ("Your available Spells are:")
            print (DruidSpells [0:15])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Sprcerer":
            Cantrips = ["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
            print ("Your available cantrips are:")
            print (Cantrips [0:15])
            SorcererSpells = ["Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False life", "Feather Fall", "Fog Cloud", "Jump", "Mage Armor", "Magic Missile", "Ray of Sickness", "Shield", "Silent Image", "Sleep", "Thunderwave", "Witch Bolt"]
            print ("Your available Spells are:")
            print (SorcererSpells [0:20])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Warlock":
            Cantrips = ["Blade Ward", "Chill Touch", "Eldritch Blast", "Friends", "Mage Hand", "Minor Illusion", "Poison Spray", "Prestidigitation", "True Strike"]
            print ("Your available cantrips are")
            print (Cantrips [0:8])
            WarlockSpells = ["Armor of Agathys", "Arms of Hadar", "Charm Person", "Comprehend Languages", "Expeditious Retreat", "Hellish Rebuke", "Hex", "Illusory Script", "Protection from Evil and Good", "Unseen Servant", "Witch Bolt"]
            print ("Your available Spells are:")
            print (WarlockSpells [0:10])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Wizard":
            Cantrips = ["Acid Splash", "Blade Ward", "Chill Touch", "Dancing Lights", "Fire Bolt", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", "Ray of Frost", "Shocking Grasp", "True Strike"]
            print ("Your available cantrips are:")
            print (Cantrips [0:15])
            WizardSpells = ["Alarm", "Burning Hands", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages", "Detect Magic", "Disguise Self", "Expeditious Retreat", "False life", "Feather Fall", "Find Familiar", "Fog Cloud", "Grease", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection form Evil and Good", "Ray of Sickness", "Shield", "Silent Image", "Sleep", "Tasha's hideous Laughter", "Tenser's Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"]
            print ("Your available Spells are:")
            print (WizardSpells [0:30])
            print ("The number of cantrips and spells you know is specified in the Class section")
        elif Spellclass == "Ranger" or Spellclass == "Paladin" or Spellclass == "Fighter" or Spellclass == "Monk":
            print ("Your class can't cast spells at 1st level")
        elif Spellclass == "Barbarian" or Spellclass == "Rogue":
            print ("Your class can't cast spells")
        else:
            print ("Write a valid Class")
            continue
        return

SPELLLISTS ()

print ("Thanks for using")


            
            
            
            
            
            
        
                
            






    























        

















    
    
    
    
        
        
        


    
    






    


    
    











    


    

    







    





    



    

    
       
    
    
    





     
    
    


    

    
        
    
    
    


    
    
 
    
    
 

    
