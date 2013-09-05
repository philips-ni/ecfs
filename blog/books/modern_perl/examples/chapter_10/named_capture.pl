use feature 'say';
use Data::Dumper;


my $test = 'abc1234asf';


$test =~ /(?<one>\w{4})(?<two>\w{4})/;


#say 'one:', $+{one};            #works
#say 'two:', $+{two};
print Dumper \%+;


$test =~ s/(?<three>\w{4})(?<four>\w{4})/$+{four}$+{three}/;

print Dumper \%+;

say 'one:', $+{one};            #NOT works
say 'two:', $+{two};

say;

say 'three:', $+{three};

say 'four:', $+{four};

say;

say 'output:', $test;
