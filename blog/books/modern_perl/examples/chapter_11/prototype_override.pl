use subs 'push';
# sub push (\@@) {
use Data::Dumper;

sub push{
  print "hello,push\n";
}
my @a = ( 1, 2);
push(@a,3);

print Dumper \@a;
