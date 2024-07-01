$(function() {
  pwd = localStorage.getItem("pwd")
  if (pwd == null || !isRight(pwd)) {
    alert("登录过期，请重新登录!")
    var target = "https://ddx-github.github.io/?target=" + window.location.href
    window.location.replace(target)
  }
})
