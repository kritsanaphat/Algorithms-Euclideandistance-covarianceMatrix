
import math
NameTypeGame =["Adventure","Fighting","Moba","Puzzle","RPG","Shooting","Sport","Simulation","Strategy","Horror"]

AdventureOld = [4.3333,4.4667,4.2000,4.1333,4.6667,4.6000,3.8667,3.4000,4.2667,
            4.5333,4.4667,2.8667,3.5333,4.4667,3.8667,3.3333,4.6000,4.9333]          
FightingOld = [4.4667,4.4000,3.7333,4.2000,3.1333,3.2000,4.8000,4.7333,3.2000,
            3.6000,3.0667,2.9333,3.0667,3.2000,4.4000,3.3333,4.4667,3.0000]
MobaOld = [3.7647,	3.9412,	3.0000,3.8824,3.2941,4.0588,4.6471,4.2353,4.6471,
        4.0588,4.3529,2.9412,3.3529,3.6471,4.5294,4.5882,4.3529,3.0588]
PuzzleOld = [2.4667,3.6667,4.7333,2.1333,4.3333,4.6667,1.7333,1.9333,4.7333,
        4.2000,4.8667,1.8000,2.1333,2.2000,3.2667,2.2667,3.9333,2.6667]
RPGOld = [4.5333,4.4000,3.8667,4.8000,4.5333,4.7333,4.7333,3.5333,3.7333,
        4.2667,3.8667,2.1333,3.0000,3.6000,4.6000,3.3333,4.6000,4.6000]
ShootingOld = [3.3158,4.7895,3.0000,4.7368,3.5263,3.8947,4.8421,4.2632,4.7368,
            4.4211,4.6316,3.4211,4.2105,4.3158,4.2632,4.7368,4.4211,3.0526]
SportOld = [4.0000,4.2667,3.0000,1.9333,3.2667,3.6667,2.4000,2.8667,4.2000,
        3.5333,4.2000,4.5333,2.8667,1.6667,2.5333,4.3333,4.5333,2.0000]
SimulationOld = [4.4667,4.8667,2.2000,3.2000,3.8000,3.4000,2.8000,2.2000,1.7333,
            4.6000,3.8667,2.5333,2.8000,4.1333,2.6667,2.5333,4.6667,4.5333]
StrategyOld = [3.2941,4.0588,3.5882,3.6471,3.2941,3.5294,3.8824,2.9412,4.8235,
            4.5294,4.7059,2.000,2.8824,2.9412,3.4118,4.2353,4.4706,2.9412]
SurvivalHorrorOld = [4.7333,4.7333,3.8000,2.2667,4.600,3.2000,1.8000,1.6000,3.6000,
                4.0667,3.2000,1.3333,5.0000,4.6000,2.5333,2.6667,4.8667,4.2000]


Adventure = [4.3571,4.4286,	4.4286,	4.2143,	4.8571,	4.7857,	3.9286,	3.5714,4.3571,
	        4.5714,	4.6429,	3.0000,	3.5000,	4.4286,	4.0000,	3.4286,	4.5714,	4.9286]
Fighting = [4.625,4.5,3.5,4.125,2.375,	2.5,4.875,	4.875,2.125,3,
    	    1.875,1.875,1.875,2.25,	4.25,2.75,4.5,2]
Moba = [3.6923,	3.8462,	2.6923,	3.8462,	3.0769,	4.0769,	4.9231,	4.3846,	4.8462,
        4.0769,	4.5385,	2.7692,	3.1538	,3.5385,4.6923,	4.9231	,4.4615	,2.7692]
Puzzle = [2.0000,	3.4167,	4.7500,	1.9167,	4.3333,	4.7500,	1.4167,	1.5833,	4.7500,
	    4.0833,	4.8333,	1.5000,	1.7500,	1.8333,	2.9167,	1.7500,	3.7500,	2.1667]
RPG = [4.6923,	4.3846,	4.0000,	4.8462,	4.5385,	4.8462,	4.7692,	3.4615,	3.7692,	4.3077,
	    3.7692,	1.8462,	2.9231,	3.5385,	4.6923,	3.1538,	4.6154,	4.6923]
Shooting = [3.1765,	4.7647,	3.0000,	4.7647,	3.4706,	3.9412,	4.8824,	4.4118,	4.8824,	
        4.5294,	4.8235,	3.5882,	4.3529,	4.4118,	4.2353,	4.8235,	4.4118,	2.9412]
Sport = [3.9286	,4.2667	,2.9286	,1.9333,3.2667,	3.6667,	2.2143,	2.8667,	4.2857,
	3.5333,	4.2143,	4.5333,	2.8667,	1.6667,	2.5333,	4.3333,	4.5333,	1.7857]
Simulation = [4.4667,4.8667,1.5000,2.8000,3.7000,3.2000,2.3000,	1.5000,	1.7333,	
            4.6000,3.8667,2.5333,2.5000,4.1333,2.6667,2.5333,4.6667,4.5333]
Strategy = [3.2941,	4.0588,	3.5882,	3.6471,	3.2941,	3.5294,	3.8824,	2.9412,	4.8235,
	4.5294,	4.7059,	1.7692,	2.8824,	2.9412,	3.4118,	4.2353,	4.4706,	2.9412]
SurvivalHorror = [4.7333,4.7333,3.8000,2.2667,4.6000,3.2000,1.8000,1.3846,3.3846,
	            4.0667,2.9231,1.3333,5.0000,4.5385,2.5333,2.6667,4.8667,4.2308]
                
EuclidianValue = []

user_vector = Shooting
adven1 = [5,	5,	3,	3,	5,	4,	3,	2,	4,	5,	3,	1,	3,	4,	1,	1,	5,	5] #Horror #Simulation #Adventure ==
adven2 = [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5] #Adventure
adven3 = [3,	3,	5,	4,	5,	5,	3,	3,	4,	4,	5,	3,	3,	3,	3,	3,	3,	5] #Adventure
adven4 = [5,	5,	3,	5,	5,	5,	5,	3,	4,	5,	5,	5,	5,	5,	5,	5,	5,	5] #Adventure
adven5 = [5,	3,	5,	5,	5,	5,	5,	5,	2,	4,	5,	2,	5,	5,	5,	2,	5,	5] #RPG #Adventure ==
adven6 = [4,	3,	5,	4,	4,	3,	4,	4,	4,	4,	3,	3,	4,	4,	4,	4,	4,	4] #Adventure $$
adven7 = [4,	5,	5,	4,	5,	5,	3,	3,	4,	3,	5,	4,	3,	3,	4,	3,	5,	5] #Adventure 
adven9 = [4,	5,	4,	5,	5,	5,	5,	5,	5,	5,	5,	5,	4,	5,	3,	4,	5,	5] #Adventure
adven10 = [4,	5,	3,	3,	5,	5,	2,	2,	4,	5,	5,	1,	1,	5,	4,	3,	5,	5] #Adventure
adven11 = [3,	4,	5,	5,	5,	5,	5,	5,	5,	5,	5,	4,	3,	5,	4,	3,	4,	5] #Adventure
adven12 = [5,	5,	5,	5,	5,	5,	4,	4,	5,	4,	5,	3,	4,	4,	4,	5,	3,	5] #Adventure
adven13 = [5,	5,	4,	3,	4,	5,	4,	3,	5,	5,	4,	2,	2,	4,	5,	3,	5,	5] #Adventure
adven14 = [4,	4,	5,	4,	5,	5,	3,	3,	5,	5,	5,	2,	3,	5,	4,	3,	5,	5] #Adventure
adven15 = [5,	5,	5,	4,	5,	5,	4,	3,	5,	5,	5,	2,	4,	5,	5,	4,	5,	5] #Adventure


fight5 = [2,	3,	1,	4,	4,	3,	4,	4,	3,	4,	4,	1,	1,	3,	4,	4,	4,	3] #Strategy #Moba #Fighting ==
fight7 = [5,	5,	4,	5,	4,	5,	5,	5,	3,	3,	2,	1,	3,	3,	4,	3,	4,	3] #Fighting
fight9 = [5,	5,	5,	5,	3,	3,	5,	5,	2,	3,	1,	2,	2,	3,	4,	3,	5,	3] #Fighting
fight10 = [5,	5,	5,	5,	3,	3,	5,	5,	2,	3,	1,	2,	3,	3,	4,	3,	5,	3] #Fighting
fight11 = [5,	5,	4,	3,	1,	1,	5,	5,	1,	2,	1,	1,	1,	1,	5,	3,	5,	1] #Fighting
fight12 = [5,	5,	5,	2,	1,	1,	5,	5,	1,	2,	1,	1,	1,	1,	5,	2,	4,	1] #Fighting
fight14 = [5,	3,	2,	5,	2,	3,	5,	5,	2,	5,	3,	4,	3,	3,	5,	3,	5,	1] #Fighting
fight15 = [5,	5,	2,	4,	1,	1,	5,	5,	3,	2,	2,	3,	1,	1,	3,	1,	4,	1] #Fighting


moba1 =  [1,	5,	2,	3,	3,	4,	5,	4,	5,	5,	5,	1,	4,	4,	5,	5,	5,	1] #Moba $$
moba2 =  [5,	3,	3,	5,	5,	5,	5,	5,	5,	5,	5,	1,	3,	2,	5,	5,	5,	3] #Moba
moba3 =  [5,	5,	1,	4,	1,	1,	5,	4,	5,	3,	4,	1,	1,	1,	5,	5,	4,	1] #Fighting #Moba $$
moba4 =  [3,	5,	3,	5,	4,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	4] #Shooting #Moba
moba5 =  [4,	4,	3,	4,	3,	2,	5,	5,	4,	3,	4,	1,	2,	3,	4,	4,	4,	4] #Moba $$
moba7 =  [4,	4,	2,	4,	3,	5,	5,	4,	5,	4,	5,	3,	1,	3,	4,	5,	3,	3] #Moba
moba8 =  [5,	5,	4,	4,	3,	5,	5,	5,	5,	4,	4,	5,	4,	5,	5,	5,	5,	3] #Shooting #Moba
moba10 = [4,	4,	2,	3,	1,	5,	5,	4,	5,	4,	5,	3,	1,	4,	5,	5,	5,	1] #Moba
moba11 = [2,	2,	2,	2,	2,	3,	4,	5,	4,	3,	4,	2,	4,	4,	4,	5,	5,	5] #Moba
moba13 = [4,	5,	4,	5,	3,	5,	5,	5,	5,	4,	5,	3,	4,	5,	5,	5,	4,	2] #Shooting #Moba
moba14 = [3,	3,	3,	5,	4,	5,	5,	4,	5,	4,	4,	2,	4,	4,	4,	5,	3,	3] #Moba
moba17 = [4,	1,	1,	1,	3,	3,	5,	2,	5,	4,	4,	4,	3,	1,	5,	5,	5,  1] #Sport #Moba


puzz1 = [1,	1,	5,	1,	5,	5,	1,	1,	5,	5,	5,	1,	1,	1,	1,	1,	1,	1] #Puzzle
puzz4 = [3,	3,	5,	3,	5,	5,	3,	3,  4,	5,	5,	3,	3,	3,	5,	3,	3,	3] #Puzzle
puzz5 = [1,	3,	5,	2,	3,	5,	1,	1,	5,	4,	5,	1,	1,	1,	4,	2,	5,	2] #Puzzle
puzz6 = [3,	5,	5,	3,	5,	5,	1,	1,	5,	3,	5,	1,	3,	2,	4,	3,	5,	3] #Puzzle
puzz7 = [1,	1,	5,	1,	5,	5,	1,	1,	5,	4,	5,	1,	1,	1,	2,	1,	2,	1] #Puzzle
puzz9 = [2,	5,	5,	3,	4,	5,	1,	1,	5,	4,	5,	1,	2,	1,	4,	1,	5,	2] #Puzzle
puzz10 = [1,	5,	5,	2,	5,	5,	2,	2,	5,	3,	5,	1,	1,	2,	5,	2,	5,	2] #Puzzle
puzz11 = [1,    1,	5,	1,	4,	4,	1,	1,	5,	4,	5,	1,	1,	1,	1,	1,	3,	1] #Puzzle
puzz12 = [1,	5,	5,	2,	3,	5,	1,	1,	5,	5,	5,	1,	1,	1,	2,	1,	3,	2] #Puzzle
puzz14 = [2,	2,	5,	1,	5,	3,	1,	1,	5,	4,	5,	1,	1,	1,	1,	1,	3,	2] #Puzzle
puzz15 = [5,	5,	3,	3,	3,	5,	2,	2,	3,	5,	4,	4,	2,	3,	2,	2,	5,	3] #Simulation Sport Strategy $$$


rpg1 = [5,	5,	5,	5,	5,	5,	5,	5,	4,	5,	4,	3,	3,	4,	5,	3,	5,	5] #RPG
rpg2 = [5,	5,	3,	5,	5,	5,	5,	1,	3,	5,	5,	1,	2,	1,	5,	1,	5,	5] #RPG
rpg3 = [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5] #Adventure #Shooting #RPG ==
rpg5 = [5,	4,	2,	4,	4,	4,	4,	2,	4,	4,	4,	1,	4,	4,	4,	1,	4,	4] #RPG
rpg6 = [4,	3,	4,	5,	5,	5,	5,	4,	4,	5,	3,	3,	3,	3,	5,	4,	5,	5] #RPG
rpg7 = [4,	1,	3,	5,	4,	5,	5,	5,	3,	4,	3,	1,	1,	3,	5,	3,	4,	5] #RPG
rpg8 = [4,	4,	5,	5,	3,	5,	4,	3,	3,	1,	3,	1,	1,	3,	5,	1,	4,	3] #Fighting #RPG == 
rpg10 = [5,	5,	4,	5,	4,	5,	5,	4,	5,	3,	4,	2,	4,	4,	5,	5,	5,	5] #RPG
rpg11 = [4,	5,	5,	5,	4,	4,	5,	3,	3,	5,	3,	1,	1,	4,	5,	5,	4,	5] #RPG
rpg12 = [5,	5,	5,	5,	5,	5,	5,	5,	3,	4,	3,	2,	4,	2,	4,	2,	5,	5] #RPG
rpg13 = [5,	5,	1,	4,	5,	5,	4,	2,	3,	5,	2,	1,	1,	3,	3,	3,	4,	4] #Simulation #RPG == 
rpg14 = [5,	5,	5,	5,	5,	5,	5,	3,	4,	5,	5,	2,	4,	5,	5,	5,	5,	5] #Adventure #RPG == 
rpg15 = [5,	5,	5,	5,	5,	5,	5,	3,	5,	5,	5,  1,	5,	5,	5,	3,	5,	5] #Adventure #RPG ==


shoot2 = [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5] #Adventure #Shooting ==
shoot3 = [3,	5,	5,	5,	3,	4,	5,	4,	5,	5,	5,	4,	5,	4,	5,	5,	4,	2] #Shooting
shoot4 = [1,	4,	2,	5,	2,	3,	5,	1,	4,	3,	4,	1,	5,	2,	5,	2,	4,	1] #Strategy #Moba #Shooting ==
shoot5 = [1,	5,	2,	5,	4,	4,	5,	5,	5,	5,	5,	1,	2,	5,	1,	5,	5,	5] #Shooting
shoot6 = [3,	2,	2,	5,	3,	4,	5,	4,	5,	5,	5,	5,	5,	5,	3,	5,	5,	2] #Shooting
shoot7 = [3,	5,	2,	5,	3,	5,	5,	5,	5,	5,	5,	2,	3,	5,	4,	5,	5,	2] #Shooting
shoot8 = [3,	5,	3,	5,	5,	5,	5,	5,	5,	5,	5,	3,	5,	5,	5,  5,	5,	3] #Shooting
shoot9 = [4,	5,	5,	5,	3,	4,	5,	4,	4,	5,	4,	4,	5,	3,	5,	5,	5,	5] #Shooting
shoot10 = [4,	5,	5,	3,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	3,	5] #Adventure #Shooting == 
shoot11 = [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5] #Adventure #Shooting ==
shoot12 = [4,	5,	2,	4,	2,	3,	4,	3,	5,	4,	5,	5,	3,	5,	2,	5,	4,	3] #Shooting
shoot13 = [3,	5,	3,	5,	5,	3,	5,	5,	5,	5,	5,	5,	5,	4,	3,	5,	3,	3] #Shooting
shoot14 = [3,	5,	2,	5,	4,	3,	5,	5,	5,	5,	5,	4,	5,	5,	5,	5,	5,	2] #Shooting
shoot15 = [3,	5,	3,	5,	2,	5,	4,	4,	5,	4,	4,	1,	3,	5,	4,	5,	4,	2] #Moba #Shooting ==
shoot17 = [2,	5,	3,	4,	3,	3,	5,	5,	5,	2,	5,	5,	5,	4,	5,	5,	5,	2] #Shooting
shoot18 = [2,	5,	1,	5,	2,	1,	5,	5,	5,	4,	5,	5,	3,	3,	5,	5,	5,	2] #Shooting
shoot19 = [5,	5,	1,	5,	3,	5,	5,	5,	5,	5,	5,	1,	5,	5,	5,	5,	3,	1] #Shooting
        

simu2 = [5,	5,	2,	2,	2,	3,	1,	1,	5,	4,	4,	1,	1,	3,	3,	1,	4,	4] #Simulation
simu3 = [5,	5,	1,	2,	4,	4,	2,	1,	5,	4,	4,	3,	2,	3,	1,	1,	3,	3] #Simulation
simu5 = [3,	5,	2,	2,	4,	3,	2,	1,	3,	3,	3,	1,	2,	4,	3,	3,	5,	5] #Simulation
simu6 = [5,	5,	2,	5,	5,	3,	3,	3,	3,	5,	5,	5,	5,	5,	5,	3,	5,	5] #Adventure Shooting RPG $$$
simu9 = [5,	5,	2,	3,	2,	3,	2,	2,	4,	5,	4,	2,	3,	5,	3,	3,	5,	5] #Simulation
simu11 = [4,	5,	1,	5,	3,	4,	5,	2,	4,	5,	4,	2,	4,	5,	2,	5,	4,	5] #Shooting Strategy Moba $$$
simu12 = [5,	5,	1,	2,	4,	4,	2,	1,	1,	5,	2,	1,	2,	5,	2,	1,	5,	5] #Simulation
simu13 = [3,	5,	1,	2,	4,	1,	2,	1,	1,	5,	2,	1,	2,	5,	1,	1,	5,	5] #Simulation
simu14 = [4,	5,	1,	3,	4,	2,	2,	1,	2,	5,	2,	1,	2,	5,	1,	1,	5,	5] #Simulation
simu15 = [5,	5,	2,	2,	5,	5,	2,	2,	5,	5,	5,	4,	2,	4,	2,	2,	5,	3] #Simulation



sport2 = [3,	5,	5,	2,	5,	4,	2,	2,	3,	3,	4,	5,	2,	2,	2,	4,	3,	2] #Sport
sport3 = [4,	3,	4,	2,	5,	5,	2,	4,	5,	5,	5,	5,	2,	2,	5,	5,	5,	2] #Sport
sport4 = [5,	5,	5,	3,	5,	5,	2,	2,	5,	5,	5,	5,	5,	2,	2,	2,	5,	2] #Sport
sport5 = [5,	5,	3,	1,	3,	4,	1,	1,	4,	3,	4,	5,	3,	1,	1,	5,	4,	1] #Sport
sport6 = [3,	4,	1,	1,	3,	5,	3,	3,	5,	3,	4,	5,	1,	1,	3,	4,	5,	1] #Sport
sport7 = [4,	3,	2,	1,	2,	2,	1,	3,	3,	4,	4,	5,	1,	1,	1,	5,	5,	1] #Sport
sport8 = [5,	5,	3,	1,	1,	2,	1,	4,	5,	5,	5,	5,	1,	1,	1,	5,	5,	1] #Sport
sport9 = [3,	4,	3,	4,	4,	3,	3,	4,	4,	3,	3,	4,	4,	3,	3,	4,	4,	3] #Sport $$
sport10 = [2,	5,	2,	2,	2,	5,	2,	2,	5,	3,	5,	5,	4,	2,	2,	5,	3,	2] #Sport
sport11 = [5,	5,	5,	1,	4,	4,	3,	2,	4,	3,	5,	5,	4,	2,	4,	5,	5,	2] #Sport
sport12 = [5,	5,	4,	3,	4,	4,	4,	4,	5,	3,	5,	5,	4,	2,	4,	5,	5,	4] #Moba Sport ==
sport13 = [2,	2,	1,	1,	1,	1,	1,	1,	4,	2,	3,	5,	1,	1,	1,	4,	4,	1] #Sport
sport14 = [4,	5,	1,	1,	2,	1,	1,	1,	3,	3,	2,	1,	1,	1,	2,	5,	5,	1] #Sport
sport15 = [5,	5,	2,	2,	5,	5,	5,	5,	5,	3,	5,	5,	5,	2,	2,	5,	5,	2] #Sport


Strategy2 = [2,	5,	4,	4,	4,	4,	3,	3,	5,	5,	5,	3,	4,	3,	4,	4,	3,	3] #Strategy
Strategy3 = [1,	1,	5,	1,	1,	5,	1,	5,	5,	5,	5,	1,	5,	5,	1,	5,	5,	1] #Strategy
Strategy6 = [3,	3,	5,	2,	5,	4,	3,	2,	5,	3,	5,	2,	3,	4,	3,	2,	4,	3] #Puzzle Strategy ==
Strategy8 = [5,	4,	4,	4,	3,	4,	4,	1,	5,	5,	5,	1,	3,	3,	4,	5,	5,	4] #Strategy
Strategy9 = [3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3,	3] #Strategy
Strategy10 = [5,	4,	2,	1,	1,	1,	2,	1,	5,	5,	4,	2,	3,	1,	2,	4,	3,	1] #Sport Strategy ==
Strategy11 = [1,	5,	5,	4,	3,	3,	3,	1,	5,	5,	5,	1,	1,	1,	3,	4,	5,	2] #Strategy
Strategy12 = [4,	4,	1,	4,	2,	1,	4,	1,	5,	5,	5,	1,	2,	2,	1,	5,	5,	1] #Strategy
Strategy13 = [5,	5,	1,	4,	2,	2,	4,	1,	5,	5,	5,	1,	1,	1,	2,	5,	5,	1] #Strategy
Strategy14 = [2,	2,	2,	5,	2,	2,	5,	4,	5,	5,	5,	2,	2,	4,	3,	5,	5,	2] #Strategy
Strategy16 = [4,	4,	4,	4,	4,	4,	4,	4,	5,	4,	5,	2,	2,	2,	5,	5,	5,	4] #Strategy
Strategy17 = [2,	5,	2,	4,	4,	4,	5,	1,	5,	5,	5,	1,	3,	2,	2,	1,	5,	2] #Strategy


Horror2 = [5,	5,	2,	3,	4,	4,	1,	1,	4,	5,	4,	1,	5,	4,	3,	3,	5,	3] #Horror
Horror3 = [5,	5,	4,	3,	4,	4,	1,	1,	4,	3,	3,	2,	5,	4,	3,	4,	5,	4] #Horror
Horror5 = [4,	4,	4,	3,	4,	4,	1,	1,	4,	3,	4,	1,	5,	4,	3,	2,	5,	3] #Horror
Horror6 = [4,	4,	3,	3,	5,	4,	3,	2,	4,	3,	4,	2,	5,	5,	4,	3,	4,	4] #Horror
Horror7 = [5,	5,	3,	2,	5,	3,	1,	1,	4,	3,	3,	1,	5,	4,	3,	3,	5,	4] #Horror
Horror8 = [5,	5,	4,	2,	3,	3,	1,	1,	2,	4,	2,	1,	5,	4,	2,	1,	5,	4] #Horror
Horror9 = [5,	5,	4,	1,	5,	2,	1,	1,	2,	4,	1,	1,	5,	4,	1,	1,	5,	4] #Horror
Horror10 = [5,	5,	4,	1,	5,	4,	1,	1,	3,	4,	2,	1,	5,	5,	2,	3,	5,	5] #Horror
Horror11 = [5,	5,	4,	1,	5,	3,	1,	1,	3,	5,	3,	1,	5,	5,	1,	3,	5,	5] #Horror
Horror12 = [4,	5,	5,	1,	5,	4,	1,	1,	3,	5,	3,	1,	5,	5,	1,	3,	5,	5] #Horror
Horror13 = [5,	3,	2,	3,	5,	1,	3,	3,	4,	5,	3,	1,	5,	5,	1,	1,	4,	5] #Horror
Horror14 = [5,	5,	5,	1,	5,	1,	1,	1,	2,	4,	1,	1,	5,	5,	1,	2,	5,	4] #Horror
Horror15 = [5,	5,	5,	2,	5,	3,	3,	3,	5,	5,	5,	1,	5,	5,	3,	1,	5,	5] #Horror



def Euclidian(standard,user):
    value = 0
    for i in range(len(user)):
        y = standard[i]-user[i]
        y = y**2
        value += y
    return math.sqrt(value)

EuclidianValue.append(Euclidian(Adventure,user_vector))
EuclidianValue.append(Euclidian(Fighting,user_vector))
EuclidianValue.append(Euclidian(Moba,user_vector))
EuclidianValue.append(Euclidian(Puzzle,user_vector))
EuclidianValue.append(Euclidian(RPG,user_vector))
EuclidianValue.append(Euclidian(Shooting,user_vector))
EuclidianValue.append(Euclidian(Sport,user_vector))
EuclidianValue.append(Euclidian(Simulation,user_vector))
EuclidianValue.append(Euclidian(Strategy,user_vector))
EuclidianValue.append(Euclidian(SurvivalHorror,user_vector))
        
temp = []
for i in EuclidianValue:
    temp.append(i)

temp.sort()

count = 0
for j in range(10):
        if temp[0] != EuclidianValue[j]:
            count += 1
        else:
            break
            
print(NameTypeGame[count])


count2 = 0
for k in range(10):
        if temp[1] != EuclidianValue[k]:
            count2 += 1
        else:
            break
count3 = 0
for l in range(10):
        if temp[2] != EuclidianValue[l]:
            count3 += 1
        else:
            break
print(NameTypeGame[count],NameTypeGame[count2],NameTypeGame[count3])
    
print(EuclidianValue)


    
    
    