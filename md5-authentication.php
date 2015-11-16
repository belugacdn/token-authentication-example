#!/usr/bin/php
<?php
function sign_url($url, $password, $expires = false) {
    if ($expires === false) {
        $expires = time() + (60*60*12);
    }
    $parts = parse_url($url);
    if (isset($parts['query'])) {
        $sign = sprintf("%s?%s&expires=%s&pass=%s",
            $parts['path'], $parts['query'], $expires, $password);
        $new = sprintf("%s://%s%s?%s&expires=%s&token=",
            $parts['scheme'], $parts['host'], $parts['path'],
            $parts['query'], $expires);
    } else {
        $sign = sprintf("%s?expires=%s&pass=%s",
            $parts['path'], $expires, $password);
        $new = sprintf("%s://%s%s?expires=%s&token=",
            $parts['scheme'], $parts['host'], $parts['path'],
            $expires);
    }
    $token = md5($sign);
    return sprintf("%s%s", $new, $token);
}
$expires = time() + (60*60*12);
$password = "xa5aileeph6nah5ooQu";
foreach(array_slice($_SERVER['argv'], 1) as $url) {
    printf("%s\n", sign_url($url, $password, $expires));
}
