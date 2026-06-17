class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

        const count = {}
        const arr = Array.from({length: nums.length + 1},() => [])

        for(const n of nums){
            //vales as key : count as value
            count[n] = (count[n] || 0) +1; 
        }
            //index which is values
        for (const i in count){
            //count as index : value as field
            arr[count[i]].push(i)
        }

        const res = [];
        for (let i = arr.length -1; i > 0; i--){
            for(const val of arr[i]){
                res.push(val)
                if(res.length === k){
                    return res
                }
            }
        }
    }
}
