class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(let j = 0; j<nums.length; j++) {
            for(let i=0; i < nums.length; i ++){
                if(j == i)
                    continue
                if(nums[j] + nums[i] === target){
                    return [j, i]
                }
            }
        }
    }
}
