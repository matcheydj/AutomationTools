use strict;
use warnings;
use Data::Dumper;
use XML::Smart;

my ($xml,$item,$f,$val,$i);
$xml=XML::Smart->new("E:/tmp/results");
$item=@{$xml->{PutResults}->{results}->{VulScanResult}};


do {
   $f=$xml->{PutResults}->{results}->{VulScanResult}[$item]->{Detected};
   if($f eq "true"){
     $val=$xml->{PutResults}->{results}->{VulScanResult}[$item]->{Vul_ID};
     print "$val    $f\n";
   $i++;
   }
   $item--;
   
}while($item);
 
print "$i \n";