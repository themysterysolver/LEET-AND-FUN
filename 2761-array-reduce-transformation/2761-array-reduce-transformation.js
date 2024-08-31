/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var array=[]
    var val=init;
    for(var i=0;i<nums.length;i++){
        array.push(fn(val,nums[i]));
        val=array[i];
    }
    return val;
};