This tool DetectRepair.py is python script. In order to run it, python (python2 or python3) must be installed. On RHEL,
SLES, CentOS , the default installation contains python interpreter. This tool can also run on Windows if Python is installed on Windows.

This tool has two command line options: --contents_dir and --prod_path. The following show the usage:

  python DetectRepair.py --contents_dir "./linux"
 
 You need to tell the script where the vulnerabilities files and the products files are, in this example, the vulnerabilities files are in the ./linux directory.

  python DetectRepair.py --prod_path  "//172.29.120.123/vulnerabilities/rhlinux"

 One vulnerability file needs many products files, In order to make the copying easy,you can first copy the vulnerabilities file to one directory, and then run the tool with the command line --prod_path which specifies the products files directory,it will find  the corresponding products files to the vulnerabilities directory. 



Change log:
2017.7.10
 Add repairing report.
  
