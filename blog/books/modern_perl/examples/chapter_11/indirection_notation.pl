use strict;
use warnings;
use 5.012;


my $file_name = "output.txt";
open my $fd , ">" , $file_name or die "failed to open $file_name,$!";
my $config = { output => $fd };
say {$config->{output}} 'Fun diagnostic message!';
# say $config->{output} 'Fun diagnostic message!';  #WILL NOT USE

 
