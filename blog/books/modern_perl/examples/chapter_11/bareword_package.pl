use strict;
use warnings;

{
  
  package Package;
  sub method{
    print "hello, method\n";
  }
  1;
}

sub Package{
  my $obj = new Obj();
  return $obj;
}

{
  package Obj;
  sub new{
    my $proto = shift;
    my $class = ref( $proto ) || $proto;
    my $self = {};
    bless $self, $class;
  }

  sub method{
    my $self = shift;
    print "hello, method in Obj\n";
  }

  1;
}


Package->method();
Package::->method();
Package::method();





