$langs="zh-cn","zh-tw","ja-jp","da-dk","fi-fi","sv-se","nb-no","es-es","fr-fr","it-it","pl-pl","ru-ru","nl-nl","de-de","en-us"
foreach ($element in $langs){


#$url = "http://www.microsoft.com/${element}/download/details.aspx?id=43378"
$url = "http://www.microsoft.com/${element}/download/details.aspx?id=50361"
$webclient = new-object System.Net.WebClient
$webpage = $webclient.DownloadString($url)
$webpagetxt = "F://a.txt"
$webpage > "$webpagetxt"
$line=select-string -path $webpagetxt -pattern "http://.*dmg"
$dmg=$line.Matches[0].value
write-output $dmg
 
#$obj=New-Object -com "ThunderAgent.Agent.1"
#$obj.addtask("$dmg","","","","",1,"","")
#$obj.committasks2(1)
#[Diagnostics.Process]::Start('wget','$dmg')


}


