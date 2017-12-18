from lxml import etree
import re,wx,os,sys
import paramiko
from scp  import SCPClient

def getScript(file):
    
    S=""
    fileobj=etree.parse(file)
    select=list.GetSelection()
    if list.GetString(select)=="detect":
        script=fileobj.xpath("/Vulnerability/Patches/Patch/Advanced/DetectScript")
        for n in script:
            S=n.text.replace("[LF]","\n").replace("[QUOT]","\"").replace("[APOS]","\`")
    else:
        script=fileobj.xpath("/Vulnerability/Patches/Patch/Cmds/Cmd/Args/Arg")
        for n in script:
            S=n.attrib['V']
            
    return S    

def fillText(a):
    name=content_file.GetValue()
    val=getScript("Y:/david/rhsec/"+name)
    combo.SetValue(val)

def sendFile(b):
    f=file('z','w')
    f.write(combo.GetValue())
    f.close()
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("172.29.150.66", port=22, username="david", password="landesk",key_filename="F:/scripts/keys.txt")    

    scp=SCPClient(ssh.get_transport())
    scp.put('z','/tmp')
    os.remove('z')

def saveFile(f):
    fileobj=etree.parse("V:/redhat_security/"+content_file.GetValue())
    select=list.GetSelection()
    if list.GetString(select)=="detect":
        for n in fileobj.xpath("/Vulnerability/Patches/Patch/Advanced/DetectScript"):
            n.text=combo.GetValue()
            fileobj.write("E:/tools/Newvuledit/"+content_file.GetValue())
    else:
        script=fileobj.xpath("/Vulnerability/Patches/Patch/Cmds/Cmd/Args/Arg")
        for n in script:
            n.attrib['V']=combo.GetValue()
            fileobj.write("E:/tools/Newvuledit/"+content_file.GetValue())
  
    


app=wx.App()
frame=wx.Frame(None,title="test")
frame.Show()
#content_name=wx.StaticText(frame,label="Content File",pos=(5,30))
#content_name.Show()
button=wx.Button(frame,label="Script",pos=(400,2))
button.Bind(wx.EVT_BUTTON,fillText,button)
list=wx.ListBox(frame,-1)
list.Show(True)

list.Insert("detect",0)
list.Insert("repair",1)



content_file=wx.TextCtrl(frame,-1,pos=(180,2),size=(190,-1))
content_file.Show()
button2=wx.Button(frame,label="Send",pos=(800,800))
button2.Bind(wx.EVT_BUTTON,sendFile,button2)

button3=wx.Button(frame,label="Save",pos=(800,900))
button3.Bind(wx.EVT_BUTTON,saveFile,button3)
combo=wx.TextCtrl(frame,-1,pos=(-1,50),size=(800,800),style=wx.TE_MULTILINE)
combo.Show()
app.MainLoop()


