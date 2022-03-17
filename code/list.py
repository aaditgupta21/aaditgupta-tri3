InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
	"FirstName": "LeBron",  
    "LastName": "James",  
	"Played_For":["Cavs","Lakers","Heat"]  
})  

InfoDb.append({  
	"FirstName": "Stephen",  
	"LastName": "Curry",  
	"Owns_Cars":["Warriors"]  
})  

InfoDb.append({  
	"FirstName": "Dwyane",  
	"LastName": "Wade",  
	"Played_For":["Heat", "Cavs", "Bulls"]  
})

print(InfoDb[0]["Played_For"][1])

