use strict;
use warnings;
use Data::Dumper;

use english '-no_match_vars';
# use english;

my $str = "I love you";

if ($str =~ /(love)/p) {
    print "\$` : $`\n";
    print "\$& : $&\n";
    print "\$' : $'\n";
    print "prematch: ${^PREMATCH}\n";
    print "match: ${^MATCH}\n";
    print "postmatch: ${^POSTMATCH}\n";
}
