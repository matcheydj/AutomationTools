use DBI;  
use strict;  
use warnings;

 

    my $dbargs = {AutoCommit => 0,   
                  PrintError => 1};
 
  
    my $dbh = DBI->connect("dbi:SQLite:dbname=policy.db","","",$dbargs);
    
    my $sql = "SELECT * FROM active_authority";
    my $dbconn = $dbh->prepare($sql);
    $dbconn->execute();

    my (@row_ary,$cc,$bb,$dd);
    
    while (@row_ary = $dbconn->fetchrow_array ){
       my($cc,$bb,$dd) = @row_ary;
        
       print "\t@row_ary\n";
    }
   