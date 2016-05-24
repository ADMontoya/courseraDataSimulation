#!/usr/bin/python

import sys
import getopt
import global_vars
from initialize import *
from ad_clicks import *
from game_clicks import *
import os

# Main function file.
def main():

	print "Initializing..."
	global_vars.globalUsers = createUserDatabase(2000) #userID = index on the list
	global_vars.globalTeams = createTeamDatabase(100)  #teamID = index on the list
	global_vars.globalTeamAssignments = asssignUsersTOteams(global_vars.globalUsers, global_vars.globalTeams)
	global_vars.globalUSessions = initializeUserSessions(global_vars.globalTeamAssignments, global_vars.globalTeams)

	#auxillary functions:
	#____[1] get team members who are playing right now
	playingMembers 	= getPlayingTeamMembers(global_vars.globalUSessions, global_vars.globalTeamAssignments) # ['teamid']->[userid1, userid2,...] (have open sessions)

	#____[2] get all team members assigned to each team
	allMembers  	= getAllTeamMembers(global_vars.globalTeamAssignments) #['teamid']->[userid1, userid2,...] (all members)

	#____[3] get available team members who are assigned but not playing
	freeMembers		= getFreeTeamMembers(global_vars.globalUSessions, global_vars.globalTeamAssignments) #['teamid']->[userid1,...] (free users with no open sessions)

	#Remove old log files
	os.remove("ad-clicks.log")
	
	#start time for Day = 0
	TD = datetime.datetime.now() + datetime.timedelta(days=random.uniform(2, 3))

	# dayDuration assumed to be in hours
	dayDuration = datetime.timedelta(hours=4)

	# Write the game_clicks. TODO: Implement main function loop for team alteration.
	# Write one team for now. Ugly patchy access for now...
 	totalHits= 100
	writeGameClicksForTeam(playingMembers.values()[0], totalHits, TD)

	# *APPENDS* ad clicks to "ad-clicks.log" for current players from time = TD to time = TD+dayDuration
	writeAdClicksCSV(TD, dayDuration) # takes teamAssignments, userSessions, TeamAssignments from global variables

# Main function call hook.
if __name__ == "__main__":
	main()
