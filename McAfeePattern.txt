#!/bin/bash
declare -i detected=0[LF] 
expectedversion=9095.0000[LF] 
engexpectedversion=5400.1158[LF] 


dataversionstr=$(defaults read /Library/Preferences/com.mcafee.ssm.antimalware Update_DATVersion)[LF]

if [ ${dataversionstr%%.*} -lt ${expectedversion%%.*} ]; then[LF]

detected=1[LF]

elif [ ${dataversionstr%%.*} -eq ${expectedversion%%.*} -a ${dataversionstr##*.} -lt ${expectedversion##*.} ]; then[LF]

detected=1[LF]
fi[LF]

engdataversionstr=$(defaults read /Library/Preferences/com.mcafee.ssm.antimalware Update_EngineVersion)[LF]

if [ ${engdataversionstr%%.*} -lt ${engexpectedversion%%.*} ]; then[LF]

detected=1[LF]

elif [ ${engdataversionstr%%.*} -eq ${engexpectedversion%%.*} -a ${engdataversionstr##*.} -lt ${engexpectedversion##*.} ]; then[LF]

detected=1[LF]
fi[LF]

echo "Detected:$detected"[LF]

if [ "$detected" == "1" ]; then[LF]

echo "Reason: The latest pattern files v$expectedversion  do not exist!"[LF]

echo "Expected: The latest pattern files v$expectedversion should exist! "[LF]

echo "Found:The latest pattern files v$expectedversion do not exist"[LF]
fi[LF]

exit 0[LF]

