from typing import List, Dict
from utils.selector import SelectorData

warnings: List[SelectorData] = [ 
	SelectorData(
		"Creator Chose Not To Use Archive Warnings",
		1
	),
	SelectorData(
		"Graphic Depictions Of Violence",
		2
	),
	SelectorData(
		"Major Character Death",
		4
	),
	SelectorData(
		"No Archive Warnings Apply",
		8
	),
	SelectorData(
		"Rape/Non-Con",
		16
	),
	SelectorData(
		"Underage",
		32
	),
]

categories: List[SelectorData] = [ 
	SelectorData(
		"F/F",
		1
	),
	SelectorData(
		"F/M",
		2
	),
	SelectorData(
		"Gen",
		4
	),
	SelectorData(
		"M/M",
		8
	),
	SelectorData(
		"Multi",
		16
	),
	SelectorData(
		"Other",
		32
	),
]