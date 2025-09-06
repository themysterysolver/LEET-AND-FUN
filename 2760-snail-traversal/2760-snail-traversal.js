/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    let nums = this;
    console.log(nums);
    let grid = Array.from({length:rowsCount},()=>Array(colsCount).fill(0));
    let flag = true
    count = 0
    if(rowsCount*colsCount!==nums.length){
        return []
    }
    for(let j = 0;j<colsCount;j++){
        if(flag){
            for(let i = 0;i<rowsCount;i++){
                grid[i][j] = nums[count++];
            }
        }else{
            for(let i = rowsCount-1;i>-1;i--){
                grid[i][j] = nums[count++];
            }
        }
        flag=!flag
    }
    return grid
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */