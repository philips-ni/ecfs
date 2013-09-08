use Test::More ;
is(         4, 2 + 2, 'addition should work' );
is( 'pancake',   100, 'pancakes are numeric' );
my @cousins = qw( Rick Kristen Alex
		  Kaycee Eric Corey );
is( @cousins, 6, 'I should have only six cousins' );

done_testing();
