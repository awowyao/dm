function love() {
    $.get('/Collection',function (data) {

        $.each(data,function (i,a_dm) {
            var jsonType = JSON.parse(a_dm.a_dm);
            var show ="";
            $.each(jsonType,function (i,a) {
                show +="<li>";
                show +="<a href'={{a.web}}'><img src='/"+a.fields.l_ing+"'></a>";
                show +="<h4><a href='"+a.fields.web+"'>"+a.fields.name+"</a></h4>";
                show +="<div class='operate'>";
                show +="<span class='prize'>提取码</span>";
                show +="<span class='unit'>"+a.fields.code+"</span>";
                show +="<button><a href='javascript:dellove("+a.pk+")'>删除收藏</a></button>";
                show +="</div>";
                show +="</li>";

                });

            $("#Collection").html(show);
        });
        },'json');

}

function dellove(pk){
    $.get('/del_Collection',{'a_id':pk},function (data) {
        $.each(data, function (i, a_dm) {
            alert('删除成功');
            var jsonType = JSON.parse(a_dm);
            var show = "";
            $.each(jsonType, function (i, a) {
                show += "<li>";
                show += "<a href'={{a.web}}'><img src='/" + a.fields.l_ing + "'></a>";
                show += "<h4><a href='" + a.fields.web + "'>" + a.fields.name + "</a></h4>";
                show += "<div class='operate'>";
                show += "<span class='prize'>提取码</span>";
                show += "<span class='unit'>" + a.fields.code + "</span>";
                show += "<button><a href='javascript:dellove(" + a.pk + ")'>删除收藏</a></button>";
                show += "</div>";
                show += "</li>";

                });
            $("#Collection").html(show);
        });

    },'json');
}

$(function () {
    love();
});