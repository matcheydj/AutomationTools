use strict;
use warnings;
use Data::Dumper;

my %patches;
chdir "Z:/mac";

while(<V_*>){
   if(/V_[A-Z]+?_([a-zA-Z]+)/){
        if($1=~/MAC|Mac|Sec|iTunes|Safari|Quick|DST|Java/){
           $patches{"APPLE"}++;
           next;
        }elsif($1=~/Adobe/){
           $patches{"Adobe"}++;
           next;
        }else{
           $patches{"$1"}++;
        }
   }
   
}

#print Dumper(%patches);
#print "\n";
my (@names,$count);
@names=sort {$patches{$a}<=>$patches{$b}} keys(%patches);
for (@names){
      print "$_   :$patches{$_} \n ";

}