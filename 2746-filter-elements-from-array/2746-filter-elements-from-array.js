/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var array=[]
    for(var i=0;i<arr.length;i++){
        if(fn(arr[i],i)){
            array.push(arr[i]);
        }
    }
    return array;
};