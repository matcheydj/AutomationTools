import os
import re
import time
import subprocess
import win32com
from win32com.client import Dispatch,constants


m=time.localtime()
y=m[0]
M=m[1]
d=m[2]

if (M<10):
    M="%02d"%M

if (d<10):
    d="%02d"%d

t=str(y)+str(M)+str(d)
des=str(M)+'/'+str(d)+'/'+str(y)
#n='U:\Reports\DailyReport\DailyReport('+t+').doc'
n='F:\tmp\tmp\DailyReport('+t+').doc'
#r=re.compile(r"2013")
def getNew(P):
    return os.listdir(P)
if os.path.exists(n):
    subprocess.call(["C:\Program Files\Microsoft Office\Office12\WINWORD.EXE",n ])
     
                    
else:
    doc=win32com.client.Dispatch('Word.Application')
    doc.Visible=0
    doc.DisplayAlerts=0
    d=doc.Documents.Open('F:/tmp/tmp/DailyReport(20131204).doc')
    r=re.compile(r'Macintosh: *None')
    ta=d.Tables(1)
    ta.Cell(Row=3,Column=2).Range.Text=4
    ta.Cell(Row=3,Column=3).Range.Text=9
    for i in d.Paragraphs:
         if re.match(r,str(i)):
            macr=i.Range
	    para=d.Paragraphs.Add()
	    para.Range.Style="No Spacing"
	    para.Range.InsertParagraphAfter()
	    files=getNew('F:\corrected')
	    table=d.Tables.Add(d.Range(i.Range.End,i.Range.End),len(files),1)
	    table.Style="Table List 5"
	    table.Rows.LeftIndent="0.96"
	    table.PreferredWidth=350
            table.Rows[0].Cells[0].Range.Style="No Spacing"
            table.Rows[0].Cells[0].Range.Font.Color=0xFF0000
            table.Rows[0].Cells[0].Range.Text=str(len(files)) + "  vulnerabilities"
#	    for i in   len(files):
	    i=1
            while i < len(files):
#	        text="text"+str(i)
                print i
#               table.Rows[i].Cells[0].Range.Font.Color=0xFF0000
                table.Rows[i].Cells[0].Range.Style="No Spacing"
                table.Rows[i].Cells[0].Range.Text=files[i-1]
                table.Rows[i].Cells[0].Range.Font.Size="9"
		i=i + 1
    doc.Selection.Find.Execute("11/28/2013", False, False, False, False, False, True, 1,True, des,2)
    doc.Selection.Find.Execute("Macintosh: None", False, False, False,
    False, False, True, 1,True, "Macintosh: Done",2)
    doc.ActiveDocument.SaveAs('F:/tmp/tmp/DailyReport('+t+').doc') 
    doc.Quit()

