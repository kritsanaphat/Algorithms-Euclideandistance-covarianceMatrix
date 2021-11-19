

def covariance(std1,std2):
    xbar = 0
    ybar = 0
    xmxbar = []
    ymybar = []
    cov = 0
    for i in range(18):
        xbar += std1[i]
        ybar += std2[i]
    xbar = xbar/18
    ybar = ybar/18
    for i in range(18):
        xmxbar.append(std1[i] - xbar)
        ymybar.append(std2[i] - ybar)
    for i in range(18):
        cov += xmxbar[i] * ymybar[i]
    return cov

NameTypeGame =["Adventure","Fighting","Moba","Puzzle","RPG","Shooting","Sport","Simulation","Strategy","Horror"]
    
Adventure = [4.3333,4.4667,4.2000,4.1333,4.6667,4.6000,3.8667,3.4000,4.2667,
            4.5333,4.4667,2.8667,3.5333,4.4667,3.8667,3.3333,4.6000,4.9333]   #Horror Puzzle Simulation
            
Fighting = [4.4667,4.4000,3.7333,4.2000,3.1333,3.2000,4.8000,4.7333,3.2000,
            3.6000,3.0667,2.9333,3.0667,3.2000,4.4000,3.3333,4.4667,3.0000]   #Fighting RPG Moba

Moba = [3.7647,	3.9412,	3.0000,3.8824,3.2941,4.0588,4.6471,4.2353,4.6471,
        4.0588,4.3529,2.9412,3.3529,3.6471,4.5294,4.5882,4.3529,3.0588]   #Moba Strategy Shooting

Puzzle = [2.4667,3.6667,4.7333,2.1333,4.3333,4.6667,1.7333,1.9333,4.7333,
        4.2000,4.8667,1.8000,2.1333,2.2000,3.2667,2.2667,3.9333,2.6667]  #Puzzle Horror Strategy

RPG = [4.5333,4.4000,3.8667,4.8000,4.5333,4.7333,4.7333,3.5333,3.7333,
        4.2667,3.8667,2.1333,3.0000,3.6000,4.6000,3.3333,4.6000,4.6000]  #RPG Simulation Adventure

Shooting = [3.3158,4.7895,3.0000,4.7368,3.5263,3.8947,4.8421,4.2632,4.7368,
            4.4211,4.6316,3.4211,4.2105,4.3158,4.2632,4.7368,4.4211,3.0526]  #Shooting Moba Strategy

Sport = [4.0000,4.2667,3.0000,1.9333,3.2667,3.6667,2.4000,2.8667,4.2000,
        3.5333,4.2000,4.5333,2.8667,1.6667,2.5333,4.3333,4.5333,2.0000]  #Sport Puzzle Strategy

Simulation = [4.4667,4.8667,2.2000,3.2000,3.8000,3.4000,2.8000,2.2000,1.7333,
            4.6000,3.8667,2.5333,2.8000,4.1333,2.6667,2.5333,4.6667,4.5333]  #Simulation Horror Adventure

Strategy = [3.2941,4.0588,3.5882,3.6471,3.2941,3.5294,3.8824,2.9412,4.8235,
            4.5294,4.7059,2.000,2.8824,2.9412,3.4118,4.2353,4.4706,2.9412]  #Strategy Puzzle Moba

SurvivalHorror = [4.7333,4.7333,3.8000,2.2667,4.600,3.2000,1.8000,1.6000,3.6000,
                4.0667,3.2000,1.3333,5.0000,4.6000,2.5333,2.6667,4.8667,4.2000]  #Horror Simulation Puzzle


CovarianceValue =[]

tmp = Adventure

CovarianceValue.append(covariance(Adventure,tmp))
CovarianceValue.append(covariance(Fighting,tmp))
CovarianceValue.append(covariance(Moba,tmp))
CovarianceValue.append(covariance(Puzzle,tmp))
CovarianceValue.append(covariance(RPG,tmp))
CovarianceValue.append(covariance(Shooting,tmp))
CovarianceValue.append(covariance(Sport,tmp))
CovarianceValue.append(covariance(Simulation,tmp))
CovarianceValue.append(covariance(Strategy,tmp))
CovarianceValue.append(covariance(SurvivalHorror,tmp))



temp = []
for i in CovarianceValue:
    temp.append(i)

temp.sort()
temp.reverse()

count = 0
for j in range(10):
        if temp[0] != CovarianceValue[j]:
            count += 1
        else:
            break

count2 = 0
for k in range(10):
        if temp[1] != CovarianceValue[k]:
            count2 += 1
        else:
            break
count3 = 0
for l in range(10):
        if temp[2] != CovarianceValue[l]:
            count3 += 1
        else:
            break
print(NameTypeGame[count],NameTypeGame[count2],NameTypeGame[count3])
    
print(CovarianceValue)
