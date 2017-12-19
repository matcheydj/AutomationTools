use strict;
use warnings;
use XML::XPath;
use XML::LibXML;
use File::Copy;

#my $dir='F:\\committool\\PatchManagerContent\\Vulnerabilities\\rhlinux';
my $di='F:\\committool\\PatchManagerContent\\Vulnerabilities';
my @dirs_linux=("${di}\\CentOS","${di}\\sles9","${di}\\rhlinux","${di}\\suse_security","${di}\\redhat_security");
my @dirs_unix=("${di}\\AIX","${di}\\solaris","${di}\\solaris2","${di}\\sun_security","${di}\\HPUX","${di}\\hp_security");
my @dirs_mac=("${di}\\mac");


my $xpublish="/Vulnerability/PublishDate";
my $number=0;
my $file;

sub getDates {
my $d=shift;
my $f=shift;
foreach my $dir (@$d){
while(<$dir\\V[0-9a-zA-Z_-]*.xml>){
my $tmp=$_;
my $xml=XML::LibXML->new();
my $file=$xml->parse_file("$tmp");
my  $publish=$file->findnodes($xpublish);
open(my $f2,">>","$f");
$tmp=~s/.*\\(V[0-9a-zA-Z \._-]*.xml)/$1/;	
	print $f2 "$1    $tmp \n" if($publish->to_literal=~/^(2014-..-..)/); 
}
}
}


&getDates(\@dirs_mac,"mac2");
&getDates(\@dirs_linux,"linux2");
&getDates(\@dirs_unix,"unix2");
