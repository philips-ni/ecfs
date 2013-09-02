use strict;
use warnings;
use 5.012;

my %extensions =
    (
	'001' => 'Armon',
	'002' => 'Wesley',
	'003' => 'Gerald',
	'005' => 'Rudy',
	'007' => 'Brandon',
	'008' => 'Patrick',
	'011' => 'Luke',
	'012' => 'Lamarcus',
	'017' => 'Chris',
	'020' => 'Maurice',
	'023' => 'Marcus',
	'024' => 'Andre',
	'052' => 'Greg',
	'088' => 'Nic',
    );

say for 
    map { " $_->[1], ext. $_->[0]" }
    sort { $a->[1] cmp $b->[1] }
    map { [ $_ => $extensions{$_} ]  }
    keys %extensions;
