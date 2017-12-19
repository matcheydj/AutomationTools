use XML::LibXML;
use XML::LibXML::PrettyPrint;
use utf8;

my $isbn   = '076455106X';

my $parser = XML::LibXML->new();

my $doc    = $parser->parse_file("V_DEU_OFFICE-2008-1232.xml");

#my $query  = "//book[isbn = '$isbn']/pages/text()";
my $query  = "/Vulnerability/Patches/Patch[1]/URL/text()";

my  ($node)  = $doc->findnodes($query);
$node->unbindNode();

my $str=$doc->toString();
$str=~s#/># />#g;
open my $fh, ">tmp.xml";
binmode $fh ,":encoding(cp932)";
print $fh "$str";
close($fh);
