use XML::LibXML;
use strict;
use warnings;
use Data::Dumper;
use File::Copy;
use LWP::UserAgent;

my ($xml,$doc,@nodes,@files,@qfiles,$ua,@ar);
@files=qw/V_INTL_APPLE-SP-COMBO-Le8.xml 
V_INTL_APPLE-SP-COMBO-SLe6.xml 
V_INTL_APPLE-SP-COMBO-SLe8-Server(v1.1).xml 
V_INTL_APPLE-SP-Le8-Server.xml 
V_INTL_APPLE-SP-SLe8(v1.1).xml 
V_INTL_APPLE-SP-SLe8-Server(v1.1).xml 
V_INTL_APPLE-SP-SLe8-Supp.xml 
V_ITA_OFFICE-2004-1142.xml 
V_ITA_OFFICE-2008-1221.xml 
V_ITA_OFFICE-2011-1402.xml 
V_JPN_MS04-1123-MAC.xml 
V_NLD_OFFICE-2004-1126.xml 
V_PLK_OFFICE-2011-1414.xml 
V_SVE_OFFICE-2011-1413.xml 
V_INTL_SecUpdSrvr2012-001-1.1.xml
V_INTL_MacOSXServerUpdCombo10.7.2-10.7.2.xml
V_INTL_SecUpdSrvr2012-001-1.0.xml
V_INTL_MacOSXServerUpd10.7.2-10.7.2.xml
V_INTL_SecUpd2012-001Snow-1.1.xml
V_INTL_SecUpd2012-001Snow-1.0.xml
V_INTL_MacOSXUpdCombo10.7.3-10.7.3-V2.xml
V_INTL_MacOSXUpdCombo10.7.3-10.7.3.xml
V_ENU_APPLE-Endpoint-Protection-11-AV-Pattern.xml
/;

@qfiles=map {"$_"} @files;

for (@qfiles){
    copy "Z:/mac/$_" ,"F:/scripts/" if (! -e "F:/scripts/$_" );
} 

$ua=LWP::UserAgent->new();
$xml=XML::LibXML->new();
while(<*.xml>){
   my $file=$_;
   $doc=$xml->parse_file($file);
   my $nodes=$doc->findnodes("/Vulnerability/Patches/Patch/URL");
   #$nodes=~s/.(http)/\n$1/;
   push @ar,$nodes;
    
    
  # print "$nodes \n";
   
}
my (@ars,%ars);
@ars=map {split(/(?=http)/,"$_")} @ar; 
$"="\n";
print "@ars \n";
 while(0){
for my $entry (@ars){
   my $file=$entry;
   $file=~s/.*\///;
   print "$file \n";
}
}