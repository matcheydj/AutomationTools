#############################################################
#
# Description: Automatically creates (5) standard Task-type
#              Work Items in TFS for a given Change Request.
#
# Author:      Gary A. Stafford
# Created:     04/12/2012
# Modified:    08/14/2012
#
#############################################################

# Clear Output Pane
clear

# Loads Windows PowerShell snap-in if not already loaded
if ( (Get-PSSnapin -Name Microsoft.TeamFoundation.PowerShell -ErrorAction SilentlyContinue) -eq $null )
{
    Add-PSSnapin Microsoft.TeamFoundation.PowerShell
}

[string] $tfsServerString = "http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM"
[Microsoft.TeamFoundation.WorkItemTracking.Client.RelatedLink] $NewLink = New-Object 
-TypeName Microsoft.TeamFoundation.WorkItemTracking.Client.RelatedLink 
-ArgumentList ($WIT.WorkItemLinkTypes.LinkTypeEnds["Test Case"], $validId)

[string][ValidateNotNullOrEmpty()] $userPassword = "Landesk08"
$userPassword = ConvertTo-SecureString -String "Landesk08" -AsPlainText -Force
$userCredential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "ld\zwang", $userPassword
$tfs=Get-TfsServer   -name "http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM"  -Credential  $userCredential -all 




