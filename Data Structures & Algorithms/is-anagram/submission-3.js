class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    // isAnagram(s, t) {
    //     if(s.length !== t.length){
    //         return false
    //     }

    //     const countS = {}
    //     const countT = {}

    //     for(let i = 0; i < s.length; i++){
    //         countS[s[i]] = (countS[s[i]] || 0) + 1
    //         countT[t[i]] = (countT[t[i]] || 0) + 1
    //     }

    //     for(const key in countT){
    //         if(countS[key] !== countT[key])
    //             return false
    //     }

    //     return true
    // }

    isAnagram(s,t) {
        if(s.length !== t.length){
            return false;
        }

        const countT = {};
        const countS = {};

        console.log(s.length)

        for(let i = 0; i < s.length; i++){
            countT[t[i]] = (countT[t[i]] || 0) + 1;
            countS[s[i]] = (countS[s[i]] || 0) + 1;
        }

        console.log(countT, countS)

        for( let i in countT){
            if(countT[i] !== countS[i]){
                return false
            }
        }

        return true




    }
}
