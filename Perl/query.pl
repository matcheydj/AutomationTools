use strict;
use warnings;
use DBI;

my $dbargs = {AutoCommit => 1, PrintError => 1};
my $dbh = DBI->connect("dbi:SQLite:dbname=rpms.db","","",$dbargs);
print "please enter the  package name: \n\n";

while(1){
my $query=<STDIN>;
chomp $query;
$query=$dbh->quote($query);
my $pre=$dbh->prepare("select addr  from rpms where rpm like $query ");
$pre->execute or warn "fail to execute $!\n";

print $pre->fetchrow_array;
print " \n\n";

}