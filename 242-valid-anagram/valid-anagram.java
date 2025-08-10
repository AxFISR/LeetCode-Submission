class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
            }
        int len = s.length();
        int[] myArr = new int[26];
        for (int i = 0 ; i < len ; i++){
            myArr[s.charAt(i) - 'a' ]++;
            myArr[t.charAt(i) - 'a' ]--;
        }
        for(int j = 0 ; j < 26 ; j++){
            if(myArr[j] != 0){
                return false;
                }
        }
        return true;
    }
}