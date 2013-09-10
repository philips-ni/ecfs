use Carp;
sub only_two_arguments{
    my ($lop, $rop) = @_;
    croak( 'Too many arguments provided' ) if @_ > 2;
    print "not print this line\n";
}

only_two_arguments( 1 , 2 ,3);


