class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const res = [];
        let sum = 1;
        console.log(nums.length)
        for (let i = 0; i < nums.length; i++) {
            for (let j = 0; j < nums.length; j++) {
                if (res.length === j ) {
                    continue
                }
                console.log(nums[j])
                sum *= nums[j]
            }
            res.push(sum)
            sum = 1
        }
        return res
    }
}
