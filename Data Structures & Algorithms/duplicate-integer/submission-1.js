class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const newNum = new Set(nums);
        if(nums.length === newNum.size){
            return false
        }
        return true
    }
}
