cd /Volumes/content/david/rhsec
rm -f V_INTL_RHEL6-System-06-01-{0[2-9],1[0-9]}.xml
for  s in `seq 2 11`;do
    if [ $s -lt 10 ]; then 
       cp -v V_INTL_RHEL6-System-06-01-01.xml  V_INTL_RHEL6-System-06-01-0${s}.xml; 
      sed -i.bak 's/RHEL6-System-06-01-01/RHEL6-System-06-01-0'"${s}"'/' V_INTL_RHEL6-System-06-01-0${s}.xml ;
    else
       cp -v V_INTL_RHEL6-System-06-01-01.xml V_INTL_RHEL6-System-06-01-${s}.xml; 
      sed -i.bak  's/RHEL6-System-06-01-01/RHEL6-System-06-01-'"${s}"'/'  V_INTL_RHEL6-System-06-01-${s}.xml;
     fi
done
rm -f *bak
