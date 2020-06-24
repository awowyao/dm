$(function () {
    var user_name = 0;
    var pwd = 0;
    var cpwd = 0;
    var email = 0;
    //手机号是否已经被注册的状态

    $("#email").blur(function () {
        check_email();
    });

    $("#user_name").blur(function () {
        add();
    });

    function add() {
        var len = $("#user_name").val().trim().length;
        if (len >= 2 && len <= 10) {
            $.get('/Check_users',
                {'uphone': $("#user_name").val()},
                function (data) {
                    $("#user_name").next().show().html(data.msg);
                    user_name = data.status;
                }, 'json'
            );
        } else {
            $("#user_name").next().html('用户名必须要2到10位');
            $("#user_name").next().show();
        }
        ;
    }

    $("#pwd").blur(function () {
        var len = $(this).val().trim().length;
        if (len >= 8 && len < 20) {
            $('#pwd').next().html(null);
            pwd = 1
        }
        else {
            $("#pwd").next().html("密码最少8位，最长20位");
            $("#pwd").next().show();
            pwd = 0
        }


    });

    $("#cpwd").blur(function () {
        var pwd = $("#pwd").val().trim();
        if (pwd ===$(this).val().trim()) {
            $("#cpwd").next().html("");
            cpwd = 1;
        }
        else {
            $("#cpwd").next().html("密码不一样");
            $('#cpwd').next().show();
            cpwd = 0
        }
    });
    	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val())) {

            $('#email').next().html(null);
            email = 1;
        }

		else {
            $('#email').next().html('你输入的邮箱格式不正确')
            $('#email').next().show();
            email = 0;
        }
	}
    // user_name.blur(function () {
    //     if ($(this).val().trim().length>2 && $(this).val().trim().length<10 )
    //         $("#error_tip").html(null);
    //     else
    //         $("#error_tip").html('用户名必须要2到10位');
    //
    // });
    // $("input[id='user_name']").blur(function () {
    //     if ($(this).val().trim().length == 0)
    //         return;
    //     $.get('/aj',
    //         {'uphone':$(this).val()},
    //         function (data) {
    //         $("#error_tip").html(data.msg);
    //         window.registStatus= data.status;
    //         console.log("data.status"+data.status)
    //         },'json'
    //     );
    //
    // });
    /*submit是也不允许表单提交 */
    $("#formReg").submit(function () {
        if (user_name===1&&pwd ===1 && cpwd ===1 && email ===1)
            return true;
        else
            return false;

    });






});