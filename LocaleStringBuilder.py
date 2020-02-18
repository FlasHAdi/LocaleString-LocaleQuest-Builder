__author__ = "Owsap"
__copyright__ = "Copyright 2020, Owsap Productions"
__license__ = "MIT"
__version__ = "1.0.0"

import os
import sys
import logging

LOG_FILE_NAME = "LocaleStringBuilder.log" # Log file
LOCALE_STRING_FILE = "locale_string.txt" # Locale string file name
LOCALE_STRING_BASE_FILE = "share/locale_string_vnum.txt" # Reference file name (String VNUM)

if not os.path.exists("log"):
	os.mkdir("log")

logging.basicConfig(filename = "log/" + LOG_FILE_NAME, level = logging.DEBUG, format = '%(asctime)s %(message)s', datefmt = '%d/%m/%Y %H:%M:%S')

def GetLocaleStringFile(locale):
	return "locale/%s/%s" % (locale, LOCALE_STRING_FILE)

def TransalteLocaleString(locale):
	if not os.path.exists(LOCALE_STRING_BASE_FILE):
		print "Reference file not found. %s" % LOCALE_STRING_BASE_FILE
		logging.warning("Reference file not found. %s" % LOCALE_STRING_BASE_FILE)
		return

	localeStringOutput = "locale_string_%s.txt" % locale
	if os.path.exists(localeStringOutput):
		os.remove(localeStringOutput)

	fileOutput = open(localeStringOutput, 'a')
	for line in open(LOCALE_STRING_BASE_FILE, 'r'):
		split = line.split('";')
		vnum = split[0][1:]

		if not vnum:
			print ""
			fileOutput.write("")

		if not vnum.isdigit():
			formated = split[0] + "\";"
			print (formated.rsplit("\n", 1)[0])
			fileOutput.write(formated.rsplit("\n")[0] + "\n")
			continue

		print GetTranslationVnum(locale, vnum)
		fileOutput.write(GetTranslationVnum(locale, vnum) + "\n")

	fileOutput.close()

def GetTranslationVnum(locale, vnum):
	lineCount = 0
	for line in open(GetLocaleStringFile(locale), 'r'):
		lineCount += 1
		match = line.find(vnum)
		if match == 0:
			localeStringFile = open(GetLocaleStringFile(locale), 'r')
			localeText = str(localeStringFile.readlines()[lineCount - 1])
			split = localeText.split("\t")
			formated = "\"" + split[1]

			return (formated.rsplit("\n", 1)[0]) + "\";"

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: [locale]"
		locale = raw_input("Enter locale name: ")
		TransalteLocaleString(str(locale))

	elif len(sys.argv) == 2:
		TransalteLocaleString(sys.argv[1])
