function dm() {
    $.get('/anime',function (data) {
        var show = "";
        var sort = "";
        sort +="<li><a href=''>排序：</a></li>";
        sort +="<li><a href='javascript:sort(1)'>时间　</a></li>　";
        sort +="<li><a href='javascript:sort(2)'>名字</a></li>";
        $.each(data,function (i,obj) {
            var jsonType=JSON.parse(obj.ani);
            console.log(jsonType);
            // show +="<ul class='goods_list fl'>";
            show +=" <li>";
            show +="<button><a href='javascript:add("+jsonType.id+");'>添加收藏</a></button>";
            show +="<h4><a href='"+jsonType.web+"'>"+"<button>百度云"+jsonType.code+"</button></a></h4>";
            show +="<a><img src='/"+jsonType.l_ing+"'></a>";
            show +="<div class='prize'>"+jsonType.neme+"</div>";
            show +="</li>";
            // show +="</ul>";
        });

        $("#ani").html(show);
        $("#sort").html(sort);
    },'json');
}

    function sort(sort) {
        var show = "";
        $.get('/dm_sort',{'sort':sort},function (data) {
            $.each(data,function (i,dm_sort) {
                var sort = JSON.parse(dm_sort);
                $.each(sort,function (i,a) {
                    show +=" <li>";
                    show +="<button><a href='javascript:add("+a.pk+");'>添加收藏</a></button>";
                    show +="<h4><a href='"+a.fields.web+"'>"+"<button>百度云"+a.fields.code+"</button></a></h4>";
                    show +="<a><img src='/"+a.fields.l_ing+"'></a>";
                    show +="<div class='prize'>"+a.fields.name+"</div>";
                    show +="</li>";
                });
            });
            $("#ani").html(show);
        },'json');

    }

function add(id){
    $.get('/addlove',{'id':id},function (data) {
        console.log(data.status);
        var Collection="";
        if (data.status ===0){
            alert('请登录')
        }
        else {
            if (data.status === 1) {
                alert('添加成功');
                Collection += "<a class='cart_name fl' href='/love'>收藏</a>";
                Collection += "<div class='goods_count fl' >" + data.number + "</div>";
                $("#Collection").html(Collection);
            } else
                alert('已经拥有')
        }
    },'json');
}
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
$(function () {
    dm();
    Check_dm();
});