use strict;
use warnings;
use File::Copy;

foreach my $f (<F:\\scripts\\python\\*.xml>){
  my $t=(stat($f))[9];
  my $d=(localtime($t))[3];
  my $m=(localtime($t))[4];
  my $today=(localtime())[3];
  my $todaym=(localtime())[4];
  if ( $todaym eq $m ){
     if ( $d eq $today ){
         print "$f   $d    $today\n";
	 copy("$f","P:\\rhel7_security") or die "failed $!"
	     
     }	  
  }
 }
