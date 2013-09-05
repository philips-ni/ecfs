use strict;
use warnings;
use 5.012;

say my $ext_num = my $extension = 42;

my $name = "philips.ni.fei";
(my $normalized_name = $name ) =~ tr/A-Za-z//dc;

say "name: $name";
say "normalized_name: $normalized_name";
