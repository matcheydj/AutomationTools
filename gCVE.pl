use strict;
use warnings;

while(<DATA>){
  print $1."," if(/(CVE-[0-9]+-[0-9]+)/);
}
__DATA__
The Chrome team is delighted to announce the promotion of Chrome 40 to the stable channel for Windows, Mac and Linux. Chrome 40.0.2214.91 contains a number of fixes and improvements, including:

    Updated info dialog for Chrome app on Windows and Linux.
    A new clock behind/ahead error message.

A partial list of changes is available in the log.

Security Fixes and Rewards

Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.

This update includes 62 security fixes. Below, we highlight fixes that were contributed by external researchers. Please see the Chromium security page for more information.

[$5000][430353] High CVE-2014-7923: Memory corruption in ICU. Credit to yangdingning.
[$4500][435880] High CVE-2014-7924: Use-after-free in IndexedDB. Credit to Collin Payne.
[$4000][434136] High CVE-2014-7925: Use-after-free in WebAudio. Credit to mark.buer.
[$4000][422824] High CVE-2014-7926: Memory corruption in ICU. Credit to yangdingning.
[$3500][444695] High CVE-2014-7927: Memory corruption in V8. Credit to Christian Holler.
[$3500][435073] High CVE-2014-7928: Memory corruption in V8. Credit to Christian Holler.
[$3000][442806] High CVE-2014-7930: Use-after-free in DOM. Credit to cloudfuzzer.
[$3000][442710] High CVE-2014-7931: Memory corruption in V8. Credit to cloudfuzzer.
[$2000][443115] High CVE-2014-7929: Use-after-free in DOM. Credit to cloudfuzzer.
[$2000][429666] High CVE-2014-7932: Use-after-free in DOM. Credit to Atte Kettunen of OUSPG.
[$2000][427266] High CVE-2014-7933: Use-after-free in FFmpeg. Credit to aohelin.
[$2000][427249] High CVE-2014-7934: Use-after-free in DOM. Credit to cloudfuzzer.
[$2000][402957] High CVE-2014-7935: Use-after-free in Speech. Credit to Khalil Zhani.
[$1500][428561] High CVE-2014-7936: Use-after-free in Views. Credit to Christoph Diehl.
[$1500][419060] High CVE-2014-7937: Use-after-free in FFmpeg. Credit to Atte Kettunen of OUSPG.
[$1000][416323] High CVE-2014-7938: Memory corruption in Fonts. Credit to Atte Kettunen of OUSPG.
[$1000][399951] High CVE-2014-7939: Same-origin-bypass in V8. Credit to Takeshi Terada.
[$1000][433866] Medium CVE-2014-7940: Uninitialized-value in ICU. Credit to miaubiz.
[$1000][428557] Medium CVE-2014-7941: Out-of-bounds read in UI. Credit to Atte Kettunen of OUSPG and Christoph Diehl.
[$1000][426762] Medium CVE-2014-7942: Uninitialized-value in Fonts. Credit to miaubiz.
[$1000][422492] Medium CVE-2014-7943: Out-of-bounds read in Skia. Credit to Atte Kettunen of OUSPG.
[$1000][418881] Medium CVE-2014-7944: Out-of-bounds read in PDFium. Credit to cloudfuzzer.
[$1000][414310] Medium CVE-2014-7945: Out-of-bounds read in PDFium. Credit to cloudfuzzer.
[$1000][414109] Medium CVE-2014-7946: Out-of-bounds read in Fonts. Credit to miaubiz.
[$500][430566] Medium CVE-2014-7947: Out-of-bounds read in PDFium. Credit to fuzztercluck.
[$500][414026] Medium CVE-2014-7948: Caching error in AppCache. Credit to jiayaoqijia.


We would also like to thank Atte Kettunen of OUSPG, Christian Holler, cloudfuzzer and Khalil Zhani for working with us during the development cycle to prevent security bugs from ever reaching the stable channel. $35000 in additional rewards were issued.

As usual, our ongoing internal security work was responsible for a wide range of fixes

    [449894] CVE-2015-1205: Various fixes from internal audits, fuzzing and other initiatives.
    Multiple vulnerabilities in V8 fixed at the tip of the 3.30 branch (currently 3.30.33.15).

Many of the above bugs were detected using AddressSanitizer or MemorySanitizer.

Interested in switching release channels? Find out how. If you find a new issue, please let us know by filing a bug.
