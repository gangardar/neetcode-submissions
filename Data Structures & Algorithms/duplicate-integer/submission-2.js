class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const newNums = new Set(nums);
        console.log(newNums.size)
        if(nums.length === newNums.size){
            return false
        }else{
            return true
        }
    }
}
