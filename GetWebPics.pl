use strict;
use utf8;
use POE;

use LWP::UserAgent;
my $ua=LWP::UserAgent->new;
my $i=0;
sub start {
    my $addr=$_[ARG0];
    my $i=$_[ARG1];
    my $n=$_[ARG2];
    print "$addr is to start \n";
    my $res=$ua->get($addr);
    
    my $content=$res->decoded_content;
    while($content=~/.*(http:..ftp.*?.jpg).*/g){
	 $i++;
	 if($i < 11){
	 next;
	 }
        $ua->get($1,":content_file" => $n.$i.".jpg");
    }  
}

sub stop {
    print " Finished.\n"; 
}
foreach my $n  (1..28){
    my $s="http://bbs.bato.cn/thread-5703468-".$n."-1.html";
    POE::Session->create (
     inline_states=>{
       _start=> \&start,
       _stop=> \&stop,
      }, 
      args=>["$s",$i,$n],
    );
    POE::Kernel->run()
    
}

exit;
