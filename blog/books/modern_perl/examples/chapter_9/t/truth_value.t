use Test::More tests => 4;
ok(   1, 'the number one should be true'         );

#ok(   0, '... and zero should not'               );
ok(  ! 0, '... and zero should not'               );

ok(  ! '', 'the empty string should be false'      );
ok( '!', '... and a non-empty string should not' );
# done_testing();
