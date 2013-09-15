use strict;
use warnings;
use Data::Dumper;

sub length_sort ($$)
# sub length_sort
{
  my( $left, $right ) = @_;

  return length( $left ) <=> length( $right );

}

my @unsorted = qw(
                   hello
                   good
                   message
                   world
                   Symantec
               );

my @sorted = sort  {length_sort}  @unsorted;
print Dumper \@sorted;

