vul=/usr/LANDesk/ldms/vulscan
home=/usr/LANDesk/ldms
$vul -o out
#awk -F'[><]' '/Vul_ID/{a=$3;getline;getline;getline;getline;getline;getline;getline;if(/true/){sub(/-[0-9]*?$/,"",a);print a;}}' ${home}/out |uniq \
#|while read b;do
#  id=`grep -m1 "$b" out |awk -F'[><]' '{print $3}'`
#   $vul -x $id
#done

while true;do
id=`awk -F'[><]' '/Vul_ID/{a=$3;getline;getline;getline;getline;getline;getline;getline;if(/true/){print a;exit}}' ${home}/out`

   zypp=`pgrep zypper`
   if [ -z "$zypp" ];then
     $vul -x $id
   fi

   sleep 3
$vul -o out
done
