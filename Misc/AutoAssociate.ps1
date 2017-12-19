##########################################################
#
# File:           AutoAssociate.ps1
# Author:         Elvis Chen
# Purpose:        Generate Associate file
# Version:        0.03 (21 March, 2012)
# Requirements:   Windows Powershell http://support.microsoft.com/kb/968929
#
##########################################################
Param(
[String]$AssociateDir  = "",
[String]$RemoveAsso    = "no"
)
[System.IO.DirectoryInfo]$DirectoryInfo = New-Object System.IO.DirectoryInfo $AssociateDir
foreach( $SFile In ($DirectoryInfo.GetFiles("*.xml"))) 
{
	if ($SFile.name.StartsWith("V_"))
	{
		$AssociateFile=$AssociateDir+"`\"+$SFile.name
	    # Load content file
		[System.Xml.XmlDocument] $TempXML=New-Object System.Xml.XmlDocument
	    $TempXML.Load($AssociateFile)
		$ASSPnode = $TempXML.CreateNode("element","AssociatedProducts","")
		foreach( $SFile In ($DirectoryInfo.GetFiles("*.xml"))) 
		{
			if ($SFile.name.StartsWith("P_"))
			{
				[System.Xml.XmlDocument] $TempProductXML=New-Object System.Xml.XmlDocument
				$AssociateProduct=$AssociateDir+"`\"+$SFile.name
				$TempProductXML.Load($AssociateProduct)
				$rootnode = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML"),$true)
				$Prod_ID  = $rootnode.getAttribute("Prod_ID")
				$Revision = $rootnode.getAttribute("Revision")
				$prodnode = $TempXML.CreateNode("element","prod","")
				$prodnode.setAttribute("Prod_ID",$Prod_ID)
				$prodnode.setAttribute("Revision",$Revision)
				$PDName = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/Name"),$true)
				$PDVendor = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/Vendor"),$true)
				$PDVersion = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/Version"),$true)
				$PDDetectedByFiles = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/DetectedByFiles"),$true)
				$PDDetectedByRegs = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/DetectedByRegs"),$true)
				$PDDetectedByRPMs = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/DetectedByRPMs"),$true)
				$PDDetectedByBundles = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/DetectedByBundles"),$true)
				$PDAdvanced = $TempXML.ImportNode( $TempProductXML.SelectSingleNode("/PatchProductXML/Advanced"),$true)
				$prodnode.AppendChild($PDName)
				$prodnode.AppendChild($PDVendor)
				$prodnode.AppendChild($PDVersion)
				$prodnode.AppendChild($PDDetectedByFiles)
				$prodnode.AppendChild($PDDetectedByRegs)
				$prodnode.AppendChild($PDDetectedByRPMs)
				$prodnode.AppendChild($PDDetectedByBundles)
				$prodnode.AppendChild($PDAdvanced)
				$ASSPnode.PrependChild($prodnode)
			}
		}
			$Vulnode = $TempXML.SelectSingleNode("/Vulnerability")
			$Vulnode.AppendChild($ASSPnode)
			$TempXML.save($AssociateFile)
	}
}

