AndroidRecordandReplayUI
========================

download jyson from here: http://downloads.xhaus.com/jyson/
place the .jar file in your directory so they JSON parsing in the monkeyrunner python scripts run correctly

to run replay:
monkeyrunner -plugin jyson.jar replayLogic.py logfilename.txt

-tag is to include the plug in for JSON
- by default the script looks for testLogicLog.txt if no filename is specified