class Subnetter:
	
	def _findSubnet(self,data):
	
		for x in range(0,len(data)):
			if data[x]=="/":
				subnetfound=data[x+1:len(data)]
				break
		return subnetfound
	
		#Searching IP data from input
	def _findIP(self,data):

		for t in range(0,len(data)):
			if data[t]=="/":
				IP=data[0:t]
		return IP

		#A function that reverses string.
	def _reverseString(self,string):
		temp=[]
		templength=len(string)
		String=""
		for i in range(len(string)):
			temp.append(string[templength-1])
			templength=templength-1
		for f in range(len(string)):
			String=String+temp[f]
		return String
	def seperator(self,IP):
		
		Temp=IP.split(".")
		return Temp 


	#The control of IP and Subnet is seperately performed.
	#If IP and Subnet enteered correctly there will be 3 points from each subcontrol mechanism.
	#First one is: Controlling IP's syntax.Count of dots.
	#Second one is: Controlling IP's numbers and syntax(words,blanks etc).IP numbers must be between 0 and 255(including).
	#Third one is: Controlling Subnet.Subnet must be between 0 and 32(including).
	def _subnetControl(self,IP,subnet,Parts):
		counter=0
		step1=0
		step2=0
		#First Step
		
		for s1 in range(len(IP)):
			if IP[s1]==".":
				step1=step1+1
		if step1==3:
			counter=counter+1
		#Second Step
		try:
			for k in range(4):
				if int(Parts[k])>=0 and int(Parts[k])<=255:
					step2=step2+1
				if step2==4:
					counter = counter+1
		except ValueError:
			print "Please enter a valid IP and a Subnet "
			exit()
		
		#Third Step
		if int(subnet)>=0 and int(subnet)<=32:
			counter=counter+1

		if counter==3:
			return True
		if counter!=3:
			return False

	#Creating SubnetMask with subnet data
	def _subnetMask(self,subnet):
		counter=3
		remaining=subnet%8
		fullpart=subnet/8
		halfpart=remaining*"1"+(8-remaining)*"0"
		halfmask=fullpart*"255."+str(int(halfpart,2))
		halfmask=halfmask+".0.0.0"
	#Detecting the dots for fullmask.
		for s in range(0,len(halfmask)):
			if halfmask[s]==".":
				counter=counter-1
			if counter==0:
				fullmask=halfmask[0:s+1]
		return fullmask

	def _broadcastID(self,parts,subnet):
		Broadcast =""
		fullpart=subnet/8
		remaining=subnet%8
		halfpart=remaining*"1"+(8-remaining)*"0"
		halfpart=256-int(halfpart,2)
		countBroadcast=4
		DefaultPart=[]
		for t in range(fullpart):
			DefaultPart.append(parts[t])
		for k in range(256/halfpart):
			if halfpart*k<=int(parts[fullpart]) and (halfpart*(k+1))-1>=int(parts[fullpart]):
				broadcastnum=(halfpart*(k+1))-1
				break
		for p in range(fullpart):		
			Broadcast=Broadcast+DefaultPart[p]+"."
		Broadcast=str(Broadcast+str(broadcastnum)+".255.255.255")
		for b in range(len(Broadcast)):
			if Broadcast[b]==".":
				countBroadcast=countBroadcast-1
			if countBroadcast==0:
				Broadcast=Broadcast[0:b]
				break
		return Broadcast



	#The networkid created from parts of the IP and the subnet data.
	def _networkID(self,parts,subnet):
		NetworkID=""
		fullpart=subnet/8
		remaining=subnet%8
		halfpart=remaining*"1"+(8-remaining)*"0"
		halfpart=256-int(halfpart,2)
		countNetworkID=4
		DefaultPart=[]
		for t in range(fullpart):
			DefaultPart.append(parts[t])
		for k in range(256/halfpart):
			if halfpart*k<=int(parts[fullpart]) and (halfpart*(k+1))-1>=int(parts[fullpart]):
				networkidnum=halfpart*k
				break
		for p in range(fullpart):		
			NetworkID=NetworkID+DefaultPart[p]+"."
		NetworkID=str(NetworkID+str(networkidnum)+".0.0.0")
			
		for n in range(len(NetworkID)):
			if NetworkID[n]==".":
				countNetworkID=countNetworkID-1
			if countNetworkID==0:
				NetworkID=NetworkID[0:n]
				break
		return NetworkID
		#Parts of SubnetMask
	def _wildCard(self,parts):
		Wildcard=""
		for i in range(4):
			Wildcard=Wildcard+str((255-int(parts[i])))+"."
		Wildcard=Wildcard[0:len(Wildcard)-1]
		return Wildcard
		#Calculating how many host can connect that network.
	def _totalHost(self,subnet):
		hostbits=32-subnet
		hosts=1
		for i in range(hostbits):
			hosts=hosts*2
		hosts=hosts-2
		return hosts






	def __init__(self,data):
				
			self.subnet=self._findSubnet(data)
			self.address=self._findIP(data)
			if int(self.subnet)==32:
				self.subnetmask=self._subnetMask(int(self.subnet))
				self.wildcard=self._wildCard(self.seperator(self.subnetmask))
				self.networkid=self.address
				self.broadcast=self.address
				self.totalhost=1


			elif self._subnetControl(self.address,self.subnet,self.seperator(self.address))==True:
				self.subnetmask=self._subnetMask(int(self.subnet))
				self.wildcard=self._wildCard(self.seperator(self.subnetmask))
				self.networkid=self._networkID(self.seperator(self.address),int(self.subnet))
				self.broadcast=self._broadcastID(self.seperator(self.address),int(self.subnet))
				self.totalhost=self._totalHost(int(self.subnet))
