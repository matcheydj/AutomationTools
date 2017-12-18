dev=$(df |awk '$NF~/^\/$/{print $1}')
dname=$(sw_vers|awk -F: 'NR==2{print $2}')
diskutil rename $dev $dname
