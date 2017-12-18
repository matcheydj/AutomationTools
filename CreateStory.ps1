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

# Set Strict Mode - optional
Set-StrictMode -Version 2.0

# Usually changes for each Sprint - both specific to your environment
[string] $areaPath = "Development\PowerShell"
[string] $iterationPath = "PowerShell\TFS2010"

# Usually changes for each CR
[string] $changeRequestName = "Create Task Automation PowerShell Script"
[string] $assignee = "Stafford, Gary"

# Values represent units of work, often 'man-hours'
[decimal[]] $taskEstimateArray = @(2,3,10,3,.5)
# Remaining Time is usually set to Estimated time at start (optional use of this array)
[decimal[]] $taskRemainingArray = @(2,3,10,3,.5)
# Completed Time is usually set to zero at start (optional use of this array)
[decimal[]] $tasktaskCompletedArray = @(0,0,0,0,0,0)

# Usually remains constant
# TFS Server address - specific to your environment
[string] $tfsServerString = "http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM"

# Work Item Type - specific to your environment
[string] $workItemType = "Development\Task"

[string[]] $taskNameArray = @("Analysis", "Design", "Coding", "Unit Testing", "Resolve Tasks")
[string[]] $taskDisciplineArray = @("Analysis", "Development", "Development", "Test", $null)

# Loop and create of eack of the (5) Tasks in prioritized order
[int] $i = 0

Write-Host `n`r**** Script started...`n`r

while ($i -le 4) {
    # Concatenate name of task with CR name for Title and Description fields
    $taskTitle = $taskNameArray[$i] + ": " + $changeRequestName
    
    # Build string of field parameters (key/value pairs)
    [string] $fields = "Title=$($taskTitle);Description=$($taskTitle);Assigned To=$($assignee);"
    $fields += "Area Path=$($areaPath);Iteration Path=$($iterationPath);Discipline=$($taskDisciplineArray[$i]);Priority=$($i+1);"
    $fields += "Estimate=$($taskEstimateArray[$i]);Remaining Work=$($taskRemainingArray[$i]);Completed Work=$($tasktaskCompletedArray[$i])"
    
    #For debugging - optional console output
    Write-Host $fields
    
    # Create the Task (Work Item)
    tfpt workitem /new $workItemType /collection:$tfsServerString /fields:$fields
    
    $i++
 }
 
 Write-Host `n`r**** Script completed...

