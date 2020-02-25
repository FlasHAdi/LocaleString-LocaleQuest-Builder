__author__ = "Owsap"
__copyright__ = "Copyright 2020, Owsap Productions"
__license__ = "MIT"
__version__ = "1.0.0"

import os
import sys
import logging

LOG_FILE_NAME = "LocaleQuestBuilder.log" # Log file name
LOCALE_QUEST_FILE_NAME = "locale_quest.txt" # Locale quest file name

if not os.path.exists("log"):
	os.mkdir("log")

logging.basicConfig(filename = "log/" + LOG_FILE_NAME, level = logging.DEBUG, format = '%(asctime)s %(message)s', datefmt = '%d/%m/%Y %H:%M:%S')

def GetLocaleQuestFile(locale):
	return "locale/%s/%s" % (locale, LOCALE_QUEST_FILE_NAME)

def TranslateLocaleQuest(locale):
	localeQuestOutput = "translate_%s.lua" % locale
	if os.path.exists(localeQuestOutput):
		os.remove(localeQuestOutput)

	if not os.path.exists(GetLocaleQuestFile(locale)):
		print "%s not found." % GetLocaleQuestFile(locale)
		logging.warning("%s not found." % GetLocaleQuestFile(locale))
		return

	fileOutput = open(localeQuestOutput, 'a')
	fileOutput.write("gameforge[\"%s\"] = {}\n" % (locale))
	for line in open(GetLocaleQuestFile(locale), 'r'):
		line = line.split('\t')
		formated = line[1].replace("\"", "'")
		print "gameforge[\"%s\"][%s] = \"%s\"\n" % (locale, line[0], formated.rsplit("\n", 1)[0])
		fileOutput.write("gameforge[\"%s\"][%s] = \"%s \"\n" % (locale, line[0], formated.rsplit("\n", 1)[0]))

	fileOutput.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "USAGE: [locale]"
		locale = raw_input("Enter locale name: ")
		TranslateLocaleQuest(str(locale))

	elif len(sys.argv) == 2:
		TranslateLocaleQuest(sys.argv[1])
