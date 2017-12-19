use Data::Dumper;
#use WWW::Mechanize;
use LWP;
    my %lang=("tw"=>"zh-tw","us"=>"en-us","dk"=>"da-dk","cn"=>"zh-cn","fi"=>"fi-fi","fr"=>"fr-fr","se"=>"sv-se");
    my $ua=LWP::UserAgent->new();
    $ua->show_progress(1);
    for my $lan (keys %lang){
    my $content=$ua->get("http://www.microsoft.com/$lang{${lan}}/download/details.aspx?id=38830")->content;
    print "$1 \n" if ($content=~/.*(http:.+(Office.+.dmg)).*/); 
    system("wget.exe","$1","&");
#    $ua->default_header(charset => 'utf-8' );
#    $ua->get("$1",":content_file => $2");
    }
