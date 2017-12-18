@echo off
cd /D F:\committool\PatchManagerContent\Vulnerabilities\mac

cvs admin  update
cvs update
timeout 10
rsync -t -v -r  -e "\"/cygdrive/d/program files/Grsync/bin/ssh.exe\"" /cygdrive/f/committool/PatchManagerContent/Vulnerabilities/mac/V* //172.29.150.100/vulnerabilities/mac/
timeout 5