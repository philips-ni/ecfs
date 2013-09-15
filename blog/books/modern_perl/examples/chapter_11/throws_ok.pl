use Test::More tests => 2;
use Test::Exception;

throws_ok
  { my $unobject;
    $unobject->yoink() }
  qr/Can't call method "yoink" on an undefined/,
  'Method on undefined invocant should fail';

throws_ok
  sub { my $unobject;
    $unobject->yoink() },
  qr/Can't call method "yoink" on an undefined/,
  'Method on undefined invocant should fail';

