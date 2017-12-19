#!/usr/bin/perl
use LWP::UserAgent;
use XML::Smart;
use POSIX ":sys_wait_h";
use Getopt::Std;
$|++;



my ($week,$day,$counter,$size,$empty,$t,$ua,$n,$name,$xml,$url,$f,$i,$collect);
getopts('6:');
our ($opt_6);
my ${num_proc}=0;
my ${num_collect}=0;
open fh,">>plis";
open F,">>finished";
open DIF,">>dif";
$ua=LWP::UserAgent->new();
$SIG{CHLD}=sub {${num_proc}--;};

sub compareTime {
 my $y=1900+(localtime())[5];
   my $m=sprintf("%02d",(localtime())[4]+1);
   my $d=sprintf("%02d",(localtime())[3]+1);
   my $publish=shift;
   my @p_array=split('-',$publish);
   $p_array[1]+=7;
   if ($p_array[1] >12){
     $p_array[0]+=1;
     $p_array[1]-=12;
   }
   $publish=$p_array[0].sprintf("%02d",$p_array[1]).sprintf("%02d",$p_array[2]);
   #print "$publish \n";
   my $current=$y.$m.$d;
   if ($publish <=$current){
   #    print "Publish is $publish \n";
       return 2;
   }

}
#line:while(<./vulnerabilities/V[0-9a-zA-Z_]*.xml>){
sub loop {
  line:while(1){
     $i++;
     while (1){
       $week=(localtime)[6];
       $day=(localtime)[2];
         if ($week >=1 && $week <=5){
            if ($day <18 && $day >=7){
                sleep 3600;
                print "Now it's $day o'clock, $week weekday.\n"
            }else{
                last;
            }
         }else{
            last;
         } 
         
    }
     $_=</vulnerabilities/mac/V[0-9a-zA-Z_]*.xml>;
  if (not defined $_) {
    while (${num_proc}){
        print "num of processes is ${num_proc} \n";
        sleep 20
    }
    last line;
  }
  
     $xml=$_;
  #   $empty=`grep $xml finished`;
  #   print "$empty \n";
  #   if($empty=~/xml/){
  #      undef  $empty;
  #      next;
  #   }
     print F "$xml \n";  
     $t=XML::Smart->new($xml);
     $n=@{$t->{Vulnerability}->{Patches}{Patch}};
     my $status=$t->{Vulnerability}->{Status};
     my $PublishDate=$t->{Vulnerability}->{PublishDate};
     $PublishDate=~s/([0-9]{4}-[0-9]{2}-[0-9]{2})[0-9T:.+]*/\1/;
  ;
          print "$PublishDate \n";
     if ($opt_6){
       my $ret=&compareTime($PublishDate);
       if ($ret == 2){
            unlink $xml;
            next;
       }
     }
     
     if ($status ne "Enabled"){
          unlink $xml;
          next;
     }
     $n--;
     while($n>=0){
       undef $size;undef $size2;
       my $hash=$t->{Vulnerability}->{Patches}[$n]->{Patch}->{Hash};
       $url=$t->{Vulnerability}->{Patches}[$n]->{Patch}->{URL};
       my $uniquefilename=$t->{Vulnerability}->{Patches}[$n]->{Patch}->{UniqueFilename};
       my $download=$t->{Vulnerability}->{Patches}[$n]->{Patch}->{Download};
       if ($uniquefilename eq ""){
        unlink $xml;
        next line;
       }
       if ($download eq "DManual" || $download eq ""){
          unlink $xml; 
          next line;
       }
       $n--;
       print    "${uniquefilename} | $url \n" if($url =~/http/);
       $f=fork();
       if($f==0){
         next if ($uniquefilename eq "");
        my $response=$ua->get("$url",":content_file"=>"$uniquefilename"); 
        $size=$response->header("Content-Length");
        my $size2=(stat(${uniquefilename}))[7];
        if ($size eq $size2 && $size2 !=0){
          $counter++;
         if ($n == -1 && $counter >=0){
            unlink $xml;
         } 
          my $newhash=`mono ./hashTool/get_hash.exe /MD5 "./${uniquefilename}"`;
          chomp $newhash;
          if($newhash ne $hash){
             print DIF "$xml    $newhash     $hash \n";
          }else{
               unlink ${uniquefilename};
          }
         }else{
           unlink  ${uniquefilename};
           $counter--;   
         }
        $xml=~s#.*/##;
         print fh "$xml    $uniquefilename\n"; 
        exit 0;
       }
      
     }
    
   
    $num_proc++;
       if(($i-${num_proc}-${num_collect})>0){
           while(($collect=waitpid(-1,WNOHANG))>0){
              ${num_collect}++;
           }
       }
       
       do {
          sleep 20;
          print "proc is ${num_proc} , collect is ${num_collect} \n";
          
       } until (${num_proc}<5);
       
      
  }
}

while(1){
 
     $_=</vulnerabilities/mac/V[0-9a-zA-Z_]*.xml>;
     if (defined $_){
          &loop();
     }else{
        exit 0;
     }
      
}
exit 0;




#for n in `cat filter`;do hash=`cat dif|grep $n*|awk '{print $2}'` ;sed -i 's# Hash="[0-9a-zA-Z/=]*" # Hash='"\"${hash}\""' #' /vulnerabilities/needRepaired/${n}*;echo " $hash  $n"; vim /vulnerabilities/needRepaired/${n}*; sleep 3;done

# for n in `cat filter`;do size=`stat --printf="%s" $(cat plis|grep -m 1 $n*|awk '{print $NF}')` ;sed -i 's# Size="[0-9a-zA-Z/=]*"# Size='"\"${size}\""'#' /vulnerabilities/needRepaired/${n}*;echo " $size  $n"; vim /vulnerabilities/needRepaired/${n}*; sleep 3;done

# for n in `cat filter`;do rev=`egrep -m 1 -o "Revision=[\"0-9]+"  /vulnerabilities/needRepaired/$n*` ;num=$rev;num=$(expr `echo $num|egrep -o [0-9]+` + 1);echo $rev;sed -i 's# Revision="[0-9]*"# Revision='"\"${num}\""'#' /vulnerabilities/needRepaired/${n}*; vim /vulnerabilities/needRepaired/${n}*; sleep 3;done
