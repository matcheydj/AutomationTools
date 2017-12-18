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
#@dirs=("${di}\\AIX","${di}\\mac","${di}\\CentOS","${di}\\sles9","${di}\\rhlinux","${di}\\suse_security","${di}\\redhat_security","${di}\\solaris","${di}\\solaris2","${di}\\sun_security","${di}\\HPUX","${di}\\hp_security");
#@dirs=("${di}\\mac");
#my $xdown='/Vulnerability/Patches/Patch/@Download';
#my $xdelete="/Vulnerability/Status";
my $xpublish="/Vulnerability/PublishDate";
my $number=0;
my $file;
foreach my $dir (@dirs_mac){
while(<$dir\\V[0-9a-zA-Z_-]*.xml>){
my $tmp=$_;
#my $xp=XML::XPath->new(filename=>"$tmp");
#my $nodes=$xp->find('/Vulnerability/Patches/Patch/@UniqueFilename');
#print "$nodes \n";
my $xml=XML::LibXML->new();
my $file=$xml->parse_file("$tmp");
#my @down=$file->findnodes($xdown);
#my $delete=$file->findnodes($xdelete);
my  $publish=$file->findnodes($xpublish);
#if (defined $down[0]){
#next if ($down[0]->to_literal()=~/DManual/);
#}
#next if ($delete->to_literal=~/Deleted/);
##print "@down \n";
#my $xpath='/Vulnerability/Patches/Patch/@UniqueFilename';
#my @arr=$file->findnodes($xpath);
#my $flag=0;
#foreach (@arr){
##   print $_->to_literal."\n";
#    my $rpm=$_->to_literal;
#    next if ($rpm eq ""); 
#    $flag=1 if ($rpm !~/^\*/);
#
#}
##print "$tmp \n" if ($flag==1);
#if ($flag==1){
#	my $d=$dir;
#	$d=~s/^F:[0-9a-zA-Z\\-_]*\\([0-9a-zA-Z_]*)$/$1/;
#	print "$d \n";
#    mkdir("F:\\tmp\\tmp\\$d") if (! -e "F:\\tmp\\tmp\\$d");
#    copy($tmp,"F:\\tmp\\tmp\\$d");
#}
#    ${number}++ if($publish->to_literal=~/^2013/);
#	$file=$tmp;
#	$file=~s/.*(V_.*)$/$1/;
        $tmp=~s/.*\\(V[0-9a-zA-Z \._-]*.xml)/$1/;	
	print "$1    $tmp \n" if($publish->to_literal=~/^(2014-..-..)/); 
}
#     print "$dir is $number \n";
#	 $number=0;
}
