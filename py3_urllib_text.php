<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<titile>菜鸟教程(runoob.com) urllib POST 测试 </titile>
</head>
<body>
<from action="" method="post" name="myForm">
    Name:<input type="text" name="name"><br>
    Tag:<input type="text" name="tag"><br>
    <input type="submit" value="提交">
</form>
<hr>
<?PHP
// 使用PHP来获取表单提交的数据，你可以换成其他的
if(isset($_POST['name']) && $_POST['tag'] ){
echo $_POST['name'] . '，' .$_POST['tag'];
}
?>
</body>
</html>