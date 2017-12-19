
$objWord = New-Object -Com Word.Application


$filename = 'F:\tmp\tmp\DailyReport(20140611).doc'
#if ( ){

$doc=$objWord.Documents
$objDocument = $objWord.Documents.Open($filename) 

$paras=$objDocument.paragraphs


$contents=dir  \\172.29.140.30\vulnerabilities\mac|where-object {$_.lastwritetime -gt "6/11/2014" -and $_.name -match "^V_*"}
write-output $contents
$num=$contents.Count
write-output $num
$objWord.Selection.Find.Execute('Macintosh: None',$False,$False,$False,$False,$False,$True,1,$True,'Macintosh: Done',2)
 foreach ($par in $paras){
   $text=$par.Range.Text
  
   if ($text -Like "Macintosh: *"){
   
  
   $ran=$par.Range
   $ran.InsertParagraphAfter() 
   
   $table=$objDocument.Tables.add($objDocument.Range($par.Range.End,$par.Range.End),$num,1)
   $table.Borders.Enable=$true
   
 
   
   $count=$contents.Count.ToString() + "   vulnerabilities"
   $table.Rows.LeftIndent=65
   $table.cell(1,1).range.Style="No Spacing"
   $table.cell(1,1).range.Shading.ForegroundPatternColor=0xe5ffcc
   

   $table.PreferredWidth=350
  
   
   $table.cell(1,1).range.text=$count
 
   $r=2;$c=1
    
   foreach ($i in $contents){
    
     $table.cell($r,$c).range.Style="Normal"
     $table.cell($r,$c).range.text=$i.Name
     ++$r
 }




$objDocument.Close()
$objWord.Quit()

# Stop Winword Process
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($objWord)
  

 
break
} 

  }
  
  
#}
