#First of all we need to find how many crop we can produce from a single block in 30 days. Later we are going to calculate the harvest.
# IMPORTANT NOTE: THE DATA IN RIMWORLDWIKI.COM ISN'T DETAILED ENOUGH TO CALCULATE CORRECTLY THE FOLLOWING PLANTS:
# HOP,HEALROOT,POTATO,PSYCHOID,SMOKELEAF,STRAWBERRY
# If you have the necessary informations about these plants, please inform us from our reddit or discord.


CornPlant1 = 29 # How many corns do we get from a single crop in Gravel for 30 days.
CornPlant2 = 40 # How many corns do we get from a single crop in Soil for 30 days. 
CornPlant3 = 58 # How many corns do we get from a single crop in Rich Soil for 30 days. 
CornPlant4 = 0 # can not be sowed to hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

CottonPlant1 = 23 # gravel
CottonPlant2 = 28 # soil
CottonPlant3 = 36 # Rich soil
CottonPlant4 = 54 # Hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

DevilstrandMushroom1 = 4 # gravel
DevilstrandMushroom2 = 6 # soil
DevilstrandMushroom3 = 8 #Rich soil
DevilstrandMushroom4 = 0 # can not be sowed to hydroponics DO NOT USE THIS VARIABLE

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

HaygrassPlant1 = 47 #gravel
HaygrassPlant2 = 57 #soil
HaygrassPlant3 = 70 #Richsoil
HaygrassPlant4 = 0 # Can not be sowed to hydroponics DO NOT USE THIS VARIABLE

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

HealrootPlant1 = 2 # Gravel
HealrootPlant2 = 2 # soil
HealrootPlant3 = 2 # Richsoil
HealrootPlant4 = 2 # Hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

HopPlant1 = 33 #Gravel
HopPlant2 = 33 #soil
HopPlant3 = 33 #rich soil
HopPlant4 = 33 #Hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

PotatoPlant1 = 40 # gravel
PotatoPlant2 = 40 # soil
PotatoPlant3 = 40 # rich soil
PotatoPlant4 = 40 # hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

PsychoidPlant1 = 15 # gravel
PsychoidPlant2 = 15 # soil
PsychoidPlant3 = 15 # rich soil
PsychoidPlant4 = 15 # Hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

RicePlant1 = 8 # gravel
RicePlant2 = 8 # soil
RicePlant3 = 8 # rich soil
RicePlant4 = 8 # Hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

SmokeleafPlant1 = 20 # gravel
SmokeleafPlant2 = 20 # soil
SmokeleafPlant3 = 20 # rich soil
SmokeleafPlant4 = 20 # hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------

StrawberryPlant1 = 36 # gravel
StrawberryPlant2 = 36 # soil
StrawberryPlant3 = 36 # rich soil
StrawberryPlant4 = 36 # hydroponics

# -------------------------------------------------------------------------------------------------0-----------------------------------------------------------------------------------


Foods = [CornPlant1,CornPlant2,CornPlant3,CornPlant4,PotatoPlant1,PotatoPlant2,PotatoPlant3,PotatoPlant4,RicePlant1,RicePlant2,RicePlant3,RicePlant4,StrawberryPlant1,StrawberryPlant2,StrawberryPlant3,StrawberryPlant4]
Plants = [CottonPlant1,CottonPlant2,CottonPlant3,CottonPlant4,DevilstrandMushroom1,DevilstrandMushroom2,DevilstrandMushroom3,DevilstrandMushroom4,HaygrassPlant1,HaygrassPlant2,HaygrassPlant3,HaygrassPlant4,HealrootPlant1,HealrootPlant2,HealrootPlant3,HealrootPlant4,HopPlant1,HopPlant2,HopPlant3,HopPlant4,PsychoidPlant1,PsychoidPlant2,PsychoidPlant3,PsychoidPlant4,SmokeleafPlant1,SmokeleafPlant2,SmokeleafPlant3,SmokeleafPlant4]
crops = ["Corn Plant","Cotton Plant","Devilstrand Mushroom","Haygrass Plant","Healroot Plant","Hop Plant","Potato Plant","Psychoid Plant","Rice Plant","Smokeleaf Plant","Strawberry Plant"]
crops_gravel_30days = [CornPlant1,CottonPlant1,DevilstrandMushroom1,HaygrassPlant1,HealrootPlant1,HopPlant1,PotatoPlant1,PsychoidPlant1,RicePlant1,SmokeleafPlant1,StrawberryPlant1]
crops_soil_30days = [CornPlant2,CottonPlant2,DevilstrandMushroom2,HaygrassPlant2,HealrootPlant2,HopPlant2,PotatoPlant2,PsychoidPlant2,RicePlant2,SmokeleafPlant2,StrawberryPlant2]
crops_Rsoil_30days = [CornPlant3,CottonPlant3,DevilstrandMushroom3,HaygrassPlant3,HealrootPlant3,HopPlant3,PotatoPlant3,PsychoidPlant3,RicePlant3,SmokeleafPlant3,StrawberryPlant3]
crops_Hydro_30days = [CornPlant4,CottonPlant4,DevilstrandMushroom4,HaygrassPlant4,HealrootPlant4,HopPlant4,PotatoPlant4,PsychoidPlant4,RicePlant4,SmokeleafPlant4,StrawberryPlant4]

# Lots of lists.

print("Hello, Welcome to Rimworld Crop Calculator! This program is designed to calculate the amount of crops you need for your colony (for foods) and it also gives you the harvest yield of the other plants. Keep in mind we as Mercymek wrote this\napplication for study purpose and if it catches your interest we will make this application much better.\n\n")

colonists = float(input("Please enter how many colonists are living in your colony:"))

if colonists < 0:
	print("Nice try.")
	
	input("Press enter to close the program.")
	quit()
elif colonists == 0:
	print("Nice try.")
	
	input("Press enter to close the program.")
	quit()
corn_eaten_by_a_single_colonist_perday = 30.0
corn_for_30_days = corn_eaten_by_a_single_colonist_perday * colonists * 30.0 # for 30 days 
corn_for_30_days_final = corn_for_30_days * 0.7

potato_eaten_by_a_single_colonist_perday = 30.0
potato_for_30days = potato_eaten_by_a_single_colonist_perday * colonists * 30.0 # for 30 days
potato_for_30days_final = potato_for_30days * 0.7

rice_eaten_by_a_single_colonist_perday = 30.0
rice_eaten_for_30days = rice_eaten_by_a_single_colonist_perday * colonists * 30.0
rice_eaten_for_30days_final = rice_eaten_for_30days * 0.7

strawberry_eaten_by_a_single_colonists_perday = 30.0
strawberry_eaten_for_30days = strawberry_eaten_by_a_single_colonists_perday * colonists * 30.0
strawberry_eaten_for_30days_final = strawberry_eaten_for_30days * 0.7

print("You have this many colonists:", colonists)

corn1 = corn_for_30_days_final / CornPlant1
corn2 = corn_for_30_days_final / CornPlant2
corn3 = corn_for_30_days_final / CornPlant3
#corn4 is zero and causes the division by zero error.

potato1 = potato_for_30days_final / PotatoPlant1
potato2 = potato_for_30days_final / PotatoPlant2
potato3 = potato_for_30days_final / PotatoPlant3
potato4 = potato_for_30days_final / PotatoPlant4

rice1 = rice_eaten_for_30days_final / RicePlant1
rice2 = rice_eaten_for_30days_final / RicePlant2
rice3 = rice_eaten_for_30days_final / RicePlant3
rice4 = rice_eaten_for_30days_final / RicePlant4

strawberry1 = strawberry_eaten_for_30days_final / StrawberryPlant1
strawberry2 = strawberry_eaten_for_30days_final / StrawberryPlant2
strawberry3 = strawberry_eaten_for_30days_final / StrawberryPlant3
strawberry4 = strawberry_eaten_for_30days_final / StrawberryPlant4




# Change everything with value of 0 to something or it breaks the code.
# All variables are set now we will move to the procedure.

entered_key = int(input("Please select a Plant type.\nCorn->0\nCotton->1\nDevilstrand Mushroom->2\nHaygrass Plant->3\nHealroot Plant->4\nHop Plant->5\nPotato Plant->6\nPsychoid Plant->7\nRice Plant->8\nSmokeleaf Plant->9\nStrawberry Plant->10\n\nPlease make an entry:"))

if   entered_key == 0:
		print("You have chosen the Corn plant. The colony needs these many crops : (Gravel, Soil, Rich Soil)", int(corn1), int(corn2), int(corn3))

		input("To close the program please press enter...\n") # Make every input like this for decoration purpose.
		quit()
elif entered_key == 1:
		print("You have chosen the Cotton plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", CottonPlant1, CottonPlant2, CottonPlant3, CottonPlant4)
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 2:
		print("You have chosen the Devilstrand Mushroom. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", DevilstrandMushroom1, DevilstrandMushroom2, DevilstrandMushroom3, DevilstrandMushroom4)
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 3:
		print("You have chosen the Haygrass plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", HaygrassPlant1, HaygrassPlant2, HaygrassPlant3 , HaygrassPlant4)
	
		input("To close the program please press enter.")
		quit()
elif entered_key == 4:
		print("You have chosen the Healroot plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", HealrootPlant1, HealrootPlant2, HealrootPlant3, HealrootPlant4)

		input("To close the program please press enter.")
		quit()
elif entered_key == 5:
		print("You have chosen the Hop plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", HopPlant1, HopPlant2, HopPlant3, HopPlant4)
	
		input("To close the program please press enter.")
		quit()
elif entered_key == 6:
		print("You have chosen the Potato plant. The colony needs these many crops : (Gravel, Soil, Rich Soil, Hydroponics)", int(potato1), int(potato2), int(potato3), int(potato4))
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 7:
		print("You have chosen the Psychoid plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", PsychoidPlant1,PsychoidPlant2,PsychoidPlant3,PsychoidPlant4)
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 8:
		print("You have chosen the Rice plant. The colony needs these many crops : (Gravel, Soil, Rich Soil, Hydroponics)", int(rice1), int(rice2), int(rice3),int(rice4))
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 9:
		print("You have chosen the Smokeleaf plant. Harvest yield is listed in this order : (Gravel, Soil, Rich Soil, Hydroponics)", SmokeleafPlant1,SmokeleafPlant2,SmokeleafPlant3,SmokeleafPlant4)
		
		input("To close the program please press enter.")
		quit()
elif entered_key == 10:
		print("You have chosen the Strawberry plant. The colony needs these many crops : (Gravel, Soil, Rich Soil, Hydroponics)", int(strawberry1), int(strawberry2), int(strawberry3), int(strawberry4))
		
		input("To close the program please press enter.")
		quit()
else:
		print("Goodbye.")
		
		input("Press enter to close the program")
		quit()

		#elif entered_key == #number here:
	#print("You have chosen the ... Plant.\n Every crop gives that much in gravel:", #variable comes here)
	#	
	#input("To close the program press enter.")	
	
	
	
	
	
	
#    __  __                                    _       ____   __  __ _      _       _ 
#   |  \/  |                                  | |     / __ \ / _|/ _(_)    (_)     | |
#   | \  / | ___ _ __ ___ _   _ _ __ ___   ___| | __ | |  | | |_| |_ _  ___ _  __ _| |
#   | |\/| |/ _ | '__/ __| | | | '_ ` _ \ / _ | |/ / | |  | |  _|  _| |/ __| |/ _` | |
#   | |  | |  __| | | (__| |_| | | | | | |  __|   <  | |__| | | | | | | (__| | (_| | |
#   |_|  |_|\___|_|  \___|\__, |_| |_| |_|\___|_|\_\  \____/|_| |_| |_|\___|_|\__,_|_|
#                          __/ |                                                      
#                         |___/                                                       
# 
#
#  Patreon: https://www.patreon.com/mercymekofficial
#  Github:  https://www.github.com/mercymekofficial
#  Reddit:  https://www.reddit.com/user/sipsipsubidibao
#  Discord: https://discord.gg/3uNm7e2