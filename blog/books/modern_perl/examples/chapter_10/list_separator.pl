use strict;
use warnings;
use diagnostics;
use English '-no_match_vars';

my @vals;

push @vals, "a";

push @vals, "b";


print "<$LIST_SEPARATOR>\n";

$LIST_SEPARATOR='|';


print "@vals\n";
