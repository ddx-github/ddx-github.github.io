function check(thisform) {
	var name=document.getElementById("name").value;
	var pass=document.getElementById("pass").value;
	if (name=="ddx" && pass=="ddx110509" || name=="xrh" && pass=="xrh740920") {
		localStorage.setItem("user",name)
		localStorage.setItem("pwd",pass)
		alert("登录成功！");
		window.document.f.action="home.html";
		window.document.f.submit();
	}
	else{
		alert("用户名或密码错误！");
	}
}
