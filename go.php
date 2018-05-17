<?php
/**
 * Created by PhpStorm.
 * go.php
 *
 * Author: Benny <benny@bennythink.com>
 * Date: 2018/5/17 14:10
 */
$_GET['name'] = 'i2p';

$host     = [ 'http://12110/', 'http://123/', 'http://1817/' ];
$relation = [
	'180422'      => '180422',
	'i2p'         => 'itwop',
	'vpngate'     => 'men',
	'psiphon3'    => 'sf',
	'tor'         => 'tao',
	'shadowsocks' => 'ys',
];

if ( isset( $relation[ $_GET['name'] ] ) ) {
	$filename = $relation[ $_GET['name'] ] . '.7z';
	echo '请求成功，即将开始下载';
	header( "refresh:1;url=" . $host[ array_rand( $host ) ] . $filename );
} else {
	echo '请求错误';
}

