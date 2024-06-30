function isRight(pwd) {
    if (pwd == "ddx110509") {
        return true
    } else {
        return false;
    }
}
function check(thisform) {
	flag = isRight(pwd)
	if (flag) {
		localStorage.setItem("pwd",pwd);
		alert("登录成功！\n欢迎回来！！！");
		window.document.f.action="home.html";
		window.document.f.submit();
	}
	else{
		alert("用户名或密码错误！");
	}
}
