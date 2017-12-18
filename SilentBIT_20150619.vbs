Option Explicit

Dim WshShell, strRegValue, strHost, strTime, strLocalOutput, strRemoteOutput
Set WshShell = CreateObject("WScript.Shell")
strRegValue = "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Hostname"
strHost = WshShell.RegRead( strRegValue )
strTime = "_" & Month(Date) & "_" & Day(Date) & "_" & Year(Date) & "_" & Hour(Time) & "_" & Minute(Time) 
strLocalOutput = "C:\Windows\Temp"          
strRemoteOutput = "\\slc-datavault.ld.landesk.com\scan\"   


''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Define commands to be run
Dim strFindServ : strFindServ = "HKEY_LOCAL_MACHINE ImagePath DisplayName ServiceDLL"
Dim strImageEx : strImageEx = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
Dim strAppXP : strAppXP = "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatibility"
Dim strApp7 : strApp7 = "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache"
Dim strAutoTSComLoc : strAutoTSComLoc = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\CurrentVersion\Run"
Dim strAutoTSRunOnceComLoc : strAutoTSRunOnceComLoc = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\CurrentVersion\Runonce"
Dim strRegWinLogonUserInitLoc : strRegWinLogonUserInitLoc = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit"
Dim strRegWinLogonShellLoc : strRegWinLogonShellLoc = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell"
Dim strRegWinLogonTaskmanLoc : strRegWinLogonTaskmanLoc = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Taskman"
Dim strRegExplorerBHOLoc : strRegExplorerBHOLoc = "HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects"
Dim strWowExplorerBHOLoc : strWowExplorerBHOLoc = "HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects"
Dim strRegSessionMgrBootExecLoc : strRegSessionMgrBootExecLoc = "HKLM\System\CurrentControlSet\Control\Session Manager\BootExecute"
Dim strRegSessionMgrAppCertLoc : strRegSessionMgrAppCertLoc = "HKLM\System\CurrentControlSet\Control\Session Manager\AppCertDlls"
Dim strRegStartupDirLoc : strRegStartupDirLoc = "C:\Documents and Settings\All Users\Start Menu\Programs\Startup"
Dim strRegProgDataStartupDirLoc : strRegProgDataStartupDirLoc = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
Dim strRegVulnIELoc : strRegVulnIELoc = "HKLM\SOFTWARE\Microsoft\Internet Explorer"
Dim strVulnJavax64Loc : strVulnJavax64Loc = "C:\Program Files (x86)\Java\"
Dim strVulnJavax86Loc : strVulnJavax86Loc = "C:\Program Files\Java\"
Dim strVulnAdobe64Read11Loc : strVulnAdobe64Read11Loc = "'C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe64Acro11Loc : strVulnAdobe64Acro11Loc = "'C:\\Program Files (x86)\\Adobe\\Acrobat 11.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe64Read10Loc : strVulnAdobe64Read10Loc = "'C:\\Program Files (x86)\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe64Acro10Loc : strVulnAdobe64Acro10Loc = "'C:\\Program Files (x86)\\Adobe\\Acrobat 10.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe64Read09Loc : strVulnAdobe64Read09Loc = "'C:\\Program Files (x86)\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe64Acro09Loc : strVulnAdobe64Acro09Loc = "'C:\\Program Files (x86)\\Adobe\\Acrobat 9.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe64Read08Loc : strVulnAdobe64Read08Loc = "'C:\\Program Files (x86)\\Adobe\\Reader 8.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe64Acro08Loc : strVulnAdobe64Acro08Loc = "'C:\\Program Files (x86)\\Adobe\\Acrobat 8.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe64Read07Loc : strVulnAdobe64Read07Loc = "'C:\\Program Files (x86)\\Adobe\\Reader 7.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe64Acro07Loc : strVulnAdobe64Acro07Loc = "'C:\\Program Files (x86)\\Adobe\\Acrobat 7.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe86Read11Loc : strVulnAdobe86Read11Loc = "'C:\\Program Files\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe86Acro11Loc : strVulnAdobe86Acro11Loc = "'C:\\Program Files\\Adobe\\Acrobat 11.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe86Read10Loc : strVulnAdobe86Read10Loc = "'C:\\Program Files\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe86Acro10Loc : strVulnAdobe86Acro10Loc = "'C:\\Program Files\\Adobe\\Acrobat 10.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe86Read09Loc : strVulnAdobe86Read09Loc = "'C:\\Program Files\\Adobe\\Reader 9.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe86Acro09Loc : strVulnAdobe86Acro09Loc = "'C:\\Program Files\\Adobe\\Acrobat 9.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe86Read08Loc : strVulnAdobe86Read08Loc = "'C:\\Program Files\\Adobe\\Reader 8.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe86Acro08Loc : strVulnAdobe86Acro08Loc = "'C:\\Program Files\\Adobe\\Acrobat 8.0\\Acrobat\\Acrobat.exe'"
Dim strVulnAdobe86Read07Loc : strVulnAdobe86Read07Loc = "'C:\\Program Files\\Adobe\\Reader 7.0\\Reader\\AcroRd32.exe'"
Dim strVulnAdobe86Acro07Loc : strVulnAdobe86Acro07Loc = "'C:\\Program Files\\Adobe\\Acrobat 7.0\\Acrobat\\Acrobat.exe'"
                     
Dim strProcCommand : strProcCommand = "%comspec% /c wmic process get Caption,CommandLine,CSName,ExecutablePath,Handle,ParentProcessID,ProcessID,CreationDate,priority /format:list > """ & strLocalOutput & "\" & strHost & strTime & "_systemprocesses.pwc"""
Dim strSizeCommand : strSizeCommand = "%comspec% /c wmic partition get name, bootable, size, type /format:csv > """ & strLocalOutput & "\" & strHost & strTime & "_size.pwc"""
Dim strOSCommand : strOSCommand = "%comspec% /c wmic os get version, caption, name, registereduser, installdate /format:csv > """ & strLocalOutput & "\" & strHost & strTime & "_os.pwc"""
Dim strSysCommand : strSysCommand = "%comspec% /c WMIC computersystem get name, domain, username /format:csv > """ & strLocalOutput & "\" & strHost & strTime & "_system.pwc""" 
Dim strSrvCommand : strSrvCommand = "%comspec% /c wmic service get /format:list > """ & strLocalOutput & "\" & strHost & strTime & "_services.pwc"""
Dim strStartCommand : strStartCommand = "%comspec% /c wmic startup list full /format:csv > """ & strLocalOutput & "\" & strHost & strTime & "_startuplistfull.pwc"""
Dim strNetCommand : strNetCommand = "%comspec% /c netstat -ano > """ & strLocalOutput & "\" & strHost & strTime & "_netstat.pwc"""
Dim strSchCommand : strSchCommand = "%comspec% /c schtasks /query /v /fo list > """ & strLocalOutput & "\" & strHost & strTime & "_schtasks.pwc"""
Dim strTskDLLCommand : strTskDLLCommand = "%comspec% /c tasklist -m -fo csv > """ & strLocalOutput & "\" & strHost & strTime & "_tasklist_dll.pwc"""
Dim strTskCommand : strTskCommand = "%comspec% /c tasklist -v > """ & strLocalOutput & "\" & strHost & strTime & "_tasklist.pwc"""
Dim strDNSCommand : strDNSCommand = "%comspec% /c ipconfig /displaydns > """ & strLocalOutput & "\" & strHost & strTime & "_displaydns.pwc"""
Dim strQUseCommand : strQUseCommand = "%comspec% /c quser > """ & strLocalOutput & "\" & strHost & strTime & "_quser.pwc"""
Dim strWinCommand : strWinCommand = "%comspec% /c REG QUERY HKLM\Software\Windows\CurrentVersion\ /s > """ & strLocalOutput & "\" & strHost & strTime & "_reg_match_win_currver.pwc"""
Dim strAutoCommand : strAutoCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strAutoTSCommand : strAutoTSCommand = "%comspec% /c REG QUERY """ & strAutoTSComLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strAutoTSRunOnceCommand : strAutoTSRunOnceCommand = "%comspec% /c REG QUERY """ & strAutoTSRunOnceComLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRunCommand : strRunCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strCurrRunCommand : strCurrRunCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRunOnceCommand : strRunOnceCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strWowRunCommand : strWowRunCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strWowRunOnceCommand : strWowRunOnceCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strWowProcRunCommand : strWowProcRunCommand = "%comspec% /c REG QUERY HKLM\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegServicesCommand : strRegServicesCommand = "%comspec% /c REG QUERY HKLM\SYSTEM\CurrentControlSet\services\ /s | findstr /i """ & strFindServ & """ > """ & strLocalOutput & "\" & strHost & strTime & "_reg_services.pwc"""
Dim strRegServices001Command : strRegServices001Command = "%comspec% /c REG QUERY HKLM\SYSTEM\ControlSet001\services\ /s | findstr /i """ & strFindServ & """ >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_services.pwc"""
Dim strRegServices002Command : strRegServices002Command = "%comspec% /c REG QUERY HKLM\SYSTEM\ControlSet002\services\ /s | findstr /i """ & strFindServ & """ >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_services.pwc"""
Dim strLegacyDriversCommand : strLegacyDriversCommand = "%comspec% /c REG QUERY HKLM\SYSTEM\CurrentControlSet\Enum\Root\ /s > """ & strLocalOutput & "\" & strHost & strTime & "_legacy_drivers.pwc"""
Dim strLegacyDrivers001Command : strLegacyDrivers001Command = "%comspec% /c REG QUERY HKLM\SYSTEM\ControlSet001\Enum\Root\ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_legacy_drivers.pwc"""
Dim strLegacyDrivers002Command : strLegacyDrivers002Command = "%comspec% /c REG QUERY HKLM\SYSTEM\ControlSet002\Enum\Root\ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_legacy_drivers.pwc"""
Dim strServiceDriversCommand : strServiceDriversCommand = "%comspec% /c REG QUERY HKLM\SYSTEM\CurrentControlSet\services\ /s | findstr /i """ & strFindServ & """ > """ & strLocalOutput & "\" & strHost & strTime & "_service_drivers.pwc"""
Dim strImageExec : strImageExec = "%comspec% /c REG QUERY """ & strImageEx & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_image_execution.pwc"""
Dim strAppCompatXP : strAppCompatXP = "%comspec% /c REG QUERY """ & strAppXP & """ /s > """ & strLocalOutput & "\" & strHost & strTime & "_reg_appcompat.pwc"""
Dim strAppCompat7 : strAppCompat7 = "%comspec% /c REG QUERY """ & strApp7 & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_appcompat.pwc"""
Dim strRegExplorerRunCommand : strRegExplorerRunCommand = "%comspec% /c REG QUERY HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run /s >> """ & strLocalOutput & "\" &  strHost & strTime & "_reg_autorun.pwc"""
Dim strRegWinLogonUserInitCommand : strRegWinLogonUserInitCommand = "%comspec% /c REG QUERY """ & strRegWinLogonUserInitLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegWinLogonShellCommand : strRegWinLogonShellCommand = "%comspec% /c REG QUERY """ & strRegWinLogonShellLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegWinLogonTaskmanCommand : strRegWinLogonTaskmanCommand = "%comspec% /c REG QUERY """ & strRegWinLogonTaskmanLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegExplorerBHOCommand : strRegExplorerBHOCommand = "%comspec% /c REG QUERY """ & strRegExplorerBHOLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strWowExplorerBHOCommand : strWowExplorerBHOCommand = "%comspec% /c REG QUERY """ & strWowExplorerBHOLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegSessionMgrBootExecCommand : strRegSessionMgrBootExecCommand = "%comspec% /c REG QUERY """ & strRegSessionMgrBootExecLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegSessionMgrAppCertCommand : strRegSessionMgrAppCertCommand = "%comspec% /c REG QUERY """ & strRegSessionMgrAppCertLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strRegBootVerProgCommand : strRegBootVerProgCommand = "%comspec% /c REG QUERY HKLM\System\CurrentControlSet\Control\BootVerificationProgram\ImagePath /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
Dim strPrefetchCommand : strPrefetchCommand = "%comspec% /c DIR /B /S C:\Windows\Prefetch >> """ & strLocalOutput & strHost & strTime & "_prefetch.pwc"""
Dim strWinTempCommand : strWinTempCommand = "%comspec% /c DIR /B /S C:\Windows\Temp > """ & strLocalOutput & "\" & strHost & strTime & "_temp_files.pwc"""
Dim strRootTempCommand : strRootTempCommand = "%comspec% /c DIR /B /S C:\Temp >> """ & strLocalOutput & "\" & strHost & strTime & "_temp_files.pwc"""
Dim strRegStartupDirCommand : strRegStartupDirCommand = "%comspec% /c DIR /B /S """ & strRegStartupDirLoc & " > """ & strLocalOutput & "\" & strHost & strTime & "_reg_startup_files.pwc"""
Dim strRegProgDataStartupDirCommand : strRegProgDataStartupDirCommand = "%comspec% /c DIR /B /S """ & strRegProgDataStartupDirLoc & " >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_startup_files.pwc"""
Dim strRegVulnIECommand : strRegVulnIECommand = "%comspec% /c REG QUERY """ & strRegVulnIELoc & """  /v svcVersion > """ & strLocalOutput & "\" & strHost & strTime & "_IE_vuln.pwc"""
Dim strVulnx64JavaCommand : strVulnx64JavaCommand = "%comspec% /c DIR /B /S """ & strVulnJavax64Loc & """ | findstr java.exe > """ & strLocalOutput & "\" & strHost & strTime & "_64_Java_vuln.pwc"""
Dim strVulnx86JavaCommand : strVulnx86JavaCommand = "%comspec% /c DIR /B /S """ & strVulnJavax86Loc & """ | findstr java.exe > """ & strLocalOutput & "\" & strHost & strTime & "_86_Java_vuln.pwc"""
Dim strVulnx64FlashCommand : strVulnx64FlashCommand = "%comspec% /c DIR /B C:\Windows\SysWow64\Macromed\Flash\FlashPlayerPlugin*.exe > """ & strLocalOutput & "\" & strHost & strTime & "_64_Flash_Vuln.pwc"""
Dim strVulnx86FlashCommand : strVulnx86FlashCommand = "%comspec% /c DIR /B C:\Windows\System32\Macromed\Flash\FlashPlayerPlugin*.exe > """ & strLocalOutput & "\" & strHost & strTime & "_86_Flash_Vuln.pwc"""
Dim strVulnAdobe11Read64Command : strVulnAdobe11Read64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Read11Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_11Reader.pwc"""
Dim strVulnAdobe11Acro64Command : strVulnAdobe11Acro64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Acro11Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_11Acrobat.pwc"""
Dim strVulnAdobe10Read64Command : strVulnAdobe10Read64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Read10Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_10Reader.pwc"""
Dim strVulnAdobe10Acro64Command : strVulnAdobe10Acro64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Acro10Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_10Acrobat.pwc"""
Dim strVulnAdobe09Read64Command : strVulnAdobe09Read64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Read09Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_09Reader.pwc"""
Dim strVulnAdobe09Acro64Command : strVulnAdobe09Acro64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Acro09Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_09Acrobat.pwc"""
Dim strVulnAdobe08Read64Command : strVulnAdobe08Read64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Read08Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_08Reader.pwc"""
Dim strVulnAdobe08Acro64Command : strVulnAdobe08Acro64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Acro08Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_08Acrobat.pwc"""
Dim strVulnAdobe07Read64Command : strVulnAdobe07Read64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Read07Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_07Reader.pwc"""
Dim strVulnAdobe07Acro64Command : strVulnAdobe07Acro64Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe64Acro07Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_64_07Acrobat.pwc"""
Dim strVulnAdobe11Read86Command : strVulnAdobe11Read86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Read11Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_11Reader.pwc"""
Dim strVulnAdobe11Acro86Command : strVulnAdobe11Acro86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Acro11Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_11Acrobat.pwc"""
Dim strVulnAdobe10Read86Command : strVulnAdobe10Read86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Read10Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_10Reader.pwc"""
Dim strVulnAdobe10Acro86Command : strVulnAdobe10Acro86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Acro10Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_10Acrobat.pwc"""
Dim strVulnAdobe09Read86Command : strVulnAdobe09Read86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Read09Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_09Reader.pwc"""
Dim strVulnAdobe09Acro86Command : strVulnAdobe09Acro86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Acro09Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_09Acrobat.pwc"""
Dim strVulnAdobe08Read86Command : strVulnAdobe08Read86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Read08Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_08Reader.pwc"""
Dim strVulnAdobe08Acro86Command : strVulnAdobe08Acro86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Acro08Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_08Acrobat.pwc"""
Dim strVulnAdobe07Read86Command : strVulnAdobe07Read86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Read07Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_07Reader.pwc"""
Dim strVulnAdobe07Acro86Command : strVulnAdobe07Acro86Command = "%comspec% /c WMIC datafile where ""name =" & strVulnAdobe86Acro07Loc & """ get version >> """ & strLocalOutput & "\" & strHost & strTime & "_86_07Acrobat.pwc"""

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Run the bulk of BIT Commands
WshShell.Run strProcCommand, 0, True
WshShell.Run strSizeCommand, 0, True
WshShell.Run strOSCommand, 0, True
WshShell.Run strSysCommand, 0, True
WshShell.Run strSrvCommand, 0, True
WshShell.Run strStartCommand, 0, True
WshShell.Run strNetCommand, 0, True
WshShell.Run strSchCommand, 0, True
WshShell.Run strTskCommand, 0, True
WshShell.Run strTskDLLCommand, 0, True
WshShell.Run strDNSCommand, 0, True
WshShell.Run strQUseCommand, 0, True
WshShell.Run strWinCommand, 0, True
WshShell.Run strAutoCommand, 0, True
WshShell.Run strAutoTSCommand, 0, True
WshShell.Run strAutoTSRunOnceCommand, 0, True
WshShell.Run strRunCommand, 0, True
WshShell.Run strCurrRunCommand, 0, True
WshShell.Run strRunOnceCommand, 0, True
WshShell.Run strWowRunCommand, 0, True
WshShell.Run strWowRunOnceCommand, 0, True
WshShell.Run strWowProcRunCommand, 0, True
WshShell.Run strRegServicesCommand, 0, True
WshShell.Run strRegServices001Command, 0, True
WshShell.Run strRegServices002Command, 0, True
WshShell.Run strLegacyDriversCommand, 0, True
WshShell.Run strLegacyDrivers001Command, 0, True
WshShell.Run strLegacyDrivers002Command, 0, True
WshShell.Run strServiceDriversCommand, 0, True
WshShell.Run strImageExec, 0, True
WshShell.Run strAppCompatXP, 0, True
WshShell.Run strAppCompat7, 0, True
WshShell.Run strRegExplorerRunCommand, 0, True
WshShell.Run strRegWinLogonUserInitCommand, 0, True
WshShell.Run strRegWinLogonShellCommand, 0, True
WshShell.Run strRegWinLogonTaskmanCommand, 0, True
WshShell.Run strRegExplorerBHOCommand, 0, True
WshShell.Run strWowExplorerBHOCommand, 0, True 
WshShell.Run strRegSessionMgrBootExecCommand, 0, True
WshShell.Run strRegSessionMgrAppCertCommand, 0, True
WshShell.Run strRegBootVerProgCommand, 0, True
WshShell.Run strPrefetchCommand, 0, True
WshShell.Run strWinTempCommand, 0, True
WshShell.Run strRootTempCommand, 0, True
WshShell.Run strRegStartupDirCommand, 0, True
WshShell.Run strRegProgDataStartupDirCommand, 0, True
WshShell.Run strRegVulnIECommand, 0, True
WshShell.Run strVulnx64JavaCommand, 0, True
WshShell.Run strVulnx86JavaCommand, 0, True
WshShell.Run strVulnx64FlashCommand, 0, True
WshShell.Run strVulnx86FlashCommand, 0, True
WshShell.Run strVulnAdobe11Read64Command, 0, True
WshShell.Run strVulnAdobe11Acro64Command, 0, True
WshShell.Run strVulnAdobe10Read64Command, 0, True
WshShell.Run strVulnAdobe10Acro64Command, 0, True
WshShell.Run strVulnAdobe09Read64Command, 0, True
WshShell.Run strVulnAdobe09Acro64Command, 0, True
WshShell.Run strVulnAdobe08Read64Command, 0, True
WshShell.Run strVulnAdobe08Acro64Command, 0, True
WshShell.Run strVulnAdobe07Read64Command, 0, True
WshShell.Run strVulnAdobe07Acro64Command, 0, True
WshShell.Run strVulnAdobe11Read86Command, 0, True
WshShell.Run strVulnAdobe11Acro86Command, 0, True
WshShell.Run strVulnAdobe10Read86Command, 0, True
WshShell.Run strVulnAdobe10Acro86Command, 0, True
WshShell.Run strVulnAdobe09Read86Command, 0, True
WshShell.Run strVulnAdobe09Acro86Command, 0, True
WshShell.Run strVulnAdobe08Read86Command, 0, True
WshShell.Run strVulnAdobe08Acro86Command, 0, True
WshShell.Run strVulnAdobe07Read86Command, 0, True
WshShell.Run strVulnAdobe07Acro86Command, 0, True


''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Hash DLLs and EXEs
hashRunningProcs strHost, strLocalOutput
hashLoadedMods strHost, strLocalOutput
Dim fso, f, f1, fc
Set fso = CreateObject("Scripting.FileSystemObject") 

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Recurse profiles in C:\Users
Dim strGetUserProfileNameCommand
strGetUserProfileNameCommand = "%comspec% /c DIR /B C:\Users >> """ & strLocalOutput & "\" & strHost & strTime & "_ref_usernames.pwc"""
WshShell.Run strGetUserProfileNameCommand, 0, True
''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Recurse profile GUIDs
Dim strProfRegLoc, strProfileList, strProfileListOutput
strProfRegLoc = "HKLM\Software\Microsoft\Windows NT\CurrentVersion\ProfileList"
strProfileList = "%comspec% /c reg query """ & strProfRegLoc & """ /s /v ProfileImagePath | findstr /i """ & "S-1-5-21" & """"
strProfileListOutput = "%comspec% /c reg query """ & strProfRegLoc & """ /s /v ProfileImagePath > """ & strLocalOutput & "\" & strHost & strTime & "_ref_profiles.pwc"""
WshShell.Run strProfileListOutput, 0, True

Dim readProfiles, rawReadProfiles, arrProfiles
Set readProfiles = fso.OpenTextFile(strLocalOutput & "\" & strHost & strTime & "_ref_profiles.pwc", 1)
rawReadProfiles = readProfiles.ReadAll
readProfiles.Close
arrProfiles = Split(rawReadProfiles,vbNewLine)

Dim profileCount, x, curSID
profileCount = 0
For Each x in arrProfiles
	If len(x) > 1 Then
		If InStr(x,"HKEY_LOCAL_MACHINE") > 0 Then
			curSID = Replace(x,"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\ProfileList\","")
			If Left(curSID,8) = "S-1-5-21" Then
				profileCount = 1
			Else
				profileCount = 0
			End If
		ElseIf profileCount = 1 And InStr(x,"ProfileImagePath") > 0 Then
			Dim arrProfile
			arrProfile = Split(x,"\")
			Dim j, userName
			For Each j in arrProfile
				If len(j) > 1 Then
					userName = trim(j)
				End If
			Next
			Dim strUserTSLoc : strUserTSLoc = "HKU\" & curSID & "\Software\Microsoft\Terminal Server Client\Servers"
			Dim strUserLoadLoc : strUserLoadLoc = "HKU\" & curSID & "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\Load"
			Dim strUserNTRunLoc : strUserNTRunLoc = "HKU\" & curSID & "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\Run"
			Dim strUserAutoTSComLoc : strUserAutoTSComLoc = "HKU\" & curSID & "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\CurrentVersion\Run"
			Dim strUserAutoTSRunOnceComLoc : strUserAutoTSRunOnceComLoc = "HKU\" & curSID & "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Terminal Server\Install\Software\Microsoft\Windows\CurrentVersion\Runonce"
			Dim strUserWinLogonShellLoc : strUserWinLogonShellLoc = "HKU\" & curSID & "\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell"
			Dim strUsernameStartMenuLoc : strUsernameStartMenuLoc = "C:\users\" & userName & "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
			Dim strUsernameXPStartMenuLoc : strUsernameXPStartMenuLoc = "C:\Documents and Settings\" & userName & "\Start Menu\Programs\Startup"
			
			Dim strUsernameStartupCommand : strUsernameStartupCommand = "%comspec% /c DIR /B """ & strUsernameStartMenuLoc & """ > """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_startup_files.pwc""" 
			Dim strUsernameXPStartupCommand : strUsernameXPStartupCommand = "%comspec% /c DIR /B """ & strUsernameXPStartMenuLoc & """ >> """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_xp_startup_files.pwc"""
			Dim strUserAssistCommand : strUserAssistCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist /s > """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_userassist.pwc"""
			Dim strUserRunMRUCommand : strUserRunMRUCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /s > """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_runMRU.pwc"""
			Dim strUserRecentDocsCommand : strUserRecentDocsCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs /s > """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_recentDocs.pwc"""
			Dim strUserTSServersCommand : strUserTSServersCommand = "%comspec% /c REG QUERY """ & strUserTSLoc & """ /s > """ & strLocalOutput & "\" & strHost & strTime & "_" & userName & "_TSservers.pwc"""
			Dim strUserAutoCommand : strUserAutoCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\RunServices /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserAutoTSCommand : strUserAutoTSCommand = "%comspec% /c REG QUERY """ & strUserAutoTSComLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserAutoTSRunOnceCommand : strUserAutoTSRunOnceCommand = "%comspec% /c REG QUERY """ & strUserAutoTSRunOnceComLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserRunCommand : strUserRunCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserCurrRunCommand : strUserCurrRunCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserRunOnceCommand : strUserRunOnceCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserWowRunCommand : strUserWowRunCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserWowRunOnceCommand : strUserWowRunOnceCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserWowProcRunCommand : strUserWowProcRunCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\Wow6432Node\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserLoadCommand : strUserLoadCommand = "%comspec% /c REG QUERY """ & strUserLoadLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserNTRunCommand : strUserNTRunCommand = "%comspec% /c REG QUERY """ & strUserNTRunLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserWinLogonShellCommand : strUserWinLogonShellCommand = "%comspec% /c REG QUERY """ & strUserWinLogonShellLoc & """ /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserComDlg32MRUCommand : strUserComDlg32MRUCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU /s >> """ &  strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""
			Dim strUserComDlg32PidlMRUCommand : strUserComDlg32PidlMRUCommand = "%comspec% /c REG QUERY HKU\" & curSID & "\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU /s >> """ & strLocalOutput & "\" & strHost & strTime & "_reg_autorun.pwc"""

			            

			
			WshShell.Run strUsernameStartupCommand, 0, True
			WshShell.Run strUsernameXPStartupCommand, 0, True
			WshShell.Run strUserRecentDocsCommand, 0, True
			WshShell.Run strUserAssistCommand, 0, True
			WshShell.Run strUserRunMRUCommand, 0, True
			WshShell.Run strUserTSServersCommand, 0, True
			WshShell.Run strUserAutoCommand, 0, True
			WshShell.Run strUserAutoTSCommand, 0, True
			WshShell.Run strUserAutoTSRunOnceCommand, 0, True
			WshShell.Run strUserRunCommand, 0, True
			WshShell.Run strUserCurrRunCommand, 0, True
			WshShell.Run strUserRunOnceCommand, 0, True
			WshShell.Run strUserWowRunCommand, 0, True
			WshShell.Run strUserWowRunOnceCommand, 0, True
			WshShell.Run strUserWowProcRunCommand, 0, True
			WshShell.Run strUserLoadCommand, 0, True
			WshShell.Run strUserNTRunCommand, 0, True
			WshShell.Run strUserWinLogonShellCommand, 0, True
			WshShell.Run strUserComDlg32MRUCommand, 0, True
			WshShell.Run strUserComDlg32PidlMRUCommand, 0, True
	
			profileCount = 0
		End If
	End If
Next

''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	'Now move the output
If right(strRemoteOutput,1) <> "\" Then
	strRemoteOutput = strRemoteOutput & "\"
End If

Set f = fso.GetFolder("" & strLocalOutput & "") 
Set fc = f.Files 
For Each f1 in fc 
 If fso.getextensionname(f1) = "pwc" Then
	fso.CopyFile f1, "" & strRemoteOutput & "", True
	fso.DeleteFile f1
 End If
Next 

Function hashRunningProcs(strComputer, strOutputFolder)
	Dim objWMIService, objProcess, colProcess, objSWbemLocator

	'Get all running process through WMI
	Dim illegalList, currenProcessHash
	'WSCript.Echo "Getting all running process for - " & strComputer & " ..."

	Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
	If Err <> 0 Then
		WScript.Echo "*** Failed to create WBEMScripting.SWBemLocator object*** " & Err.Description
	End If
	Set objWMIService = objSWbemLocator.ConnectServer(strComputer,"root\cimv2", "", "")
	If Err <> 0 Then
		WSCript.Echo "***Failed to get running processes - " & Err.Description
	End If

	Dim objFSO
	Set objFSO=CreateObject("Scripting.FileSystemObject")
	If Right(strOutputFolder,1) <> "\" Then
		strOutputFolder = strOutputFolder & "\"
	End If
	
	Dim outFile
	outFile= strOutputFolder & strComputer & strTime &  "_proc_hash.pwc"
	Dim objFile
	Set objFile = objFSO.CreateTextFile(outFile,True)

	Set colProcess = objWMIService.ExecQuery("Select * from Win32_Process")
	For Each objProcess in colProcess
		currenProcessHash = ""
		If objProcess.ExecutablePath <> "" Then
		    on error resume next
			Dim currenMTime, currenATime, currenCTime, currenAttrib, currenSize
			currenProcessHash = GetFileHash(objProcess.ExecutablePath)
			currenMTime = objFSO.GetFile(objProcess.ExecutablePath).DateLastModified
			currenATime = objFSO.GetFile(objProcess.ExecutablePath).DateLastAccessed
			currenCTime = objFSO.GetFile(objProcess.ExecutablePath).DateCreated
			currenAttrib = objFSO.GetFile(objProcess.ExecutablePath).Attributes
			currenSize = objFSO.GetFile(objProcess.ExecutablePath).Size
			'Description of the numeric returns for .Attributes:
			'	http://msdn.microsoft.com/en-us/library/5tx15443(v=vs.84).aspx
			objFile.WriteLine strComputer & "	" & Trim(objProcess.ProcessID) & "	" & Trim(objProcess.Name) & "	" & Trim(objProcess.ExecutablePath) & "	" & currenProcessHash & "	" & currenMTime & "	" & currenATime & "	" & currenCTime & "	" & currenAttrib & "	" & currenSize
		End If
	Next
	
	objFile.Close
End Function

Function hashLoadedMods(strComputer, strOutputFolder)
	Dim objWMIService, objProcess, colProcess, objSWbemLocator

	'Get all running process through WMI
	Dim illegalList, currenProcessHash
	'WSCript.Echo "Getting all running process for - " & strComputer & " ..."

	Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
	If Err <> 0 Then
		WScript.Echo "*** Failed to create WBEMScripting.SWBemLocator object*** " & Err.Description
	End If
	Set objWMIService = objSWbemLocator.ConnectServer(strComputer,"root\cimv2", "", "")
	If Err <> 0 Then
		WSCript.Echo "***Failed to get running processes - " & Err.Description
	End If

	Dim objFSO
	Set objFSO=CreateObject("Scripting.FileSystemObject")
	If Right(strOutputFolder,1) <> "\" Then
		strOutputFolder = strOutputFolder & "\"
	End If
	
	Dim outFile, objFile
	outFile = strOutputFolder & strComputer & strTime &  "_mods_hash.pwc"
	Set objFile = objFSO.CreateTextFile(outFile,True)

	Dim myMod, myPID
	Set colProcess = objWMIService.ExecQuery("Select * from CIM_ProcessExecutable")
	For Each objProcess in colProcess
		currenProcessHash = ""
		myMod = Split(objProcess.Antecedent,chr(34))(1)
		myMod = Replace(myMod,(chr(92))&(chr(92)),(chr(92)))
		myPID = Split(objProcess.Dependent,chr(34))(1)
	on error resume next
		currenProcessHash = GetFileHash(myMod)
		currenMTime = objFSO.GetFile(myMod).DateLastModified
		currenATime = objFSO.GetFile(myMod).DateLastAccessed
		currenCTime = objFSO.GetFile( myMod).DateCreated
		currenAttrib = objFSO.GetFile(myMod).Attributes
		currenSize = objFSO.GetFile(myMod).Size
		'Description of the numeric returns for .Attributes:
		'	http://msdn.microsoft.com/en-us/library/5tx15443(v=vs.84).aspx
		objFile.WriteLine strComputer & "	" & Trim(myPID) & "	" & Trim(myMod) & "	" & currenProcessHash & "	" & currenMTime & "	" & currenATime & "	" & currenCTime & "	" & currenAttrib & "	" & currenSize
	Next
	
	objFile.Close
End Function

Function GetFileHash(file_name)
	Dim wi, file_hash
	Dim hash_value
	Dim i
	Set wi = CreateObject("WindowsInstaller.Installer")
	Set file_hash = wi.FileHash(file_name, 0)
	hash_value = ""
	For i = 1 To file_hash.FieldCount
	hash_value = hash_value & BigEndianHex(file_hash.IntegerData(i))
	Next
	GetFileHash = hash_value
	Set file_hash = Nothing
	Set wi = Nothing
End Function

Function BigEndianHex(Int)
	Dim result
	Dim b1, b2, b3, b4
	result = right("0000000" & Hex(Int),8)
	b1 = Mid(result, 7, 2)
	b2 = Mid(result, 5, 2)
	b3 = Mid(result, 3, 2)
	b4 = Mid(result, 1, 2)
	BigEndianHex = b1 & b2 & b3 & b4
End Function


