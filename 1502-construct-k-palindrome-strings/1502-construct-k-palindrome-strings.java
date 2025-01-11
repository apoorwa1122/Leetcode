class Solution {
    public boolean canConstruct(String s, int k) {
        int n = s.length();
        if(n<k) return false;
        if(n==k) return true;
        int[] freq = new int[26];
        int odd =0 ;
        for(char ch:s.toCharArray()){
            freq[ch-'a']++;
        }
        for(int count : freq){
            if(count%2==1){
                odd++;
            }
        }
        return odd<=k;
    }
}