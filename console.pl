use Win32::GUI;
use File::Copy;

my ($tool,$hash,$size);
$tool="E:/hashTool";
 
    $main = Win32::GUI::Window->new(
                -name   => 'Main',
                -text =>"Calculate the MD5 and Size of DMG",
                -width  => 800,
                -height => 1500,
     );
    
    my ($DOS) = Win32::GUI::GetPerlWindow();
    Win32::GUI::Hide($DOS);
   
    $main->AddListbox( 
    -text=>'Listjkdflasdfjlsdkjflksdjflksj ',
    -left   => 200,
    -top    => 50,
    -width  => 300,
    -height => 100,
    -name   => "listbox",
    );
 
   $main->AddButton(
	-name    => "search",
	-left   => 500,
	-text    => "Search",
	-top     => 50,
	-onClick => \&show,
   );

   $main->AddTextfield( -name   => "outputHash",  
      -left   => 200,                            
      -top    => 200,                            
      -width  => 300,                            
      -height => 20,                             
      -prompt => "MD5 of selected DMG:",
                                                 
      -multiline=>1,
   );                           
   $main->AddTextfield( -name   => "outputSize",  
      -left   => 200,                            
      -top    => 250,                            
      -width  => 300,                            
      -height => 20,                             
      -prompt => "Size of selected DMG:",
                                                 
      -multiline=>1,
   );                           
 
   $main->AddButton(
	-name    => "calculate",
	-left   => 500,
	-text    => "Calculate",
	-top     => 200,
	-onClick => \&cal,
  );

  $main->AddButton(
	-name    => "clear",
	-left   => 200,
	-text    => "Clear All Text",
	-top     => 800,
	-onClick => \&clear,
  );
  $main->AddButton(
	-name    => "quit",
	-left   => 400,
	-text    => "Quit",
	-top     => 800,
	-onClick => sub {exit 0},
  );

  $main->AddButton(
	-name    => "maketoc",
	-left   => 200,
	-text    => "maketoc",
	-top     => 350,
	-onClick =>\&toc, 
  );
   $main->AddTextfield( -name   => "TOCoutput",  
      -left   => 200,                            
      -top    => 400,                            
      -width  => 300,                            
      -height => 400,                             
      -prompt => "maketoc output",
                                                 
      -multiline=>1,
   );                           
   my $icon = new Win32::GUI::Icon('D:\Perl\cpan\build\Win32-GUI-1.06-WEZ1D3\guiperl.ico');
   my $ni = $main->AddNotifyIcon(
        -name => "notify",
        -icon => $icon,
        -tip => "MAC"
    );
  $main->AddButton(
	-name    => "daily report",
	-left   => 500,
	-text    => "Daily Report",
	-top     => 350,
	-onClick =>\&openDailyReport, 
  );
  $main->AddButton(
	-name    => "search content",
	-left   => 550,
	-text    => "search content",
	-top     => 450,
	-onClick =>\&findContent,
  );
   $main->AddTextfield( -name   => "app",  
      -left   => 550,                            
      -top    => 500,                            
      -width  => 80,                            
      -height => 20,                             
      -multiline=>1,
   );                           
   $main->AddTextfield( -name   => "ESR",  
      -left   => 550,                            
      -top    => 540,                            
      -width  => 80,                            
      -height => 20,                             
      -multiline=>1,
   );                           
  $main->AddButton(
	-name    => "commit tool",
	-left   => 700,
	-text    => "Commit Tool",
	-top     => 350,
	-onClick =>\&commitTool,
  );
    
 $main->Show();
 Win32::GUI::Dialog();
 
    sub Main_Minimize {
 	
        $main->Disable();
        $main->Hide();
        return 1;
    }
    
    sub notify_Click {
    	
        $main->Enable();
        $main->Show();
        return 1;
    }
    
    sub cal {
    	
    my $id=$main->listbox->GetCurSel();
    my $str=$main->listbox->GetString($id);
    $hash=`E:/hashTool/get_hash.exe /MD5 "$str"`;
	chomp $hash;
    $size=(stat($str))[7];
    $main->outputHash->Append($hash);
    $main->outputSize->Append($size);

    }
    
    sub clear {
    	
    	$main->outputHash->SelectAll();
    	$main->outputHash->Clear();
    	$main->outputSize->SelectAll();
    	$main->outputSize->Clear();
        $main->TOCoutput->SelectAll();
        $main->TOCoutput->Clear();
    	$main->app->SelectAll();
		$main->app->Clear();
    	$main->ESR->SelectAll();
		$main->ESR->Clear();
    }
    
    sub show {
    	
    	 
    	$main->listbox->Clear();
    	my (@ar,@re);
    	
    	@ar=<E://ffdownloads//*.dmg>;
    	@re=sort {(stat($b))[9] <=> (stat($a))[9]} @ar;
    	
    	for my $f (@re){
 	$main->listbox->AddString($f);
   }
   sub toc {
      open my $f,'-|','E:\tools\maketoc\MakeTOC.exe V:\mac';
      while(<$f>){
          $main->TOCoutput->Append($_);
      }
      open my $g,'-|','E:\tools\maketoc\MakeTOC.exe V:\AppleSWPackages';
      while(<$g>){
          $main->TOCoutput->Append($_);
      }
   }
   sub openDailyReport {
      system("python xls.txt");
   }
   sub commitTool {
     system('F:\committool\AdvanceCommitTool\AdvanceCommitTool.exe');
     }
   sub findContent{
	   my $ap=$main->app->Text();
	   my $esr=$main->ESR->Text();
      system("perl F:\\scripts\\searchContent.pl  $ap $esr");
#	   copy("F:\\scripts\\ab.txt","F:\\tmp\\New");
   }
}
   
