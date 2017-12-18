#This script is used to delete all the unused Product files.
use strict;
use warnings;
use HTML::TreeBuilder;
use Data::Dumper;
use DBI;
use XML::Smart;
use File::Copy;

$|++;

my (@files,$f,$fx,$flag,$num,@ids,$id,$p,$px,$state,$statement1, $statement2,$stat,$enable,@count,$enablex,$con,@rpms,$tree,$lists,$key,$val,$link,$cs,$rpm,@ar,$li,$addr);
opendir(FH,"E:\\tmp\\tmp");

my $dbargs = {AutoCommit => 1, PrintError => 1};
my $dbh = DBI->connect("dbi:SQLite:dbname=products.db","","",$dbargs);

$dbh->do(<<EOF);
   create table if not exists products (
       product VARCHAR(255)  NOT NULL,
       state VARCHAR(255) 
       
   )
EOF
$statement1=$dbh->prepare("insert into products values(?,?)");
$statement2=$dbh->prepare("select state from products where product=?");
while ($f=readdir(FH)){
   if ($f=~/^V_.*/){

    $fx=XML::Smart->new("E:\\tmp\\tmp\\".$f);
    $state=$fx->{Vulnerability}{Status};
    if ($state ne "Enabled"){
        next;
    }
    $num=@{$fx->{Vulnerability}{Patches}{Patch}}; 
    $flag=0;
    while ($flag lt $num ){
      @ids=@{$fx->{Vulnerability}{Patches}{Patch}[$flag]{Products}{ID}}; 
      for (@ids){
                          $id=$_;
			  if ($id eq ""){
			     next;
			  }
                          $id=$dbh->quote($id);
                          $enable=$dbh->quote("enabled");
                          $statement1->execute($id, $enable);
			  print $id."   ".$enable."\n";
                                                 
      }
      $flag++;
     }
   }
}

closedir(FH);
opendir(FH2,"E:\\tmp\\tmp");
while ($p=readdir(FH2)){
   if ($p=~/^P_.*/){
   
     $px=XML::Smart->new("E:\\tmp\\tmp\\".$p);
     $stat=$px->{PatchProductXML}('[@]','Prod_ID');
     $stat=$dbh->quote($stat);
     $statement2->execute($stat);
     @count=$statement2->fetchrow_array;
    
     if ($#count lt 0){
	   move("E:\\tmp\\tmp\\".$p,"E:\\tmp\\".$p);
           print $p."\n";
     } 
   }

}

closedir(FH2);
$dbh->disconnect;
unlink "E:\\scripts\\products.db" && print "products.db is deleted \n";
#my $dbargs = {AutoCommit => 1, PrintError => 1};
#my $dbh = DBI->connect("dbi:SQLite:dbname=products.db","","",$dbargs);
#
#$dbh->do(<<EOF);
#   create table if not exists products (
#       product VARCHAR(255)  NOT NULL,
#       state VARCHAR(255) 
#       
#   )
#EOF



#$tree=HTML::TreeBuilder->new_from_file("patches.htm");
#
# 
#for  ($tree->look_down('_tag','div')){
#      $cs=$_;
#      if($cs->attr('class') eq "current"){
#         for ($cs->look_down('_tag','li')){    
#             $key=$_;                            
#             $val=$key->look_down('_tag','a');   
#             $link=$val->attr('href');           
#                                                 
#             if($link =~/buildid/){
#                    
#                    $con=HTML::TreeBuilder->new_from_url($link);
#                    @ar=$con->as_text=~/(?<=\))([a-z0-9A-Z-_.]*?\.rpm)/g;
#                     for (@ar){
#                          $rpm=$_;
#                          $rpm=$dbh->quote($rpm);
#                          $li=$dbh->quote($link);
#                          $dbh->do("insert into rpms values($rpm, $li)");
#                          print "$rpm    $li    \n\n";
#                                                 
#                      }                        
#                                
#                                   
#             }                                   
#         }                                       
#       }                                          
#                                                 
#}              
            
                                                 
 

 
