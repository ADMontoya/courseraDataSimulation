import sys
import getopt
from initialize import *

def main():
	print "Initializing..."
	userDatabaseList = createUserDatabase(2000) #userID = index on the list
	teamDatabaseList = createTeamDatabase(100)  #teamID = index on the list
	assignmentsList = asssignUsersTOteams(userDatabaseList, teamDatabaseList)
	userSessionsList = initializeUserSessions(assignmentsList)

if __name__ == "__main__":
	main()
