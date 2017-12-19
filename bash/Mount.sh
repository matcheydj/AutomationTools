grep auto_resources /etc/auto_master
if [ $? -ne 0 ];then
   echo "/Volumes/Resources   auto_resources" >>/etc/auto_master
fi
if [ ! -e "/etc/auto_resources" ];then
    echo "content -fstype=smbfs   ://content:password@172.29.150.129/content"   >/etc/auto_resources
    echo "vulnerabilities -fstype=smbfs   ://content:!LANDesk123@172.29.150.129/vulnerabilities" >>/etc/auto_resources
fi
automount -vc
open /Volumes/Resources/content
open /Volumes/Resources/vulnerabilitiest

