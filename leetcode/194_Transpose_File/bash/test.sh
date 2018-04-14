awk '
{
    for (i=1;i<=NF;i++){
        if (NR == 1 ){
            print $i;
        }
    }
    
        
}' file.txt
