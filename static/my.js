function mapToList(array,map){
    for(let key of map){
      array.push(key[1]);
    }
    return array;
}
function mapLength(map){
    return mapToList(new Array(), map).length;
}

function mapToStr(map) {
    let str = '{';
    let i = 0;
    for(let x of map){
        i++;
        if(getMapLength(map)===i){
            str += x[0]+':'+x[1];
        }else {
            str += x[0]+':'+x[1]+',';
        }
    }
    str += '}';
    return str;
}
function getMapLength(map){
    let count = 0;
    for(let i of map){
   　　count++;
　　}
　　return count;　　
}
function strToMap(str) {
    let map = new Map();
    let array = new Array();
    array = str.replace('{','').replace('}','').split(',');
    for(let i=0;i<array.length;i++){
        map.set(array[i].split(':')[0], array[i].split(':')[1])
    }
    return map
}
function getJsonLast(obj) {
    let k;
    let i = 0;
    for(k in obj){
        i++;
        if(Object.keys(obj).length === i){
            let json = {};
            json[k]=obj[k]
        	return json
        }
    }
}
function postData() {
    $.post("/getjson",{
		"csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val(),
	    },function(data,status){
          console.log(data)
        });
}
