use strict;
use warnings;
use SVG::TT::Graph::Line;

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
        }elsif($1=~/OPENXML/){
           $patches{"Converter"}++;
           next;
        }else{
           $patches{"$1"}++;
        }
   }
   
}


  my @fields = keys %patches;
  my @data = values %patches;
  
  my $graph = SVG::TT::Graph::Line->new({
    'height' => '400',
    'width'  => '1400',
    'fields' => \@fields,
  });
  
  
  
  $graph->add_data({
    'data'  => \@data ,
    'title' => 'count',
  });
  
 # print "Content-type: image/svg+xml\n\n";
  print $graph->burn();