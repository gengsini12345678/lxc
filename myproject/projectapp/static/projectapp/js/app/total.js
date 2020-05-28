/**
 * Created by Administrator on 2020/2/29.
 */

$(document).ready(function(){
    $('#total_money').click(function(){

        //获取单价
        var sale_price = $('#sale_price').val();
        // 获取数量
        var sale_number = $('#sale_number').val();

        if (sale_price == null || sale_price == ""){
            alert("必须填写单价");	//如果值为空，提示用户填写
        }
        if (sale_number == null || sale_number == ""){
            alert("必须填写数量");	//如果值为空，提示用户填写
        }
        var re = /^[0-9]+.?[0-9]*$/; //判断字符串是否为数字 //判断正整数 /^[1-9]+[0-9]*]*$/
        if (!re.test(sale_number)) {

            alert("数量必须为数字");
        }
        if (!re.test(sale_price)) {

            alert("价格必须为数字");
        }
        var total = sale_number * sale_price
        $('#total_money').val(total);
        //alert("单价："+sale_price+"数量："+sale_number+"总价："+total);

    })
})





