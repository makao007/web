$ts="8ABC7DLO5MN6Z9EFGdeJfghijkHIVrstuvwWSTUXYabclmnopqKPQRxyz01234";

function s52e ($n) {
    $N = strlen($ts);
    $N2= $N*$N;
    $N5= $N*5;

    $n1= strlen($n);
    $t = []

    for ($i=0; $i<$n1; $i++) {
        $a = ord($n[$i]);
        if ($a < N5) {
            array_push($t, int(a/N));
            array_push($t, a%N);
        } else {
            array_push($t, int(a/N2)+5);
            array_push($t, int(a/N)%N);
            array_push($t, a%N);
        }
    }
    $s = join("",$t);
    return strlen(strlen(s)+''+strlen(s)+s;

}


function m($y) {
    return array_search($y,$ts);
}

function s52d ($n) {
    $c = $n[0];
    if (! is_numeric ($c))
        return '';
    $cc = '';
    for ($i=1;$i<intval($c);$i++) 
        $cc += $n[$i];
    if (! is_numeric ($cc))
        return '';
    $c = intval($cc);

    $n1 = strlen($n);
    $t  = [];
    $x  = strlen($c+'')+1

    $N = strlen($ts)

    if ($n1 != $x+$c)
        return '';

    while ($x < $n1) {
        $a = m($n[$x]);
        $x += 1;
        if ($a < 5) 
            $f = $a*$N+m($n[$x]);
        else {
            $f = ($a-5)*$N*$N + m($x)*$N + m($n[$x+1]);
            $x += 1;
        }

        array_push($t, chr($f));
        $x += 1;

    }
    return join ('',$t);
}
    
        
    

