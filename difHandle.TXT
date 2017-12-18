use strict;
use warnings;

my $str=<<END;
V_ENU_APPLE-Endpoint-Protection-11-AV-Pattern.xml
V_DAN_OFFICE-2011-1422.xml
V_ENU_APPLE-KasperskyAV-AutoUpdate-Status.xml
V_ENU_APPLE-KasperskyAV-Engine-RTStatus.xml
V_ENU_APPLE-KasperskyAV-Pattern.xml
V_ENU_APPLE-Messenger-7.0.2.xml
V_ENU_APPLE-Messenger-8.0.0.xml
V_ENU_APPLE-Messenger-8.0.1.xml
V_ENU_APPLE-Norton-11-AV-Pattern.xml
V_ENU_APPLE-Norton-11-AV-Pattern.xml
V_ENU_APPLE-Norton-AV-Pattern.xml
V_ENU_APPLE-SEP-Client-12.1.2015.xml
V_ENU_APPLE-Symantec-AV-10.2-Pattern.xml
V_ENU_APPLE-Symantec-AV-10.2-Pattern.xml
END

foreach (split("\n",$str)){

     system("C:\\Program Files\\UltraEdit\\uedit32.exe","V:\\mac\\$_");
}