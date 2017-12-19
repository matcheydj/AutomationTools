use strict;
use warnings;
use XML::Smart;
use File::Copy;

my ($count,$name,$smart,$type, $url,$filename);
my ($new, $old);
while(0){
   chomp;
  
  # print "$_ \n";
   if (/exist/){
       ($name)=split " ";
     # print "$name \n";
       $smart=XML::Smart->new("Z:/mac/${name}");
       $type=$smart->{Vulnerability}->{Patches}[0]->{Patch}->{Download};
       $url=$smart->{Vulnerability}->{Patches}[0]->{Patch}->{URL};
     #  printf "%-52s  %s\n", $name,$type if ($type eq "DAuto");
   }
   else {
      ($name,$new,$old)=split;
      printf "%-40s   %25s   %25s\n",$name,$new,$old;
   
   }
}

while(0){
my @flist=qw/V_INTL_APPLE-SP-SLe6.xml                
V_INTL_APPLE-SP-SLe7-Server.xml         
V_INTL_APPLE-SP-SLe7.xml                

      

/;
for (@flist){
    chomp;
    
    system("C:/Program Files/UltraEdit/uedit32.exe","Z:/mac/$_");
    sleep 20;
}

}

my $val=0;
unless(0){
  print "the value is $val \n";
}
#my $f;
my @ar=qw/V_NOR_OFFICE-2008-1227.xml
V_RUS_OFFICE-2011-1422.xml
V_SVE_OFFICE-2004-1126.xml 
V_SVE_OFFICE-2008-1227.xml 
/;
#my ($count,$name,$smart,$type, $url);
#my ($new, $old);
while(0){
for my $f (@ar){
  
  $name=XML::Smart->new("Z:/mac/$f");
  $filename=$name->{Vulnerability}->{Patches}[0]->{Patch}->{UniqueFilename};
  $type=$name->{Vulnerability}->{Patches}[0]->{Patch}->{Download};
  #copy "Z:/mac/$f","./new/" or die "copy failed $!";
   if($type eq "DAuto"){
   print "$f"."   "."$filename \n";
  }
}
}
for my $f (@ar){
   system("C:/Program Files/UltraEdit/uedit32.exe","Z:/mac/$f");
   sleep 10;
}


