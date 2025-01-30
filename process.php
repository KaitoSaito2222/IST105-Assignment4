<?php
    $a = escapeShellarg($_POST["a"]);
    $b = escapeShellarg($_POST["b"]);
    $c = escapeShellarg($_POST["c"]);
    
    $command = escapeshellcmd("python3 calculate.py $a $b $c");
    $output = shell_exec($command);
    
    if ($output) {
        echo $output;
    } else {
        echo "Error executing Python script";
    }
?>