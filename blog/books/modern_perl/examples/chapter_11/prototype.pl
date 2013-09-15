use strict;
use warnings;
use Data::Dumper;

sub mypush(\@@){
  my ($array, @rest) = @_;
  push @$array, @rest;
}

my @a = ( 1,2 );
mypush( @a, 3,4);
print Dumper \@a;
# mypush( my $elems = [] , 1 .. 20 );


