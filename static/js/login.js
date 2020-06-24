$(function () {
    // $("#username").blur(function () {
    //     if ($(this).val().length===0)
    //         return;
    //     else
    //         $.get("/Check_users",{'username':$(this).val()},
    //             function (data) {
    //             $("#username").next().html(data.msg);
    //
    //         },'json');
    //
    // });

    // if ({{ error_name }} == 1){
    //
    //     $('.user_error').html('用户名错误');
    //
    //     }
    $(function () {
        Check_dm();
    });
    function Check_dm() {
        $.get("/Check_dm", function (data) {
            var html = "";
            var Collection = "";
            if (data.status === 0){
                html +="<a href='/login'>登录</a>";
                html +="<span>|</span>";
                html +="<a href='/register'>注册</a>";
            }
            else{
                html +="欢迎您："+"<em>"+data.user+"</em>";
                html +="<span>|</span>";
                html +="<a href='/loginout'>退出</a>";
                Collection +="<a class='cart_name fl' href='/love'>收藏</a>";
                Collection +="<div class='goods_count fl' >"+data.number+"</div>";
            }
                $("#longin").html(html);
                $("#Collection").html(Collection);
        },'json');
    }










});