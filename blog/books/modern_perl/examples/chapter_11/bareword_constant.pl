use strict;
use warnings;
my $str = "string";
use constant  CONS => "hello,$str"; #ERROR
print "cons CONS\n";  #can not evaluate constant in double-quoted strings


