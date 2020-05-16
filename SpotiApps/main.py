import sys,os
from Sortify.SortMySavedList import SortMySavedList


sort = SortMySavedList()
saved_list = sort.readSavedTracks()
sort.showTracks(saved_list)

