<?php
require_once('class.phpmailer.php');

$mail = new PHPMailer(); //实例化
$mail->IsSMTP(); // 启用SMTP
$mail->Host = "smtp.exmail.qq.com"; //SMTP服务器 以腾讯企业邮为例子
$mail->Port = 25;  //邮件发送端口
$mail->SMTPAuth   = true;  //启用SMTP认证
$mail->SMTPSecure = "tls";
$mail->CharSet  = "UTF-8"; //字符集
$mail->Encoding = "base64"; //编码方式

$mail->Username = "no-reply@example.com";  //你的邮箱
$mail->Password = "邮箱密码";  //你的密码
$mail->Subject = "××博客更新了"; //邮件标题

$mail->From = "no-reply@example.com";  //发件人地址（也就是你的邮箱）
$mail->FromName = "Benny~";  //发件人姓名

$address = "110110@qq.com";//收件人email
$mail->AddAddress($address, "嗨");//添加收件人（地址，昵称）

//$mail->AddAttachment('xx.xls','我的附件.xls'); // 添加附件,并指定名称
$mail->IsHTML(true); //支持html格式内容
//$mail->AddEmbeddedImage("logo.jpg", "my-attach", "logo.jpg"); //设置邮件中的图片
$mail->Body = '萌月的博客已经更新，下面是diff内容<br>'.base64_decode(str_replace(" ","+",$_POST["diff"]));; //邮件主体内容
//echo $mail->Body ;

//发送

if(!$mail->Send()) {
  echo "发送失败: " . $mail->ErrorInfo;
} else {
	//$_SESSION['ip'] = get_client_ip();
	//$_SESSION['time'] = time();
  echo "1";
}

//114   168
?>
