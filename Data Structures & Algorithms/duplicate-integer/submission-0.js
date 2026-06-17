class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let istrue = false;
        nums.forEach((num , index) => {
            for(let i = 0; i < nums.length; i++){
                if(index === i)
                    continue
                if(num === nums[i])
                    istrue = true;
            }
        })

        return istrue;
    }
}
