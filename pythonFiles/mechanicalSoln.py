#Importing plotting libraries
import matplotlib.pyplot as plt


#Variables for Mechanical Equation
TauM = 5 #Torque of the motor (Nm)
TauF = 1 #Torque of friction (Nm)

totalTorque = TauM - TauF

#Constants for Mechanical Equation
wheelRadius = .01 #Radius of a train wheel (m)
mu = .04 #Friction constant
mass = .25 #Mass of train (kg)
gravity = 9.82 #Gravity (m/s^2)
gamma = .5 #radius of first gear over radius of second gear
FWInertia = 4 #Inertia of the flywheel (I1) (kgm^2)
wheelInertia = 2 #Inertia of the train wheel (I2) (kgm^2)



linearAcceleration = (totalTorque + (mu*gravity*wheelRadius))/((wheelInertia/(wheelRadius*gamma))-((wheelRadius*mass)/gamma)+FWInertia)

print(linearAcceleration)


def longList(startValue, increment, endValue):
	elementNumber = endValue/increment
	returnVal = [0] * int(elementNumber + 1)
	i = 1

	while i <= elementNumber:
		returnVal[i] = increment * i
		i += 1		
	return returnVal


someVar = longList(.1,.1,5)



def calcLinearAcc(torque):
	linearAcceleration = [0] * len(torque)
	
	for i in range(1, len(torque)):
		linearAcceleration[i] = (torque[i] + (mu*gravity*wheelRadius))/((wheelInertia/(wheelRadius*gamma))-((wheelRadius*mass)/gamma)+FWInertia)
	return linearAcceleration	

acceleration = calcLinearAcc(someVar)
print(acceleration)

plt.plot(someVar, acceleration)
plt.show()
	
