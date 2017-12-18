use strict;
use warnings;

my ($cve11,$cve10,$cve9,$cve12,$eleven,$ten,$nine,$e,$t,$n);
while(<DATA>){
  
   if($e and $t and $n){
    if(/(CVE-[0-9]{4}-[0-9]{4})/)
     {
      $cve11.=$1.",";
      $cve10.=$1.",";
      $cve9.=$1.",";
      next;
     }
  }
   if($e and $t){
    if(/(CVE-[0-9]{4}-[0-9]{4})/)
     {
      $cve11.=$1.",";
      $cve10.=$1.",";
      next;
     }
  }
   if($e){
    if(/(CVE-[0-9]{4}-[0-9]{4})/)
     {
      $cve11.=$1.",";
      next;
     }
  }
   if($n){
    if(/(CVE-[0-9]{4}-[0-9]{4})/)
     {
      $cve12.=$1.",";
      next;
     }
  }
  if(/Available for:/){
   if(/10.11/){
    $e=2; 
  }else{
    undef $e;
  }
  if(/10.10/){
    $t=2; 
  }else{
    undef $t;
 }
   if(/10.12/){
    $n=2;    
  }else{
    undef $n;
   }
  } 
}

print "10:11   $cve11\n\n\n";
print "10:10:  $cve10 \n\n\n";
print "10:12  $cve12  \n";
__DATA__
802.1X
Available for: macOS Sierra 10.12.4
Impact: A malicious network with 802.1X authentication may be able to capture user network credentials
Description: A certificate validation issue existed in EAP-TLS when a certificate changed. This issue was addressed through improved certificate validation.
CVE-2017-6988: Tim Cappalli of Aruba, a Hewlett Packard Enterprise company
Accessibility Framework
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain system privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-6978: Ian Beer of Google Project Zero
CoreAnimation
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: Processing maliciously crafted data may lead to arbitrary code execution
Description: A memory consumption issue was addressed through improved memory handling.
CVE-2017-2527: Ian Beer of Google Project Zero
CoreAudio
Available for: macOS Sierra 10.12.4
Impact: An application may be able to read restricted memory
Description: A validation issue was addressed with improved input sanitization.
CVE-2017-2502: Yangkang (@dnpushme) of Qihoo360 Qex Team
DiskArbitration
Available for: macOS Sierra 10.12.4 and OS X El Capitan 10.11.6
Impact: An application may be able to gain system privileges
Description: A race condition was addressed with additional filesystem restrictions.
CVE-2017-2533: Samuel Gros and Niklas Baumstark working with Trend Micro's Zero Day Initiative
HFS
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to read restricted memory
Description: A validation issue was addressed with improved input sanitization.
CVE-2017-6990: Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
iBooks
Available for: macOS Sierra 10.12.4
Impact: A maliciously crafted book may open arbitrary websites without user permission
Description: A URL handling issue was addressed through improved state management.
CVE-2017-2497: Jun Kokatsu (@shhnjk)
iBooks
Available for: macOS Sierra 10.12.4
Impact: An application may be able to execute arbitrary code with root privileges
Description: An issue existed within the path validation logic for symlinks. This issue was addressed through improved path sanitization.
CVE-2017-6981: evi1m0 of YSRC (sec.ly.com)
iBooks
Available for: macOS Sierra 10.12.4
Impact: An application may be able to escape its sandbox
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-6986: evi1m0 of YSRC (sec.ly.com) & Heige (SuperHei) of Knownsec 404 Security Team
Intel Graphics Driver
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2503:?sss and Axis of 360Nirvan team
IOGraphics
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2545: 360 Security (@mj0011sec) working with Trend Micro's Zero Day Initiative
IOSurface
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-6979: Adam Donenfeld of Zimperium zLabs
Kernel
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2494: Jann Horn of Google Project Zero
Kernel
Available for: macOS Sierra 10.12.4
Impact: An application may be able to execute arbitrary code with kernel privileges
Description: A race condition was addressed through improved locking.
CVE-2017-2501: Ian Beer of Google Project Zero
Kernel
Available for: macOS Sierra 10.12.4
Impact: An application may be able to read restricted memory
Description: A validation issue was addressed with improved input sanitization.
CVE-2017-2507: Ian Beer of Google Project Zero
CVE-2017-2509: Jann Horn of Google Project Zero
CVE-2017-6987: Patrick Wardle of Synack
Kernel
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to read restricted memory
Description: A validation issue was addressed with improved input sanitization.
CVE-2017-2516: Jann Horn of Google Project Zero
Kernel
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2546: Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
Multi-Touch
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2542: 360 Security (@mj0011sec) working with Trend Micro's Zero Day Initiative
CVE-2017-2543: 360 Security (@mj0011sec) working with Trend Micro's Zero Day Initiative
NVIDIA Graphics Drivers
Available for: macOS Sierra 10.12.4
Impact: An application may be able to gain kernel privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-6985: Axis and sss of Nirvan Team of Qihoo 360 and Simon Huang (@HuangShaomang) of IceSword Lab of Qihoo 360
Sandbox
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to escape its sandbox
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2512: Federico Bento of Faculty of Sciences, University of Porto
Security
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to escape its sandbox
Description: A resource exhaustion issue was addressed through improved input validation.
CVE-2017-2535: Samuel Gros and Niklas Baumstark working with Trend Micro's Zero Day Initiative
Speech Framework
Available for: macOS Sierra 10.12.4
Impact: An application may be able to escape its sandbox
Description: An access issue was addressed through additional sandbox restrictions.
CVE-2017-2534: Samuel Gros and Niklas Baumstark working with Trend Micro's Zero Day Initiative
Speech Framework
Available for: macOS Sierra 10.12.4
Impact: An application may be able to escape its sandbox
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-6977:?Samuel Gros and Niklas Baumstark working with Trend Micro's Zero Day Initiative
SQLite
Available for: macOS Sierra 10.12.4
Impact: A maliciously crafted SQL query may lead to arbitrary code execution
Description: A use after free issue was addressed through improved memory management.
CVE-2017-2513: found by OSS-Fuzz
SQLite
Available for: macOS Sierra 10.12.4
Impact: A maliciously crafted SQL query may lead to arbitrary code execution
Description: A buffer overflow issue was addressed through improved memory handling.
CVE-2017-2518: found by OSS-Fuzz
CVE-2017-2520: found by OSS-Fuzz
SQLite
Available for: macOS Sierra 10.12.4
Impact: A maliciously crafted SQL query may lead to arbitrary code execution
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2519: found by OSS-Fuzz
SQLite
Available for: macOS Sierra 10.12.4
Impact: Processing maliciously crafted web content may lead to arbitrary code execution
Description: Multiple memory corruption issues were addressed with improved input validation.
CVE-2017-6983: Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
CVE-2017-6991: Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
TextInput
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: Parsing maliciously crafted data may lead to arbitrary code execution
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2524: Ian Beer of Google Project Zero
WindowServer
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to gain system privileges
Description: A memory corruption issue was addressed with improved memory handling.
CVE-2017-2537: Chaitin Security Research Lab (@ChaitinTech) working with Trend Micro's Zero Day Initiative
CVE-2017-2541: Richard Zhu (fluorescence) working with Trend Micro's Zero Day Initiative
CVE-2017-2548: Team Sniper (Keen Lab and PC Mgr) working with Trend Micro's Zero Day Initiative
WindowServer
Available for: macOS Sierra 10.12.4, OS X El Capitan 10.11.6, and OS X Yosemite 10.10.5
Impact: An application may be able to read restricted memory
Description: A validation issue was addressed with improved input sanitization.
CVE-2017-2540: Richard Zhu (fluorescence) working with Trend Micro's Zero Day Initiative
