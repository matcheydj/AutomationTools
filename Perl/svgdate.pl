use strict;
use warnings;
use SVG::TT::Graph::Line;
use XML::Smart;

my (%patches,$xml,$year);
chdir "Z:/mac";

while(<V_*>){
   $xml=XML::Smart->new("$_");
   $year=$xml->{Vulnerability}->{PublishDate};
   $year=~s/^([0-9]+?)-.*/$1/;
   $patches{"$year"}++;
   }
   
my @fields =  keys %patches;
  my @data = values %patches;
  
  my $graph = SVG::TT::Graph::Line->new({
    'height' => '500',
    'width'  => '800',
    'fields' => \@fields,
  });
  
  
  
  $graph->add_data({
    'data'  => \@data,
    'title' => 'number',
  });
  

  print $graph->burn();