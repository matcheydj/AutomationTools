use strict;
use warnings;
use XML::Smart;
use File::Copy;
use XML::LibXML;

my @apps=("firefox","thunderbird","vlc","chrome","adium","configurator");

my $str="F:\\committool\\PatchManagerContent\\Vulnerabilities\\mac";
chdir("F:\\committool\\PatchManagerContent\\Vulnerabilities\\mac");
#my $str="/Volumes/Resources/vulnerabilities/mac";
#chdir("/Volumes/Resources/vulnerabilities/mac");
opendir(my $dir,$str);
my @fs=readdir($dir);
my ($date,$tmp,$old,$esr,$t,@olds);
my $oldfile="";
my $tmpfile="";
my $f="";
$tmp=0;
$old=0;
#foreach (@apps){
while (1){
	my $reply=shift;
	chomp $reply;
	if(@_==0){
	   $esr=shift;
	}else{
	   $esr="";
	}
	foreach my $item (@fs){
		if($item=~/V_.*$reply/i){
			next  if ($item=~/esr/i  && length($esr) == 0 );
			next  if ($item!~/esr/i  && length($esr) > 0 );
			next  if ($item=~/Firefox17/i);
			my $xml=XML::Smart->new("${str}\\$item");
			$date=$xml->{Vulnerability}->{PublishDate};
			$date=~s/T.*//;
			$date=~s/-//g;
			if($date gt  $tmp){
				$t=$tmp;
				$tmpfile=$f;
				$tmp=$date;
				$f=$item;
				if ( $old lt $t ){
					$oldfile=$tmpfile;
					$old=$t;
				}
			}
			if( $old lt $date && $date lt $tmp){
				$oldfile=$item;
				$old=$date;
			}
		} 
	}

	foreach (@olds=split(" ",$oldfile)){
	  copy("${str}\\$_","F:\\tmp\\New");
  }
	copy("${str}\\$f","F:\\tmp\\New");
	my $parser=XML::LibXML->new();
	my $x=$parser->parse_file("${str}\\$f");
	my $ids=&getp($x);
	foreach my $id (@{$ids}){

		copy("${str}\\P_${id}.xml","F:\\tmp\\New");
	} 
	$tmp=0;
	$f="";
	$date=0;
	last;
	$old=0
}

sub getp {

	my $xml=shift;
	my @ids;
	foreach my $patch ($xml->findnodes('/Vulnerability/Patches')){
		my @i=$patch->findnodes('./Patch/Products/ID');
		foreach (@i){
			push(@ids,$_->to_literal);
		}


	}
#    my $n=@{$xml->{Vulnerability}->{Patches}->{Patch}->{Products}->{ID}};
#    while($n >=1){
#         --$n;
#         push(@ids,$xml->{Vulnerability}->{Patches}->{Patch}->{Products}->{ID}[$n]);
#         
#    }
	return \@ids; 
}  
