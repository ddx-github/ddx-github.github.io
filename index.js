function check(thisform) {
	var name=document.getElementById("name").value;
	var pass=document.getElementById("pass").value;
	if (name=="ddx" && pass=="ddx110509" || name=="xrh" && pass=="xrh740920") {
		alert("登录成功！");
		window.document.f.action="test.html";
		window.document.f.submit();
	}
	else{
		alert("用户名或密码错误！");
	}
}
